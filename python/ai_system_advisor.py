#!/usr/bin/env python3
import requests
import sys
import json
import psutil
from datetime import datetime

THRESHOLD_CPU = 80
THRESHOLD_MEM = 80
THRESHOLD_DISK = 80

def collect_stats():
    return {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent
    }

def analyze_with_ollama(stats):
    prompt = f"You are a Linux system engineer. Analyze the following system stats and provide recommendations:\n\nCPU: {stats['cpu']}%\nMemory: {stats['memory']}%\nDisk: {stats['disk']}%"
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post("http://localhost:11434/api/generate", json=payload)
    if response.status_code == 200:
        return response.json().get("response", "")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return ""
    
if __name__ == "__main__":
    print("=== AI System Advisor ===")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Collecting system stats...")
    
    stats = collect_stats()
    print(f"CPU: {stats['cpu']}%")
    print(f"Memory: {stats['memory']}%")
    print(f"Disk: {stats['disk']}%")
    
    print("\nSending to Ollama for analysis...")
    result = analyze_with_ollama(stats)
    print("\n--- AI Advice ---")
    print(result)