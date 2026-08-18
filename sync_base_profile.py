#!/usr/bin/env python3
"""
RuneLite Two-Tier Master Base + Dynamic PvM Group + Universal Data Sync Script
========================================================================================
100% Pure File-Driven Architecture: ZERO Hardcoded Plugin Names in Python.

Two-Tier Master Hierarchy:
1. Master Base QoL (default-0.properties): Pushes universal QoL plugins & configs outward to ALL profiles.
2. Master PvM Combat Base (PvM-10.properties): Pushes shared combat plugins & configs outward to ALL Combat Profiles.
3. Activity Profiles: Dynamically discover and protect profile-specific exclusives directly from disk.
"""
import os
import sys
import json
import argparse
import re
import platform
import subprocess
import time
from typing import Dict, Set, List

PROFILES_DIR = os.path.expanduser("~/.runelite/profiles2")

def is_runelite_running() -> bool:
    """Cross-platform check to see if RuneLite process is active."""
    os_type = platform.system()
    try:
        if os_type == "Windows":
            cmd = ["tasklist", "/FI", "IMAGENAME eq RuneLite.exe"]
            res = subprocess.run(cmd, capture_output=True, text=True)
            return "RuneLite.exe" in res.stdout
        else:
            res = subprocess.run(["pgrep", "-f", "RuneLite"], capture_output=True)
            return res.returncode == 0
    except Exception:
        return False

def check_runelite_running_guard(no_guard: bool = False):
    """Prompts the user if RuneLite is running to ensure session data is flushed to disk before sync."""
    if no_guard:
        return
    if is_runelite_running():
        print("\n" + "=" * 76)
        print(" [GUARD] RuneLite is currently running!")
        print(" Please close RuneLite so your in-game session data is saved to disk.")
        print("=" * 76)
        try:
            input(" Press Enter once RuneLite has finished closing to proceed (or Ctrl+C to abort)... ")
        except (KeyboardInterrupt, EOFError):
            print("\n[ABORTED] Synchronization cancelled by user.")
            sys.exit(0)

        while is_runelite_running():
            print(" [GUARD] RuneLite is still closing... waiting 1 second.")
            time.sleep(1)
        print(" [GUARD] RuneLite closed. Proceeding with synchronization.\n")

# Pattern identifying Combat/PvM Activity Profiles
COMBAT_PROFILE_PATTERNS = ["Slayer", "Raids - ToA", "Raids - CoX", "Raids - ToB", "Bossing", "Wilderness", "Questing", "PvM"]

# Prefixes for plugins whose data should be ALWAYS 100% IDENTICAL & UP-TO-DATE across ALL profiles
UNIVERSAL_SYNC_PREFIXES = [
    "inventorysetups.",
    "banktags.",
    "dudewheresmystuff.",
    "richtextnotes.",
    "notes.",
    "customitemhovers.",
    "pvmTools.",
    "arberToolkitUi.",
    "cluescrolljuggling.",
    "tictac7x-charges.",
    "xpgoals_3."
]

def parse_properties(filepath: str) -> Dict[str, str]:
    """Parse a Java properties file into a key-value dictionary."""
    props = {}
    if not os.path.exists(filepath):
        return props
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' in line:
                k, v = line.split('=', 1)
                props[k.strip()] = v.strip()
    return props

def write_properties(filepath: str, props: Dict[str, str], header_comment: str = "RuneLite configuration synced by sync_base_profile.py"):
    """Write dictionary back to Java properties format."""
    lines = [f"# {header_comment}\n"]
    for k in sorted(props.keys()):
        lines.append(f"{k}={props[k]}\n")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(lines)

def ensure_local_sync_disabled():
    """Ensure sync: false is set on all profile entries in profiles.json to prevent cloud overwrites."""
    json_path = os.path.join(PROFILES_DIR, "profiles.json")
    if not os.path.exists(json_path):
        return
    try:
        with open(json_path, 'r') as f:
            data = json.load(f)
        modified = False
        for p in data.get("profiles", []):
            if p.get("sync") is not False:
                p["sync"] = False
                modified = True
        if modified:
            with open(json_path, 'w') as f:
                json.dump(data, f, indent=2)
            print("[CONFIG] Enforced sync=false in profiles.json to protect local files.")
    except Exception as e:
        print(f"[WARNING] Could not update profiles.json sync flag: {e}")

def collect_universal_data(profile_files: List[str]) -> Dict[str, str]:
    """
    Collect universal data (Inventory Setups, Bank Tags) from profile files.
    Files are ordered with newest edited activity profile FIRST so that whichever activity profile
    was edited most recently in RuneLite has its keys locked in FIRST.
    """
    universal_data = {}
    for pf in profile_files:
        path = os.path.join(PROFILES_DIR, pf)
        props = parse_properties(path)
        for k, v in props.items():
            if any(k.startswith(prefix) for prefix in UNIVERSAL_SYNC_PREFIXES):
                if k not in universal_data:
                    universal_data[k] = v
    return universal_data

