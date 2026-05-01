#!/usr/bin/env bash
set -euo pipefail

if [ $# -ne 2 ]; then
    echo "Usage: $0 <directory> <days>"
    exit 1
fi

LOG_DIR=$1
DAYS=$2

if [ ! -d "$LOG_DIR" ]; then
    echo "Error: directory '$LOG_DIR' does not exist"
    exit 1
fi

echo "Cleaning log files older than $DAYS days in $LOG_DIR..."

FILE_COUNT=$(find "$LOG_DIR" -name "*.log" -mtime +$DAYS | wc -l)
echo "Found $FILE_COUNT file(s) to delete."

if [ "$FILE_COUNT" -eq 0 ]; then
    echo "No log files older than $DAYS days found. Nothing to clean."
    exit 0
fi

DELETED=0
while IFS= read -r file; do
    echo "Deleting: $file"
    rm -f "$file"
    DELETED=$((DELETED + 1))
done < <(find "$LOG_DIR" -name "*.log" -mtime +$DAYS)

echo "Done. $DELETED file(s) deleted."