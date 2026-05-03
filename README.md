# linux-devops-toolkit
This is the toolkit that for daily Linux DevOps and SysAdmin tasks.
Built as a learning project to develop system admin skills

## Features
- System health check - CPU, memory, disk usage
- Log cleanup - automatically delete old log files by retention days
- User management - create Linux users with home directory and sudo access
- Network check — verify IP, connectivity and port status
- System monitor — Python-based resource monitor with threshold alerts
- Log analyzer — parse log files and summarise errors and warnings

## Requirements
- Linux OS (Ubuntu/Debian recommended)
- Bash 4.0+
- Python 3.8+
- psutil library (`pip install psutil`)

## Installation
```bash
git clone https://github.com/YOUR_USERNAME/linux-devops-toolkit.git
cd linux-devops-toolkit
pip install psutil
```

## Usage
### system_status.sh
```bash
bash bash/system_status.sh
```

### log_cleanup.sh
```bash
bash bash/log_cleanup.sh /var/log 7
```

### user_create.sh
```bash
sudo bash bash/user_create.sh username
```

### network_check.sh
```bash
bash bash/network_check.sh
```

### system_monitor.py
```bash
python3 python/system_monitor.py
```

### log_analyzer.py
```bash
python3 python/log_analyzer.py /var/log/syslog
```

## Use Cases
- Quickly check server health before deployment
- Schedule log cleanup with cron jobs
- Onboard new team members with automated user setup
- Diagnose network connectivity issues on a server
- Monitor resource usage and get alerted before things break
