#!/usr/bin.env python3
import sys
from datetime import datetime

def analyze_log(file_path):
    error_count = 0
    warning_count = 0
    info_count = 0
    error_lines = []

    with open(file_path, 'r') as f:
        for line in f:
            if "ERROR" in line:
                error_count += 1
                error_lines.append(line.strip())
            elif "WARNING" in line:
                warning_count += 1
            elif "INFO" in line:
                info_count += 1
    print(f"=== Log Analysis Report ===")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"File: {file_path}")
    print(f"---")
    print(f"INFO:    {info_count}")
    print(f"WARNING: {warning_count}")
    print(f"ERROR:   {error_count}")

    if error_lines:
        print(f"--- Error Details ---")
        for line in error_lines:
            print(f"  {line}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 log_analyzer.py <logfile>")
        sys.exit(1)
    analyze_log(sys.argv[1])
    
