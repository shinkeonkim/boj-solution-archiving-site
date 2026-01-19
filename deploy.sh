#!/bin/bash

# Configuration
# APP_DIR is the directory where this script resides
APP_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PORT=8899

cd "$APP_DIR"

# 1. Update Code
echo "Pulling latest code..."
git pull origin main

# 2. Update Dependencies
echo "Syncing dependencies..."
uv sync

# 3. Restart Application
echo "Restarting application..."
# Find and kill existing uvicorn process running on the specific port
# Note: Using pkill instead of lsof to prevent hanging on container/k8s overlay filesystems
echo "Stopping existing process... (Pattern: uvicorn main:app ... $PORT)"
pkill -f "uvicorn main:app --host 0.0.0.0 --port $PORT" || true

# Wait a moment for cleanup
sleep 2

# Start new process in background
nohup uv run uvicorn main:app --host 0.0.0.0 --port $PORT > app.log 2>&1 &

echo "Deployment complete. App running on port $PORT"
