#!/bin/bash

# Configuration
# APP_DIR is the directory where this script resides
APP_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PORT=8899

cd "$APP_DIR"

# 1. Update Code
echo "Pulling latest code..."
git pull origin main

# 2. Restart Application with Docker Compose
echo "Restarting application using Docker Compose..."
# -d: run in background
# --build: rebuild images before starting containers
docker compose up -d --build

echo "Deployment complete. App is running via Docker Compose on port 8899."
