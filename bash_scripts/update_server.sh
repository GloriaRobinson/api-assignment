#!/bin/bash

LOG_FILE="/var/log/update.log"
REPO_DIR="/var/www/html/api-assignment"
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

echo "$TIMESTAMP - Starting update" >> $LOG_FILE
sudo apt update && sudo apt upgrade -y >> $LOG_FILE

cd $REPO_DIR
git pull origin main >> $LOG_FILE
if [ $? -ne 0 ]; then
  echo "$TIMESTAMP - Git pull failed" >> $LOG_FILE
  exit 1
fi

systemctl restart apache2
echo "$TIMESTAMP - Server update completed" >> $LOG_FILE
