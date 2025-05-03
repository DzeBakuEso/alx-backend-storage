## 0x00. MySQL Advanced

### Project Overview
This project focuses on advanced MySQL concepts including table creation with constraints, query optimization with indexes, stored procedures, functions, views, and triggers. The project consists of several tasks that demonstrate these concepts in practice.

### Project Details
- **Weight**: 1
- **Start Date**: Apr 29, 2025, 6:00 PM
- **End Date**: May 1, 2025, 6:00 PM
- **Checker Release**: Apr 30, 2025, 6:00 AM
- **Auto Review**: Launched at the deadline

### Concepts Covered
- Advanced SQL

### Resources
- [MySQL Cheatsheet](https://example.com/mysql-cheatsheet)
- [MySQL Performance: Database Indexing](https://example.com/mysql-indexing)
- [Stored Procedures](https://example.com/stored-procedures)
- [Triggers](https://example.com/triggers)
- [Views](https://example.com/views)
- [Functions and Operators](https://example.com/mysql-functions)
- [Trigger Syntax and Examples](https://example.com/trigger-syntax)
- [CREATE TABLE Statement](https://example.com/create-table)
- [CREATE PROCEDURE and CREATE FUNCTION](https://example.com/create-procedure)
- [CREATE INDEX Statement](https://example.com/create-index)
- [CREATE VIEW Statement](https://example.com/create-view)

### Learning Objectives
By the end of this project, you should be able to:
- Create tables with constraints
- Optimize queries by adding indexes
- Implement stored procedures and functions
- Implement views in MySQL
- Implement triggers in MySQL

### Requirements
- All files executed on Ubuntu 18.04 LTS using MySQL 5.7
- Files must end with a new line
- SQL queries must have comments
- Files must start with a task description
- SQL keywords must be uppercase
- README.md file is mandatory
- File length checked with `wc`

### Tasks

#### 0. We are all unique!
Create a table `users` with:
- `id`: integer, never null, auto increment, primary key
- `email`: string (255 chars), never null, unique
- `name`: string (255 chars)
- Script should not fail if table exists
- Executable on any database

#### 1. In and not out
Create a table `users` with:
- `id`: integer, never null, auto increment, primary key
- `email`: string (255 chars), never null, unique
- `name`: string (255 chars)
- `country`: enum (US, CO, TN), never null (default US)
- Script should not fail if table exists
- Executable on any database

#### 2. Best band ever!
Rank country origins of bands by number of (non-unique) fans:
- Import `metal_bands.sql.zip`
- Column names: `origin` and `nb_fans`
- Executable on any database

#### 3. Old school band
List all bands with Glam rock as main style, ranked by longevity:
- Import `metal_bands.sql.zip`
- Column names: `band_name` and `lifespan` (years until 2022)
- Use attributes `formed` and `split` for lifespan
- Executable on any database

#### 4. Buy buy buy
Create a trigger that decreases item quantity after adding a new order:
- Quantity in `items` can be negative
- Demonstrates maintaining data consistency through triggers

### How to Use
1. Start MySQL service: `service mysql start`
2. Execute SQL files: `cat filename.sql | mysql -uroot -p database_name`
3. Credentials: root/root

### Example Import
```bash
echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
curl "https://example.com/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows

Author: Dzeble Kwame Baku
