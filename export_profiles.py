#!/usr/bin/env python3
"""
Helper script to export clean, sanitized RuneLite profiles and sync tools
from ~/.runelite to this clan repository directory, and automatically
update AUDIT_REPORT.md to reflect current active plugins, removing any deleted
plugins entirely and renumbering remaining entries within each section.
"""
import os
import shutil
import re

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
PROFILES_TARGET = os.path.join(REPO_DIR, 'profiles')
PROFILES_SOURCE = os.path.expanduser('~/.runelite/profiles2')
SYNC_SCRIPT_SOURCE = os.path.expanduser('~/.runelite/sync_base_profile.py')
AUDIT_PATH = os.path.join(REPO_DIR, 'AUDIT_REPORT.md')

os.makedirs(PROFILES_TARGET, exist_ok=True)

# 1. Copy sync script
if os.path.exists(SYNC_SCRIPT_SOURCE):
    shutil.copy2(SYNC_SCRIPT_SOURCE, os.path.join(REPO_DIR, 'sync_base_profile.py'))
    print('[EXPORT] Copied sync_base_profile.py')

# 2. Export, sanitize, and sort profile properties files alphabetically to eliminate git churn
sensitive_key_prefixes = [
    'dudewheresmystuff.rsprofile.',
    'rsprofile.loginsalt',
    'rsprofile.',
    'osrsprofile.',
    'dinkplugin.primarywebhook',
    'dinkplugin.secondarywebhook',
    'osrstcg.pullwebhookurl',
    'lastseenonline.',
    'friendnotes.',
    'friendlist.',
    'friendslist.',
    'party.previouspartyid',
    'partypanel.previouspartyid',
    'womutils.verificationcode',
    'womutils.groupid',
    'notes.',
    'notesplugin.',
    'clanchat.chatsdata'
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
        
        # Sort lines alphabetically by key to eliminate Java HashMap random ordering churn
        sorted_lines = sorted(lines, key=lambda l: l.split('=', 1)[0].lower())
        
        with open(dst, 'w', encoding='utf-8') as fp:
            fp.writelines(sorted_lines)
        copied += 1

print(f'[EXPORT] Successfully exported, sanitized, and sorted {copied} profile properties files to {PROFILES_TARGET}')

# 3. Dynamically discover profiles and active plugins (100% generic)
profile_map = {}
for f in os.listdir(PROFILES_TARGET):
    if f.endswith('.properties') and not f.startswith('$rsprofile') and not f.startswith('.'):
        pname = re.sub(r'-\d+\.properties$', '', f)
        profile_map[f] = pname

profile_active_plugins = {}
all_active_plugins = set()

for filename, pname in profile_map.items():
    path = os.path.join(PROFILES_TARGET, filename)
    plugins = set()
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
            for line in fp:
                line = line.strip()
                if line.startswith('runelite.externalPlugins='):
                    val = line.split('=', 1)[1]
                    plugins = set(x for x in val.split(',') if x)
    profile_active_plugins[pname] = plugins
    all_active_plugins.update(plugins)

# 4. Dynamically update AUDIT_REPORT.md
if os.path.exists(AUDIT_PATH):
    with open(AUDIT_PATH, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()

    new_lines = []
    current_sec_header_idx = -1
    sec_plugin_count = 0
    seen_plugins = set()
    dropped_plugins = []

    all_profile_names_str = ", ".join([f"`{p}`" for p in profile_map.values()])

    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Update summary table rows dynamically
        if line.startswith("| **`") and "`** | `" in line:
            for pname, pset in profile_active_plugins.items():
                if f"| **`{pname}`** |" in line:
                    line = re.sub(r"(\|\s*\*\*`[^`]+`\*\*\s*\|\s*`[^`]+`\s*\|\s*\*\*)\d+(\*\*\s*\|)", rf"\g<1>{len(pset)}\g<2>", line)
                    break
            new_lines.append(line)
            i += 1
            continue
        
        # Update total unique count
        if "for all **" in line and "unique external plugins**" in line:
            line = re.sub(r"(for all\s+\*\*)\d+(\s+unique external plugins\*\*)", rf"\g<1>{len(all_active_plugins)}\g<2>", line)
            new_lines.append(line)
            i += 1
            continue
        
        # Section header
        if line.startswith("## ") and not line.startswith("## 📊"):
            if current_sec_header_idx >= 0:
                hdr = new_lines[current_sec_header_idx]
                new_lines[current_sec_header_idx] = re.sub(r"(\s*-\s*)\d+(\s*Plugins\))", rf"\g<1>{sec_plugin_count}\g<2>", hdr)
            
            current_sec_header_idx = len(new_lines)
            sec_plugin_count = 0
            new_lines.append(line)
            i += 1
            continue
        
        # Generic plugin entry block match: ### <num>. `<plugin-id>`
        m = re.match(r"^### \d+\. `([^`]+)`", line)
        if m:
            plugin_id = m.group(1)
            block_lines = [line]
            i += 1
            while i < len(lines) and not lines[i].startswith("### ") and not lines[i].startswith("## ") and not lines[i].startswith("---"):
                block_lines.append(lines[i])
                i += 1
            
            active_for_plugin = [pname for pname, pset in profile_active_plugins.items() if plugin_id in pset]
            
            # Drop block if inactive across ALL profiles or already documented in a prior section
            if not active_for_plugin or plugin_id in seen_plugins:
                if not active_for_plugin:
                    dropped_plugins.append(plugin_id)
                continue
            
            seen_plugins.add(plugin_id)
            sec_plugin_count += 1
            
            # Renumber entry header
            block_lines[0] = re.sub(r"^### \d+\.", f"### {sec_plugin_count}.", block_lines[0])
            
            # Format active profiles string dynamically
            if len(active_for_plugin) == len(profile_map):
                active_str = f"All {len(profile_map)} Profiles ({all_profile_names_str})\n"
            else:
                active_str = ", ".join([f"`{p}`" for p in active_for_plugin]) + "\n"
            
            for j in range(1, len(block_lines)):
                if block_lines[j].startswith("* **Active Profiles:**"):
                    block_lines[j] = f"* **Active Profiles:** {active_str}"
                    break
            
            new_lines.extend(block_lines)
            continue
        
        new_lines.append(line)
        i += 1

    # Update last section header count
    if current_sec_header_idx >= 0:
        hdr = new_lines[current_sec_header_idx]
        new_lines[current_sec_header_idx] = re.sub(r"(\s*-\s*)\d+(\s*Plugins\))", rf"\g<1>{sec_plugin_count}\g<2>", hdr)

    with open(AUDIT_PATH, 'w', encoding='utf-8') as fp:
        fp.writelines(new_lines)
    
    print(f'[EXPORT] Successfully updated AUDIT_REPORT.md ({len(all_active_plugins)} active unique plugins, dropped {len(dropped_plugins)} deleted plugins).')
