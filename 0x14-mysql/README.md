## 0x14. Mysql
---

### Task
---

0. Install MySQL 
1. Let us in! 
2. If only you could see what I've seen with your eyes
3. Quite an experience to live in fear, isn't it? 
4. Setup a Primary-Replica infrastructure using MySQL
5. MySQL backup 

### Description
---

0. First things first, let’s get MySQL installed on both your web-01 and web-02 servers.
1. In order for us to verify that your servers are properly configured, we need you to create a user and password for both MySQL databases which will allow the checker access to them.
2. In order for you to set up replication, you’ll need to have a database with at least one table and one row in your primary MySQL server (web-01) to replicate from.
3. Before you get started with your primary-replica synchronization, you need one more thing in place. On your primary MySQL server (web-01), create a new user for the replica server.
4. Having a replica member on for your MySQL database has 2 advantages:
5. Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.
