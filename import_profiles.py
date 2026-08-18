#!/usr/bin/env python3
"""
RuneLite Clan Profile Importer & Personal Data Protector

This script safely imports the clan's optimized RuneLite profiles into your local
RuneLite profiles directory (~/.runelite/profiles2 or %USERPROFILE%\\.runelite\\profiles2).

Safety Features:
1. Automated Pre-Import Backup: Creates a timestamped backup directory in ~/.runelite/
   before making any modifications (e.g., profiles2_backup_YYYYMMDD_HHMMSS).
2. Personal Data Protection: Automatically extracts and preserves all of your existing
   Inventory Setups, Bank Tags, Bank Tag Layouts, Ground Tile Markers, Object Highlights,
   Inventory Tags, and Personal Notes, merging them seamlessly into every imported clan profile.
3. Sync Script Installation: Copies sync_base_profile.py to your ~/.runelite/ directory.
"""
import os
import sys
import shutil
import datetime
import argparse
import re
from typing import Dict, Set, List

def get_profiles_dir() -> str:
    if sys.platform.startswith("win"):
        user_profile = os.environ.get("USERPROFILE", os.path.expanduser("~"))
        return os.path.join(user_profile, ".runelite", "profiles2")
    else:
        return os.path.expanduser("~/.runelite/profiles2")

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
PROFILES_SOURCE = os.path.join(REPO_DIR, "profiles")
SYNC_SCRIPT_SOURCE = os.path.join(REPO_DIR, "sync_base_profile.py")

UNIVERSAL_USER_PREFIXES = [
    "inventorysetups.",
    "banktags.",
    "groundMarker.",
    "objectindicators.",
    "inventorytags.",
    "notes.",
    "notesplugin.",
    "richtextnotes."
]

def parse_properties(filepath: str) -> Dict[str, str]:
    props = {}
    if not os.path.exists(filepath):
        return props
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line_str = line.strip()
            if line_str and not line_str.startswith("#") and "=" in line_str:
                k, v = line_str.split("=", 1)
                props[k.strip()] = v.strip()
    return props

def write_properties(filepath: str, props: Dict[str, str]):
    sorted_keys = sorted(props.keys(), key=lambda k: k.lower())
    with open(filepath, "w", encoding="utf-8") as f:
        for k in sorted_keys:
            f.write(f"{k}={props[k]}\n")

def main():
    parser = argparse.ArgumentParser(description="Import RuneLite Clan Profiles while preserving personal Inventory Setups, Bank Tags, and Tile Markers.")
    parser.add_argument("--dry-run", action="store_true", help="Perform a dry run without modifying any files.")
    args = parser.parse_args()

    profiles_target = get_profiles_dir()
    runelite_dir = os.path.dirname(profiles_target)

    print("=== RuneLite Clan Profile Importer & Personal Data Protection ===")
    print(f"Source Repository Profiles: {PROFILES_SOURCE}")
    print(f"Target RuneLite Directory:  {profiles_target}\n")

    if not os.path.exists(PROFILES_SOURCE):
        print(f"[ERROR] Source profiles directory not found at: {PROFILES_SOURCE}")
        sys.exit(1)

    if os.path.exists(profiles_target):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = os.path.join(runelite_dir, f"profiles2_backup_{timestamp}")
        print(f"[BACKUP] Creating timestamped pre-import backup at:\n         {backup_dir}")
        if not args.dry_run:
            shutil.copytree(profiles_target, backup_dir)
        print("         Backup completed successfully.\n")
    else:
        print("[NOTICE] No existing profiles2 directory found; creating a fresh profile setup.\n")
        if not args.dry_run:
            os.makedirs(profiles_target, exist_ok=True)

    user_data = {}
    if os.path.exists(profiles_target):
        existing_files = [f for f in os.listdir(profiles_target) if f.endswith(".properties") and not f.startswith(".")]
        print(f"[DATA PROTECTION] Scanning {len(existing_files)} existing profile files for personal user data...")
        for ef in existing_files:
            ef_path = os.path.join(profiles_target, ef)
            props = parse_properties(ef_path)
            for k, v in props.items():
                if any(k.startswith(prefix) for prefix in UNIVERSAL_USER_PREFIXES):
                    if k not in user_data:
                        user_data[k] = v

    print(f"[DATA PROTECTION] Extracted {len(user_data)} personal user keys to preserve:")
    inv_count = sum(1 for k in user_data if k.startswith("inventorysetups."))
    bank_count = sum(1 for k in user_data if k.startswith("banktags."))
    tile_count = sum(1 for k in user_data if k.startswith("groundMarker.") or k.startswith("objectindicators."))
    other_count = len(user_data) - inv_count - bank_count - tile_count
    print(f"                  - Inventory Setups : {inv_count} keys")
    print(f"                  - Bank Tags/Layouts: {bank_count} keys")
    print(f"                  - Ground/Object Tiles: {tile_count} keys")
    print(f"                  - Notes & Item Tags : {other_count} keys\n")

    source_files = [f for f in os.listdir(PROFILES_SOURCE) if f.endswith(".properties") and not f.startswith(".")]
    print(f"[IMPORT] Copying and merging {len(source_files)} clan profile files into RuneLite...")

    for sf in sorted(source_files):
        src_path = os.path.join(PROFILES_SOURCE, sf)
        dst_path = os.path.join(profiles_target, sf)

        clan_props = parse_properties(src_path)

        merged_count = 0
        for k, v in user_data.items():
            if clan_props.get(k) != v:
                clan_props[k] = v
                merged_count += 1

        if not args.dry_run:
            write_properties(dst_path, clan_props)
        print(f"  [OK] Imported {sf:35s} (Merged {merged_count} personal data keys)")

    if os.path.exists(SYNC_SCRIPT_SOURCE):
        sync_target = os.path.join(runelite_dir, "sync_base_profile.py")
        print(f"\n[SYNC TOOL] Copying sync_base_profile.py to:\n            {sync_target}")
        if not args.dry_run:
            shutil.copy2(SYNC_SCRIPT_SOURCE, sync_target)
            try:
                os.chmod(sync_target, 0o755)
            except Exception:
                pass

    print("\n🎉 [SUCCESS] RuneLite Clan Profiles imported successfully!")
    print("   - All existing Inventory Setups, Bank Tags, and Tile Markers were preserved.")
    print("   - Launch or restart RuneLite to utilize your new clan profiles!")

if __name__ == "__main__":
    main()
