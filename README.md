# RuneLite Clan Profiles & QoL Setup Guide

Welcome to the clan RuneLite configuration repository! This repository contains synchronized activity profiles (`Bossing`, `Raids`, `Slayer`, `Wilderness`, `Skilling & Minigames`, `Questing`, `PvM`), master base settings (`default-0.properties`), and automated import, export, and sync tools (`import_profiles.py`, `export_profiles.py`, `sync_base_profile.py`).

---

## 🚀 1-Click Automated Import (Recommended)

Importing these profiles takes less than 10 seconds. The automated import script automatically creates a **pre-import timestamped backup** of your existing profiles and **preserves all of your personal Inventory Setups, Bank Tags, Tile Markers, and Notes**:

1. Open your terminal or command prompt in this repository folder.
2. Run the import script:
   ```bash
   python3 import_profiles.py
   ```
3. Restart RuneLite and switch profiles using the **Profiles** plugin icon on the right sidebar!

--- 

## 🛡️ Personal Data Protection & Safety Features

When you run `import_profiles.py`, your personal setup is 100% safe:
- **🔒 Timestamped Pre-Import Backup**: Before any files are touched, your entire current profile directory is backed up to `~/.runelite/profiles2_backup_YYYYMMDD_HHMMSS/`.
- **🎒 Inventory Setups Preserved**: Custom gear and inventory loadouts (`inventorysetups.`) are extracted and merged into every imported profile.
- **🏷️ Bank Tags & Layouts Preserved**: Custom bank tags, tab icons, and custom grid layouts (`banktags.`) are preserved.
- **📍 Tile & Object Markers Preserved**: Marked ground tiles (`groundMarker.`) and highlighted objects (`objectindicators.`) are preserved.
- **📝 Personal Notes & Item Tags Preserved**: Notepad entries (`notes.`, `richtextnotes.`) and item outline colors (`inventorytags.`) are preserved.

---

## 🏗️ Architecture & How Profile Syncing Works

This suite uses an automated **Two-Tier Master Profile System** managed by `sync_base_profile.py`:

- **Tier 1: Master Base QoL (`default-0.properties`)**:
  - Universal QoL settings (117 HD tuning, `lite-regen-meter` status bars, `player-outline` transparency, `grounditems` loot beams, `questhelper`) + daily/traversal tools (Sailing, Farm run checkers, Birdhouse timers, Alching, Cooking prep).
  - **Synced to ALL 10 activity profiles** so you never lose basic UI or daily utilities.

