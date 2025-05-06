# 0x01. NoSQL

## 📁 Project Overview

**Track:** Back-end  
**Focus:** NoSQL and MongoDB  
**Weight:** 1  
**Start Date:** May 4, 2025, 6:00 PM  
**End Date:** May 6, 2025, 6:00 PM  
**Checker Release:** May 5, 2025, 6:00 AM  
**Auto Review:** Triggered at deadline  

This project introduces NoSQL concepts using MongoDB and its integration with Python. You'll work with `mongo` shell commands and Python (via PyMongo) to manipulate document-based data.

---

## 📚 Resources

Read or watch the following to build a solid foundation:

- [NoSQL Databases Explained](https://www.youtube.com/watch?v=qI_g07C_Q5I)
- [What is NoSQL?](https://www.mongodb.com/nosql-explained)
- [MongoDB with Python Crash Course - Tutorial for Beginners](https://www.youtube.com/watch?v=E-1xI85Zog8)
- [MongoDB Tutorial 2: Insert, Update, Remove, Query](https://www.youtube.com/watch?v=DoHT7Qw3C3c)
- [Aggregation](https://docs.mongodb.com/manual/aggregation/)
- [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)
- [mongo Shell Methods](https://www.mongodb.com/docs/manual/reference/method/)
- [Mongosh](https://www.mongodb.com/docs/mongodb-shell/)

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain:

### General
- What NoSQL means
- Differences between SQL and NoSQL
- What ACID means
- What document storage is
- Types of NoSQL databases
- Benefits of NoSQL databases
- How to query from a NoSQL database
- How to insert, update, and delete data in NoSQL
- How to use MongoDB in the shell and via Python

---

## ✅ Requirements

### MongoDB Shell Scripts
- Ubuntu 18.04 LTS, MongoDB v4.2
- First line must be a comment (`// my comment`)
- File must end with a new line
- Must pass `wc` tests
- Required file: `README.md`

### Python Scripts
- Ubuntu 18.04 LTS, Python 3.7, PyMongo 3.10
- Shebang: `#!/usr/bin/env python3`
- Follow `pycodestyle` (v2.5.*)
- All functions and modules must be documented
- No top-level script execution allowed
- Required file: `README.md`

---

## ⚙️ MongoDB Installation (Ubuntu 18.04)

```bash
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo mkdir -p /data/db
sudo service mongod start
mongo --version
Author: Dzeble Kwame
