#!/bin/bash

# Configuration
WORKSPACE_DIR="/Users/heydey/.openclaw/workspace"
DATE=$(date +"%Y-%m-%d %H:%M:%S")

# Navigate to workspace
cd "$WORKSPACE_DIR" || exit 1

# Check for changes (both staged and unstaged)
if [[ -n $(git status --porcelain) ]]; then
    # Add all changes
    git add .
    
    # Commit with timestamp
    git commit -m "Auto-backup: $DATE"
    
    # Optional: Log success (can be removed to keep silent)
    # echo "Backup created at $DATE" >> "$WORKSPACE_DIR/backup.log"
fi
