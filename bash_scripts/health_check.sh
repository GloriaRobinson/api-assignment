#!/bin/bash

LOG_FILE="/var/log/server_health.log"
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

CPU=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
MEM=$(free -m | awk '/Mem:/ { printf("%.2f"), $3/$2*100 }')
DISK=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')

echo "$TIMESTAMP - CPU: $CPU%, MEM: $MEM%, DISK: $DISK%" >> $LOG_FILE

if ! systemctl is-active --quiet apache2; then
  echo "$TIMESTAMP - Apache is down" >> $LOG_FILE
fi

for ENDPOINT in "/students" "/subjects"; do
  STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost$ENDPOINT)
  if [ "$STATUS" != "200" ]; then
    echo "$TIMESTAMP - $ENDPOINT returned $STATUS" >> $LOG_FILE
  fi
done

if [ "$DISK" -gt 90 ]; then
  echo "$TIMESTAMP - WARNING: Disk space above 90%" >> $LOG_FILE
fi
