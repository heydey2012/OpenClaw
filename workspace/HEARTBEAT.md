# HEARTBEAT.md

# Keep this file empty (or with only comments) to skip heartbeat API calls.

# Add tasks below when you want the agent to check something periodically.

## Backup Routine
- [ ] Check if workspace is clean (`git status --porcelain`)
- [ ] If changes exist, commit them with a timestamp: `git add . && git commit -m "Auto-backup: $(date)"`
