# Gitea Fake Followers

![Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)
![Gitea](https://img.shields.io/badge/Gitea-API-609926?logo=gitea)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

Creates fake accounts on a Gitea instance and makes them follow a target user. Saves created accounts to a local SQLite database.

---

## Setup

1. `pip install requests`
2. Set your values in the config block:

```python
GITEA_URL    = "http://your-gitea-instance/api/v1"
ADMIN_TOKEN  = "your-admin-token"
TARGET_USER  = "username-to-follow"
```

3. Run: `python ccg.py`

---

## How it works

- Prompts for how many followers to create
- Creates random accounts via Gitea admin API
- Each account follows `TARGET_USER`
- Saves all credentials to `users.db`
