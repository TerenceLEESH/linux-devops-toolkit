#!/usr/bin/env bash
set -euo pipefail

echo " Network Check Report - $(date '+%Y-%m-%d %H:%M:%S')"

IP_ADDR=$(ip addr show eth0 | grep "inet " | awk '{print $2}')
echo "--- Network Interface ---"
echo "IP Address: $IP_ADDR"

echo "--- Connectivity Check ---"

check_host() {
    local host=$1
    if curl -s --connect-timeout 3 "$host" &>/dev/null; then
        echo "  $host: REACHABLE"
    else
        echo "  $host: UNREACHABLE"
    fi
}

check_host "google.com"
check_host "github.com"
check_host "8.8.8.8"

echo "--- Port Check ---"

# nc -z = zero I/O mode (just check port), -w3 = timeout 3 seconds
check_port() {
    local host=$1
    local port=$2
    if nc -zw3 "$host" "$port" &>/dev/null; then
        echo "  $host:$port OPEN"
    else
        echo "  $host:$port CLOSED/FILTERED"
    fi
}

check_port "google.com" 80
check_port "google.com" 443
check_port "google.com" 22