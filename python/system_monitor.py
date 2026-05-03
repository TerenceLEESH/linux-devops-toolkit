import psutil
from datetime import datetime

THRESHOLD_CPU = 80
THRESHOLD_MEM = 80
THRESHOLD_DISK = 80

def check_cpu():
    cpu = psutil.cpu_percent(interval=1)
    status = "ALERT" if cpu > THRESHOLD_CPU else "OK"
    print(f"CPU Usage:    {cpu}% [{status}]")

def check_memory():
    memory = psutil.virtual_memory()
    status = "ALERT" if memory.percent > THRESHOLD_MEM else "OK"
    print(f"Memory Usage: {memory.percent}% [{status}]")

def check_disk():
    disk = psutil.disk_usage('/')
    status = "ALERT" if disk.percent > THRESHOLD_DISK else "OK"
    print(f"Disk Usage: {disk.percent}% [{status}]")

if __name__ == "__main__":
    print("=== System Monitor ===")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    check_cpu()
    check_memory()
    check_disk()