- **Tier 2: Master PvM Combat Base (`PvM-10.properties`)**:
  - Shared combat helpers (`thrall-helper`, `autocast-utilities`, `consumable-cooldowns`, `max-hit-calculator`, `prayer-regeneration-helper`, `arceuus-timers`, `monster-hp-percentage`, `combat-achievements-tracker`).
  - **Synced ONLY to Combat Profiles** (`Bossing`, `Slayer`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`, `PvM`).
  - Non-combat profiles (`Skilling & Minigames`, `Questing`) remain clean and free of heavy combat overlays.

- **Universal Data Sync (Newest Profile Priority)**:
  - Inventory Setups (`inventorysetups.`) and Bank Tags (`banktags.`) are automatically synced across all profiles. Whichever profile you edited most recently in RuneLite takes priority, ensuring your latest setups never get overwritten.

- **Automated Orphaned Config Cleanup**:
  - Leftover configuration keys for uninstalled plugins are automatically purged across all profiles.

---

## What's Included

- **`import_profiles.py`**: Automated 1-click import script with timestamped backups and personal user data protection.
- **`profiles/`**: Ready-to-import `.properties` files tuned for optimal Old School RuneScape performance, visual clarity, and combat responsiveness.
- **`sync_base_profile.py`**: Profile synchronization script that enforces Two-Tier Master Base + PvM Combat Base syncing and Universal Data propagation.
- **`export_profiles.py`**: Automated export and sanitization tool that refreshes clean profile files, sorts properties A-to-Z to prevent Git diff churn, and updates [`AUDIT_REPORT.md`](AUDIT_REPORT.md).
- **`AUDIT_REPORT.md`**: Comprehensive breakdown of top QoL plugin recommendations, 117 HD settings, ground items filters, anti-drag tuning, and POH swaps.

---

## 🎯 Profile Breakdown & Plugin Categories

| Profile | Category & Purpose | Key Plugin Examples |
| :--- | :--- | :--- |
| **`default`** *(Base QoL)* | **Tier 1 Master Base Profile**: Contains core visual clarity, 117 HD tuning, status bars, true tile, ground item loot beams, and daily/traversal tools (Sailing, Farm run checkers, Birdhouse timers, Alching, Cooking prep). Synced to ALL profiles. | `117hd`, `lite-regen-meter`, `grounditems`, `player-outline`, `sailing`, `birdhouse-overlay`, `abc-alch` |
| **`PvM`** | **Tier 2 Master PvM Combat Profile**: Base QoL + Shared Combat Helpers (Thrall Helper, Autocast Utilities, Consumable Cooldowns, Prayer Regen, Max Hit Calculator). Synced to ALL Combat profiles. | `thrall-helper`, `autocast-utilities`, `consumable-cooldowns`, `max-hit-calculator`, `prayer-regeneration-helper` |
| **`Slayer`** | **Slayer & Task Training**: Base QoL + Shared Combat Helpers + Slayer task boosting & task sorters. | `slayer-task-sorter`, `mortimer-calculator`, `thrall-helper`, `autocast-utilities` |
| **`Bossing`** | **Boss Encounters**: Base QoL + Shared Combat Helpers + Boss fight mechanics & room overlays. | `zulrah-helper`, `hunllef-helper`, `the-gauntlet`, `vorkath-run-warning`, `barrows-door-highlighter` |
| **`Raids (ToA / CoX / ToB)`** | **End-Game Raiding**: Base QoL + Shared Combat Helpers + Raid puzzle solvers, points counters, and team gear checkers. | `tombs-of-amascut`, `toa-points-tracker`, `cox-additions`, `cox-qol`, `tobqol`, `nyloer` |
| **`Skilling & Minigames`** | **Skilling & Minigame Efficiency**: Base QoL + 62 dedicated skill training & minigame helpers. No combat overlays. | `guardians-of-the-rift-helper`, `tempoross`, `wintertodt-solo-helper`, `mahogany-homes`, `easy-giantsfoundry`, `easy-empty` |
| **`Wilderness`** | **PvP & Wilderness Survival**: Base QoL + Shared Combat Helpers + Wilderness danger alerts & depth boundaries. | `wilderness-player-alarm`, `wilderness-multi-lines`, `protect-item-notifier`, `looting-bag-value`, `rogues-chest` |
| **`Questing`** | **Questing & Quest Helper**: Base QoL + Quest Helper steps, dialogue skips, puzzle solvers, and quest item highlight overlays. No combat overlays. | `quest-helper`, `shortest-path`, `emote-clue-items`, `clue-teleport-helper` |

---

## 🛠️ Manual Import Instructions (Alternative)

If you prefer to copy files manually without running Python:
1. Close RuneLite completely.
2. Open your RuneLite profiles folder (`%USERPROFILE%\.runelite\profiles2` on Windows or `~/.runelite/profiles2` on Mac).
3. Copy all `.properties` files from this repo's `profiles/` folder into your open `profiles2` folder.
4. Launch RuneLite and switch profiles.

---

## ⚙️ Automated Privacy Sanitization Engine
When exported via `export_profiles.py`, sensitive personal data is automatically stripped from all profile files (Discord webhooks, login salts, account IDs, friend tracking, friend notes, party IDs, Wise Old Man clan tokens, and clan chat history).

---

## 📖 Selective QoL Plugin Guide
If you only want specific plugin improvements rather than importing entire profiles, read [`AUDIT_REPORT.md`](AUDIT_REPORT.md) for a detailed list of all external plugins and performance recommendations.
