#!/usr/bin/env bash
set -euo pipefail

RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
RESET='\033[0m'

colour() {
    local val=$1
    if [ "$val" -gt 90 ]; then
        echo -e "${RED}${val}%${RESET}"
    elif [ "$val" -gt 70 ]; then
        echo -e "${YELLOW}${val}%${RESET}"
    else
        echo -e "${GREEN}${val}%${RESET}"
    fi
}

echo " System Status Report - $(date '+%Y-%m-%d %H:%M:%S')"

echo "--- CPU ---"
CPU_IDLE=$(top -bn1 | grep "Cpu" | awk '{print $8}')
CPU_USAGE=$(awk "BEGIN {printf \"%.1f\", 100 - $CPU_IDLE}")
echo "CPU Usage: $(colour ${CPU_USAGE%.*})"

echo "--- Memory ---"
MEM_TOTAL=$(free -m | awk 'NR==2 {print $2}')
MEM_USED=$(free -m | awk 'NR==2 {print $3}')
MEM_PCT=$(awk "BEGIN {printf \"%.1f\", ($MEM_USED/$MEM_TOTAL)*100}")
echo "Memory Usage: $MEM_USED MB / $MEM_TOTAL MB ($(colour ${MEM_PCT%.*}))"

echo "--- Disk ---"
DISK_USAGE=$(df -h / | awk 'NR==2 {print $5}' | tr -d '%')
echo "Disk Usage: $(colour ${DISK_USAGE%})"