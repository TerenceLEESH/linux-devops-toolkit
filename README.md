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
./bash/system_status.sh
```

### log_cleanup.sh
```bash
./bash/log_cleanup.sh /var/log 7
```

### user_create.sh
```bash
sudo ./bash/user_create.sh username
```

### network_check.sh
```bash
./bash/network_check.sh
```

### system_monitor.py
```bash
python3 ./python/system_monitor.py
```

### log_analyzer.py
```bash
python3 ./python/log_analyzer.py /var/log/syslog
```

## Use Cases
- Quickly check server health before deployment
- Schedule log cleanup with cron jobs
- Onboard new team members with automated user setup
- Diagnose network connectivity issues on a server
- Monitor resource usage and get alerted before things break

## AI-Powered Scripts (Ollama)

### Setup
```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Start Ollama service
ollama serve &

# Pull the model
ollama pull llama3

# Install Python dependencies
pip3 install -r requirements.txt
```

### ai_log_analyzer.py
Analyzes log files using AI and explains root causes in plain English.
```bash
python3 python/ai_log_analyzer.py /var/log/syslog
```

### ai_system_advisor.py
Collects system stats and asks AI for health advice and tuning recommendations.
```bash
python3 python/ai_system_advisor.py
```

### ai_cmd_assistant.py
Type what you want to do in plain English, get the Linux command back.
```bash
python3 python/ai_cmd_assistant.py
```

## Roadmap
- Add email alerts to system_monitor.py
- Add cron job setup guide
- Support multiple log formats in log_analyzer.py
- Add more AI models support beyond Ollama3

## License
This project is licensed under the MIT License — see the LICENSE file for details.