HISTORY_FILE = os.path.join(PROFILES_DIR, "installed_plugins_history.json")

def get_external_plugins_set(props: Dict[str, str]) -> Set[str]:
    """Extract set of external plugin names from properties dict."""
    return set(p for p in props.get('runelite.externalPlugins', '').split(',') if p)

def update_plugins_history(all_active_plugins: Set[str]) -> Set[str]:
    """Update and return all historical external plugins."""
    history = set()
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r') as f:
                history = set(json.load(f).get('historical_plugins', []))
        except Exception:
            pass
    history.update(all_active_plugins)
    try:
        with open(HISTORY_FILE, 'w') as f:
            json.dump({'historical_plugins': sorted(list(history))}, f, indent=2)
    except Exception:
        pass
    return history

def purge_orphaned_config_keys(props: Dict[str, str], uninstalled_plugins: Set[str]) -> int:
    """Purge leftover configuration keys for plugins that are no longer installed anywhere."""
    if not uninstalled_plugins:
        return 0
    uninstalled_clean = set(re.sub(r'[^a-zA-Z0-9]', '', p).lower() for p in uninstalled_plugins)
    purged_count = 0
    for k in list(props.keys()):
        if k.startswith('runelite.') or k == 'runelite.externalPlugins':
            continue
        prefix = k.split('.', 1)[0] if '.' in k else k
        prefix_clean = re.sub(r'[^a-zA-Z0-9]', '', prefix).lower()
        if prefix_clean in uninstalled_clean or any(prefix_clean.startswith(uc) for uc in uninstalled_clean):
            del props[k]
            purged_count += 1
    return purged_count

def extract_pvm_configs(pvm_props: Dict[str, str], pvm_ext: Set[str]) -> Dict[str, str]:
    """Extract configuration keys and toggle states corresponding to pvm_ext plugins from the master PvM profile."""
    pvm_prefixes = [re.sub(r'[^a-zA-Z0-9]', '', p).lower() for p in pvm_ext]
    configs = {}
    for k, v in pvm_props.items():
        if k == 'runelite.externalPlugins':
            continue
        prefix = k.split('.', 1)[0] if '.' in k else k
        prefix_clean = re.sub(r'[^a-zA-Z0-9]', '', prefix).lower()
        if prefix_clean in pvm_prefixes or any(prefix_clean.startswith(p) for p in pvm_prefixes):
            configs[k] = v
        elif k.startswith('runelite.'):
            plugin_part = k.split('.', 1)[1]
            plugin_clean = re.sub(r'[^a-zA-Z0-9]', '', plugin_part).lower()
            if any(p in plugin_clean for p in pvm_prefixes):
                configs[k] = v
    return configs

def sync_rich_text_notes_folders(dry_run: bool = False):
    """Synchronize rich-text-notes directory folders across all profiles using the most recently modified profile folder as source."""
    rt_base_dir = os.path.expanduser("~/.runelite/rich-text-notes")
    if not os.path.exists(rt_base_dir):
        return

    json_path = os.path.join(PROFILES_DIR, "profiles.json")
    if not os.path.exists(json_path):
        return

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            p_data = json.load(f)
    except Exception:
        return

    profiles = p_data.get("profiles", [])
    if not profiles:
        return

    profile_folders = {}
    for p in profiles:
        pid = p.get("id")
        pname = p.get("name", "")
        folder_name = f"profile_{pid}_{pname.replace(' ', '_')}"
        profile_folders[folder_name] = pname

    def get_folder_latest_mtime(folder_path: str) -> float:
        latest = 0.0
        if not os.path.exists(folder_path):
            return latest
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.json') or file.endswith('.rtf'):
                    try:
                        mt = os.path.getmtime(os.path.join(root, file))
                        if mt > latest:
                            latest = mt
                    except Exception:
                        pass
        return latest

    source_folder = None
    latest_mtime = 0.0

    for folder_name in os.listdir(rt_base_dir):
        folder_path = os.path.join(rt_base_dir, folder_name)
        if os.path.isdir(folder_path) and folder_name in profile_folders:
            notes_dir = os.path.join(folder_path, "notes")
            if os.path.exists(notes_dir) and os.listdir(notes_dir):
                mtime = get_folder_latest_mtime(folder_path)
                if mtime > latest_mtime:
                    latest_mtime = mtime
                    source_folder = folder_name

    if not source_folder:
        return

    source_path = os.path.join(rt_base_dir, source_folder)
    source_notes_path = os.path.join(source_path, "notes")
    source_layout_path = os.path.join(source_path, "layout.json")

    source_notes = [f for f in os.listdir(source_notes_path) if f.endswith('.json') or f.endswith('.rtf')] if os.path.exists(source_notes_path) else []

    target_count = 0
    import shutil
    for folder_name in profile_folders.keys():
        if folder_name == source_folder:
            continue

        target_path = os.path.join(rt_base_dir, folder_name)
        target_notes_path = os.path.join(target_path, "notes")

        if not dry_run:
            os.makedirs(target_notes_path, exist_ok=True)

            if os.path.exists(source_layout_path):
                shutil.copy2(source_layout_path, os.path.join(target_path, "layout.json"))

            for note_file in source_notes:
                shutil.copy2(os.path.join(source_notes_path, note_file), os.path.join(target_notes_path, note_file))

            for existing_file in os.listdir(target_notes_path):
                if (existing_file.endswith('.json') or existing_file.endswith('.rtf')) and existing_file not in source_notes:
                    try:
                        os.remove(os.path.join(target_notes_path, existing_file))
                    except Exception:
                        pass

        target_count += 1

    source_display = profile_folders.get(source_folder, source_folder)
    note_docs_count = len([f for f in source_notes if f.endswith('.json')])
    print(f"\n[RICH-TEXT-NOTES] Synced {note_docs_count} notes & layout from {source_display} across {target_count} profile directories!")

