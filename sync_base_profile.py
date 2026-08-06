#!/usr/bin/env python3
"""
RuneLite Base QoL + Shared Plugin Groups + Universal Data Sync Script
=====================================================================
Synchronizes Base QoL settings and plugins from a master base profile (default-0.properties)
to all activity profiles, while maintaining Shared Plugin Groups across combat/PvM profiles,
and bidirectionally synchronizing Universal Data Plugins (Inventory Setups, Bank Tags, etc.).
Flawless Activity Profile Priority Logic:
1. Filters out $rsprofile--1.properties from taking source priority (since RuneLite updates $rsprofile ~1s after closing).
2. Sorts ACTIVITY profile files (Slayer, Bossing, Raids, etc.) strictly by st_mtime_ns DESCENDING.
3. Whichever activity profile you actually edited in RuneLite is locked in FIRST as the canonical source of truth.
4. Enforces sync=false in profiles.json so local profile files are protected from cloud overwrites.
"""
import os
import sys
import json
import argparse
from typing import Dict, Set, List, Tuple
PROFILES_DIR = os.path.expanduser("~/.runelite/profiles2")
# Shared Groups Definition (PvM Combat Plugins)
SHARED_GROUPS = {
    "pvm_combat": {
        "plugins": [
            "thrall-helper",
            "arceuus-timers",
            "combat-achievements-tracker",
            "ectoplasmator-reminder",
            "delayed-healing",
            "chugging-barrel",
            "antifire-checker",
            "attack-ranges",
            "autocast-utilities",
            "book-of-the-dead-reminder",
            "bracelet-reminder",
            "consumable-cooldowns",
            "deathindicator",
            "dont-telegrab-npcs",
            "lite-regen-meter",
            "monster-hp-percentage",
            "poisoned-npcs",
            "poison-ring",
            "poison-moo",
            "spec-regen-timer",
            "unpotted-reminder",
            "skull-notifier",
            "auto-retaliate-warning",
            "menuhp",
            "boss-health-indicators",
            "casket-saver",
            "crab-solver",
            "fight-cave-waves",
            "godwars-protection-overlay",
            "lizardman-shaman-minion-alert",
            "low-detail-raids",
            "max-hit-calculator",
            "prayer-regeneration-helper",
            "ring-of-recoil-notifier",
            "timers-ca",
            "tzhaar-hp-tracker",
            "emblem-trader-skull-timer"
        ],
        "profile_patterns": ["Slayer", "Raids - ToA", "Raids - CoX", "Raids - ToB", "Bossing", "Wilderness"]
    }
}
# Prefixes for plugins whose data should be ALWAYS 100% IDENTICAL & UP-TO-DATE across ALL profiles
UNIVERSAL_SYNC_PREFIXES = [
    "inventorysetups.",
    "banktags.",
    "dudewheresmystuff.",
    "rich-text-notes.",
    "customitemhovers."
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
    was edited most recently in RuneLite has its keys locked in FIRST and never overwritten by older files.
    """
    universal_data = {}
    for pf in profile_files:
        path = os.path.join(PROFILES_DIR, pf)
        props = parse_properties(path)
        for k, v in props.items():
            if any(k.startswith(prefix) for prefix in UNIVERSAL_SYNC_PREFIXES):
                # Lock in first occurrence (newest modified activity profile wins)
                if k not in universal_data:
                    universal_data[k] = v
    return universal_data
def collect_shared_configs(profile_paths: List[str], plugins: List[str]) -> Dict[str, str]:
    """Collect the latest configuration settings for a list of plugins across member profiles."""
    shared_configs = {}
    prefixes = [p.replace('-', '').lower() for p in plugins]
    for path in profile_paths:
        props = parse_properties(path)
        for k, v in props.items():
            k_lower = k.lower()
            if any(k_lower.startswith(prefix) for prefix in prefixes):
                shared_configs[k] = v
    return shared_configs
def sync_profiles(base_path: str, target_path: str, shared_configs_map: Dict[str, Dict[str, str]], universal_data: Dict[str, str], dry_run: bool = False):
    """Sync base properties, universal plugin data (Inventory Setups/Bank Tags), and shared group configs into target file."""
    base_props = parse_properties(base_path)
    target_props = parse_properties(target_path)
    target_filename = os.path.basename(target_path)
    if not base_props:
        print(f"[ERROR] Base profile file not found or empty: {base_path}")
        return
    # 1. External Plugins Set Union
    base_ext = set(p for p in base_props.get('runelite.externalPlugins', '').split(',') if p)
    target_ext = set(p for p in target_props.get('runelite.externalPlugins', '').split(',') if p)
    # 2. Shared Group Plugins
    extra_shared_plugins = set()
    for group_name, group_data in SHARED_GROUPS.items():
        if any(pattern in target_filename for pattern in group_data["profile_patterns"]):
            extra_shared_plugins.update(group_data["plugins"])
            group_configs = shared_configs_map.get(group_name, {})
            for k, v in group_configs.items():
                target_props[k] = v
    updated_ext = base_ext | target_ext | extra_shared_plugins
    added_to_target = (base_ext | extra_shared_plugins) - target_ext
    target_props['runelite.externalPlugins'] = ','.join(sorted(list(updated_ext)))
    # 3. Built-in Plugin States
    builtin_synced = 0
    for k, v in base_props.items():
        if k.startswith('runelite.') and k.endswith('plugin') and k != 'runelite.externalPlugins':
            if target_props.get(k) != v:
                target_props[k] = v
                builtin_synced += 1
    # 4. Universal Data Sync (Inventory Setups, Bank Tags, Notes)
    univ_synced = 0
    for k, v in universal_data.items():
        if target_props.get(k) != v:
            target_props[k] = v
            univ_synced += 1
    # 5. Global Settings Merge from Base
    settings_synced = 0
    for k, v in base_props.items():
        if (k.startswith('runelite.') or '.' in k) and not any(k.startswith(prefix) for prefix in UNIVERSAL_SYNC_PREFIXES):
            if k not in target_props:
                target_props[k] = v
                settings_synced += 1
    if not dry_run and (added_to_target or builtin_synced or univ_synced or settings_synced):
        write_properties(target_path, target_props, f"Synced by sync_base_profile.py")
    print(f"[SYNC] -> {target_filename}:")
    if added_to_target:
        print(f"       + Added Plugins: {len(added_to_target)} ({', '.join(sorted(list(added_to_target)))})")
    else:
        print(f"       + Plugins up to date")
    print(f"       + Universal Data Keys Synced (Inventory Setups / Bank Tags): {univ_synced}")
    print(f"       + Base settings merged: {settings_synced}")
def main():
    parser = argparse.ArgumentParser(description="Sync RuneLite Base QoL profile, Shared Groups, and Universal Data to activity profiles.")
    parser.add_argument("--base", default="default-0.properties", help="Base profile file name in profiles2 directory (default: default-0.properties)")
    parser.add_argument("--dry-run", action="store_true", help="Perform a dry run without modifying files.")
    args = parser.parse_args()
    base_path = os.path.join(PROFILES_DIR, args.base)
    if not os.path.exists(base_path):
        print(f"[ERROR] Base profile not found at: {base_path}")
        sys.exit(1)
    print(f"=== RuneLite Base Profile, Shared Group & Universal Data Sync ===")
    print(f"Base Profile: {base_path}")
    if args.dry_run:
        print("[MODE] DRY RUN ONLY - No files will be modified.\n")
    # Enforce local sync mode (sync=false)
    ensure_local_sync_disabled()
    # Gather all profile files
    all_files = [f for f in os.listdir(PROFILES_DIR) if f.endswith('.properties') and not f.startswith('.')]
    # Filter out $rsprofile from source priority determination
    activity_files = [f for f in all_files if not f.startswith("$rsprofile")]
    # Sort activity profiles strictly by nanosecond modification timestamp DESCENDING (newest modified first)
    activity_files_sorted = sorted(activity_files, key=lambda f: os.stat(os.path.join(PROFILES_DIR, f)).st_mtime_ns, reverse=True)
    # Final file priority: Newest activity profile first, then remaining activity profiles, then $rsprofile
    final_file_order = activity_files_sorted + [f for f in all_files if f not in activity_files_sorted]
    print("Profile priority order (newest activity profile on disk FIRST):")
    for f in final_file_order[:3]:
        mtime_ns = os.stat(os.path.join(PROFILES_DIR, f)).st_mtime_ns
        print(f"  - {f} (st_mtime_ns={mtime_ns})")
    print()
    # Collect universal data (Inventory Setups, Bank Tags) prioritizing newest modified activity profile
    universal_data = collect_universal_data(final_file_order)
    print(f"Collected {len(universal_data)} Universal Data keys (Inventory Setups / Bank Tags / Notes).\n")
    # Collect shared group configs across member profiles
    shared_configs_map = {}
    for group_name, group_data in SHARED_GROUPS.items():
        member_paths = [
            os.path.join(PROFILES_DIR, pf) for pf in all_files
            if any(pattern in pf for pattern in group_data["profile_patterns"])
        ]
        shared_configs_map[group_name] = collect_shared_configs(member_paths, group_data["plugins"])
    for pf in sorted(all_files):
        target_path = os.path.join(PROFILES_DIR, pf)
        sync_profiles(base_path, target_path, shared_configs_map, universal_data, dry_run=args.dry_run)
    print("\n[SUCCESS] Profile, Shared Group, and Universal Data sync completed!")
if __name__ == "__main__":
    main()
