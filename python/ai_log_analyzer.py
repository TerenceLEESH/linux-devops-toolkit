#!/usr/bin/env python3
import requests
import sys
import json

def read_and_filter_logs(filepath):
    keywords = ["error", "warning", "fail", "critical"]
    filtered = []
    with open(filepath, 'r', errors='ignore') as f:
        for line in f:
            if any(k in line.lower() for k in keywords):
                filtered.append(line.strip())
    return filtered

def analyze_with_ollama(log_content):
    prompt = f"Analyze the following log content and summarize the key issues:\n\n{log_content}"
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
    if len(sys.argv) != 2:
        print("Usage: python3 ai_log_analyzer.py <logfile>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    print("=== AI Log Analyzer ===")
    print("Reading and filtering logs...")
    logs = read_and_filter_logs(filepath)
    
    if not logs:
        print("No errors or warnings found.")
        sys.exit(0)
    
    print(f"Found {len(logs)} error/warning lines. Sending to Ollama...")
    result = analyze_with_ollama("\n".join(logs[:20]))
    print("\n--- AI Analysis ---")
    print(result)