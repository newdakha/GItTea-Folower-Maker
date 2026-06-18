import sqlite3, random, string, requests

# ─── CONFIG ───────────────────────────────────────────────────────────────────
GITEA_URL   = "http://100.117.79.103:8080/api/v1"
ADMIN_TOKEN = "your-admin-token"
TARGET_USER = "newdakha"
# ──────────────────────────────────────────────────────────────────────────────

count   = int(input("How many followers to create?: "))
headers = {"Authorization": f"token {ADMIN_TOKEN}", "Content-Type": "application/json"}

conn   = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, email TEXT)")

for _ in range(count):
    rand     = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    username = rand
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12)) + "!"
    email    = f"{username}@local.com"

    res = requests.post(f"{GITEA_URL}/admin/users", headers=headers, json={
        "username": username, "password": password, "email": email,
        "must_change_password": False, "visibility": "public",
    })

    if res.status_code in (201, 211):
        cursor.execute("INSERT INTO users VALUES (?, ?, ?)", (username, password, email))
        conn.commit()
        requests.put(f"{GITEA_URL}/user/following/{TARGET_USER}", auth=(username, password))
        print(f"[+] {username} followed {TARGET_USER}")
    else:
        print(f"[-] Failed: {res.status_code}")

conn.close()
print("Done.")