def main():

    parser = argparse.ArgumentParser(description="Two-Tier Master Base QoL + PvM Combat Base + Universal Data Sync.")
    parser.add_argument("--base", default="default-0.properties", help="Tier 1 Master Base QoL profile (default: default-0.properties)")
    parser.add_argument("--pvm-base", default="PvM-10.properties", help="Tier 2 Master PvM Combat Base profile (default: PvM-10.properties)")
    parser.add_argument("--dry-run", action="store_true", help="Perform a dry run without modifying files.")
    parser.add_argument("--no-guard", action="store_true", help="Bypass interactive check prompting to close RuneLite.")
    args = parser.parse_args()

    # Pre-Flight Guard: Verify RuneLite is closed before reading/writing config
    check_runelite_running_guard(args.no_guard)

    base_path = os.path.join(PROFILES_DIR, args.base)
    pvm_base_path = os.path.join(PROFILES_DIR, args.pvm_base)

    if not os.path.exists(base_path):
        print(f"[ERROR] Base profile not found at: {base_path}")
        sys.exit(1)

    print(f"=== RuneLite Two-Tier Master Base & Universal Data Sync ===")
    print(f"Tier 1 Master Base QoL:      {base_path}")
    print(f"Tier 2 Master PvM Combat Base: {pvm_base_path}")
    if args.dry_run:
        print("[MODE] DRY RUN ONLY - No files will be modified.\n")

    # Enforce local sync mode (sync=false)
    ensure_local_sync_disabled()

    # Gather all profile files
    all_files = [f for f in os.listdir(PROFILES_DIR) if f.endswith('.properties') and not f.startswith('.')]
    activity_files = [f for f in all_files if not f.startswith("$rsprofile")]

    # Sort activity profiles strictly by nanosecond modification timestamp DESCENDING (newest modified first)
    activity_files_sorted = sorted(activity_files, key=lambda f: os.stat(os.path.join(PROFILES_DIR, f)).st_mtime_ns, reverse=True)
    final_file_order = activity_files_sorted + [f for f in all_files if f not in activity_files_sorted]

    print("Profile priority order (newest activity profile on disk FIRST):")
    for f in final_file_order[:3]:
        mtime_ns = os.stat(os.path.join(PROFILES_DIR, f)).st_mtime_ns
        print(f"  - {f} (st_mtime_ns={mtime_ns})")
    print()

    # Collect universal data (Inventory Setups, Bank Tags)
    universal_data = collect_universal_data(final_file_order)
    print(f"Collected {len(universal_data)} Universal Data keys (Inventory Setups / Bank Tags / Notes).\n")

    # Parse properties for all files
    props_map = {f: parse_properties(os.path.join(PROFILES_DIR, f)) for f in all_files}
    plugins_map = {f: get_external_plugins_set(props_map[f]) for f in all_files}

    # Tier 1 Master Base Plugins
    base_ext = plugins_map.get(args.base, set())

    # Tier 2 Master PvM Combat Plugins (dynamically discovered from PvM-10.properties)
    pvm_master_ext = plugins_map.get(args.pvm_base, set())
    pvm_ext = pvm_master_ext - base_ext

    # Extract PvM configurations from PvM master profile
    if args.pvm_base in props_map:
        pvm_configs = extract_pvm_configs(props_map[args.pvm_base], pvm_ext)
    else:
        pvm_configs = {}

    # All active external plugins across all files on disk
    all_active_external_plugins = base_ext | pvm_ext | set().union(*[plugins_map[f] for f in all_files if not f.startswith("$")])
    historical_plugins = update_plugins_history(all_active_external_plugins)
    uninstalled_plugins = historical_plugins - all_active_external_plugins

    print(f"Base plugins in default-0:            {len(base_ext)}")
    print(f"Shared PvM plugins in PvM-10:         {len(pvm_ext)} ({', '.join(sorted(list(pvm_ext)))})")
    print(f"Uninstalled external plugins detected: {len(uninstalled_plugins)}\n")

    for pf in sorted(all_files):
        target_path = os.path.join(PROFILES_DIR, pf)
        target_props = props_map[pf]
        target_filename = pf
        target_ext = plugins_map[pf]

        is_combat = any(pattern in pf for pattern in COMBAT_PROFILE_PATTERNS)
        is_base = pf.startswith("default-0")
        is_pvm_master = (pf == args.pvm_base)

        if is_base:
            updated_ext = base_ext
        elif is_pvm_master:
            # Pure PvM profile: strictly shared combat plugins only
            updated_ext = pvm_ext
        else:
            # Exclusives are dynamically computed from disk
            exclusives = target_ext - base_ext - pvm_ext
            updated_ext = base_ext | (pvm_ext if is_combat else set()) | exclusives

        added_to_target = updated_ext - target_ext
        pruned_plugins = target_ext - updated_ext

        target_props['runelite.externalPlugins'] = ','.join(sorted(list(updated_ext)))

        # 3. Built-in Plugin States Merge from Base
        base_props = props_map[args.base]
        builtin_synced = 0
        if not is_pvm_master:
            for k, v in base_props.items():
                if k.startswith('runelite.') and k.endswith('plugin') and k != 'runelite.externalPlugins':
                    if target_props.get(k) != v:
                        target_props[k] = v
                        builtin_synced += 1

        # 4. Universal Data Sync (Always synced across ALL profiles)
        univ_synced = 0
        for k, v in universal_data.items():
            if target_props.get(k) != v:
                target_props[k] = v
                univ_synced += 1

        # 5. Global Settings & Plugin Configurations Overwrite Sync from Base
        settings_synced = 0
        if not is_pvm_master:
            pvm_prefixes = [re.sub(r'[^a-zA-Z0-9]', '', p).lower() for p in pvm_ext]
            for k, v in base_props.items():
                if (k.startswith('runelite.') or '.' in k) and not any(k.startswith(prefix) for prefix in UNIVERSAL_SYNC_PREFIXES) and k != 'runelite.externalPlugins':
                    prefix = k.split('.', 1)[0] if '.' in k else k
                    prefix_clean = re.sub(r'[^a-zA-Z0-9]', '', prefix).lower()
                    if prefix_clean in pvm_prefixes or any(prefix_clean.startswith(p) for p in pvm_prefixes):
                        continue
                    if k.startswith('runelite.'):
                        plugin_part = k.split('.', 1)[1]
                        plugin_clean = re.sub(r'[^a-zA-Z0-9]', '', plugin_part).lower()
                        if any(p in plugin_clean for p in pvm_prefixes):
                            continue

                    if target_props.get(k) != v:
                        target_props[k] = v
                        settings_synced += 1

        # 6. Shared PvM Group Configs Merge (for Combat profiles only)
        pvm_synced = 0
        if is_combat and pvm_configs:
            for k, v in pvm_configs.items():
                if target_props.get(k) != v:
                    target_props[k] = v
                    pvm_synced += 1

        # 7. Purge Orphaned Config Keys for Uninstalled External Plugins
        purged_keys_count = purge_orphaned_config_keys(target_props, uninstalled_plugins)

        # Write properties to disk
        if not args.dry_run:
            write_properties(target_path, target_props, f"Synced by sync_base_profile.py")

        print(f"[SYNC] -> {target_filename}:")
        if added_to_target:
            print(f"       + Added Plugins: {len(added_to_target)} ({', '.join(sorted(list(added_to_target)))})")
        elif pruned_plugins:
            print(f"       - Pruned Plugins: {len(pruned_plugins)} ({', '.join(sorted(list(pruned_plugins)))})")
        else:
            print(f"       + Plugins up to date")
        if purged_keys_count > 0:
            print(f"       - Purged Orphaned Config Keys (Uninstalled Plugins): {purged_keys_count}")
        print(f"       + Universal Data Keys Synced (Inventory Setups / Bank Tags): {univ_synced}")
        print(f"       + Base settings merged: {settings_synced}")
        if is_combat:
            print(f"       + PvM settings merged: {pvm_synced}")

    # 8. Synchronize Rich Text Notes folders across all profile directories
    sync_rich_text_notes_folders(args.dry_run)

    print("\n[SUCCESS] Two-Tier Master Base, PvM Group, and Universal Data sync completed!")

if __name__ == "__main__":
    main()
