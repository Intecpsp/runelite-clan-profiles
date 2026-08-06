#!/usr/bin/env python3
"""
Helper script to export clean, sanitized RuneLite profiles and sync tools
from ~/.runelite to this clan repository directory.
"""
import os
import shutil
import re

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
PROFILES_TARGET = os.path.join(REPO_DIR, 'profiles')
PROFILES_SOURCE = os.path.expanduser('~/.runelite/profiles2')
SYNC_SCRIPT_SOURCE = os.path.expanduser('~/.runelite/sync_base_profile.py')

os.makedirs(PROFILES_TARGET, exist_ok=True)

# Copy sync script
if os.path.exists(SYNC_SCRIPT_SOURCE):
    shutil.copy2(SYNC_SCRIPT_SOURCE, os.path.join(REPO_DIR, 'sync_base_profile.py'))
    print('[EXPORT] Copied sync_base_profile.py')

# Generic sensitive prefixes to filter out
sensitive_key_prefixes = [
    'dudewheresmystuff.rsprofile.',
    'rsprofile.loginsalt',
    'rsprofile.',
    'dinkplugin.primarywebhook',
    'dinkplugin.secondarywebhook',
    'osrstcg.pullwebhookurl'
]

copied = 0
for f in os.listdir(PROFILES_SOURCE):
    if f.endswith('.properties') and not f.startswith('$rsprofile') and not f.startswith('.'):
        src = os.path.join(PROFILES_SOURCE, f)
        dst = os.path.join(PROFILES_TARGET, f)
        
        lines = []
        with open(src, 'r', encoding='utf-8', errors='ignore') as fp:
            for line in fp:
                line_str = line.strip()
                if not line_str or line_str.startswith('#'):
                    lines.append(line)
                    continue
                
                # Filter out account-specific storage & credentials
                k = line_str.split('=', 1)[0].strip().lower()
                if any(k.startswith(p.lower()) for p in sensitive_key_prefixes):
                    continue
                
                # Replace active Discord webhook URLs with clean placeholders
                if 'discord.com/api/webhooks' in line:
                    k_name, _ = line_str.split('=', 1)
                    line = f'{k_name}=https\\://discord.com/api/webhooks/YOUR_WEBHOOK_HERE\n'
                
                lines.append(line)
        
        with open(dst, 'w', encoding='utf-8') as fp:
            fp.writelines(lines)
        copied += 1

print(f'[EXPORT] Successfully exported and sanitized {copied} profile properties files to {PROFILES_TARGET}')
