#!/bin/bash

API_DIR="/var/www/html/api-assignment"
BACKUP_DIR="/home/ubuntu/backups"
LOG_FILE="/var/log/backup.log"
DATE=$(date +%F)

mkdir -p $BACKUP_DIR

tar -czf $BACKUP_DIR/api_backup_$DATE.tar.gz $API_DIR
if [ $? -eq 0 ]; then
  echo "$DATE - API backup successful" >> $LOG_FILE
else
  echo "$DATE - API backup FAILED" >> $LOG_FILE
fi

# Optional: Add database dump
# mysqldump -u root -p[password] dbname > $BACKUP_DIR/db_backup_$DATE.sql

# Delete old backups
find $BACKUP_DIR -type f -mtime +7 -exec rm {} \;
