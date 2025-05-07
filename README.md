# Flask API Assignment

## Description
This project is a simple Flask API that handles subjects in a university program.

## Backup Schemes

### 1. Full Backup
**Description:** Complete copy of all data
- **Advantages:** 
  - Simple to implement and restore
  - Complete point-in-time recovery
- **Disadvantages:**
  - Takes more storage space
  - Longer backup time
  - Higher network bandwidth usage

### 2. Incremental Backup
**Description:** Only backs up changes since last backup
- **Advantages:**
  - Faster backup process
  - Less storage space needed
  - Reduced network load
- **Disadvantages:**
  - More complex restoration process
  - Requires base backup
  - Longer recovery time

### 3. Differential Backup
**Description:** Backs up changes since last full backup
- **Advantages:**
  - Faster than full backups
  - Simpler restore than incremental
  - Balance of space and speed
- **Disadvantages:**
  - More storage than incremental
  - Slower than incremental
  - Requires base backup

## Bash Scripts

### health_check.sh
Monitors server resources and API health.
- Checks CPU, memory, and disk usage
- Verifies Apache status
- Tests API endpoints
- Logs to /var/log/server_health.log

### backup_api.sh
Creates automated backups of the API.
- Backs up project files and database
- Maintains 7-day retention
- Logs to /var/log/backup.log

### update_server.sh
Manages server and API updates.
- Updates system packages
- Pulls latest code
- Restarts services
- Logs to /var/log/update.log

## Setup Instructions
1. Clone the repository:
   git clone https://github.com/GloriaRobinson/api-assignment

2. Install dependencies:
python -m venv venv
source venv/bin/activate  
# On Windows use: venv\Scripts\activate

pip install flask flask-mysql-connector                                            

3. Configure your database with MySQL.

4.  run the app:
 
 python app.py

## Script Setup
1. Set execute permissions:
```bash
chmod +x bash_scripts/*.sh
```

2. Dependencies:
- curl
- mysql-client (for database backups)
- git
