#!/usr/bin/env python3
import requests
import sys
import json

def send_input_to_ollama(user_input):
    prompt = f"You are a Linux expert. Return only the Linux command for the following task, no explanation: Task:\n\n{user_input}"
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
    print("=== AI Command Assistant ===")
    print("Type what you want to do in plain English.")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            if not user_input:
                continue
            result = send_input_to_ollama(user_input)
            print(f"Command: {result}\n")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break