#!/usr/bin/env bash
set -euo pipefail

if [ $# -ne 1 ]; then
    echo "Usage: $0 <username>"
    exit 1
fi

USERNAME=$1

echo "Creating user '$USERNAME'..."

if id "$USERNAME" &>/dev/null; then
    echo "Error: user '$USERNAME' already exists"
    exit 1
fi

useradd -m -s /bin/bash "$USERNAME"
echo "User '$USERNAME' created successfully"

echo "Setting password for '$USERNAME'..."
passwd "$USERNAME"

read -p "Grant sudo access to '$USERNAME'? (y/n): " SUDO_CHOICE

if [ "$SUDO_CHOICE" = "y" ]; then
    usermod -aG sudo "$USERNAME"
    echo "Sudo access granted to '$USERNAME'"
else
    echo "Skipping sudo access for '$USERNAME'"
fi

echo "User '$USERNAME' setup complete."