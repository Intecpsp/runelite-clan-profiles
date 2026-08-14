# RuneLite Clan Profiles & QoL Setup Guide

Welcome to the clan RuneLite configuration repository! This repository contains synchronized activity profiles (`Bossing`, `Raids`, `Slayer`, `Wilderness`, `Skilling`), master base settings (`default-0.properties`), and the automated synchronization tool (`sync_base_profile.py`).

---

## What's Included

- **`profiles/`**: Ready-to-import `.properties` files tuned for optimal Old School RuneScape performance, visual clarity, and combat responsiveness.
- **`sync_base_profile.py`**: Profile synchronization script that ensures shared PvM combat plugins (Thrall Helper, Autocast Utilities, Consumable Cooldowns, etc.) and Universal Data (Inventory Setups, Bank Tags) stay in sync across your activity profiles.
- **`export_profiles.py`**: Helper script to quickly refresh the clean `.properties` files in this repository whenever you update your settings in RuneLite.
- **`AUDIT_REPORT.md`**: Comprehensive breakdown of top QoL plugin recommendations, 117 HD settings, ground items filters, anti-drag tuning, and POH swaps.

---

## 🎯 Profile Breakdown & Plugin Categories

This suite uses a modular profile architecture. Master base settings are synced to all profiles, while heavy or activity-specific plugins are isolated to prevent screen clutter and lag:

| Profile | Category & Purpose | Key Plugin Examples |
| :--- | :--- | :--- |
| **`default`** *(Base QoL)* | **Universal Base Profile**: Contains core visual clarity, 117 HD tuning, status bars, true tile, ground item loot beams, and daily/traversal tools (Sailing, Farm run checkers, Birdhouse timers, Alching, Cooking prep). Synced to ALL profiles. | `117hd`, `lite-regen-meter`, `grounditems`, `player-outline`, `sailing`, `birdhouse-overlay`, `abc-alch` |
| **`Slayer`** | **Slayer & Task Training**: Base QoL + 37 Shared Combat Helpers + Slayer task boosting & task sorters. | `slayer-boosting`, `slayer-task-sorter`, `thrall-helper`, `autocast-utilities` |
| **`Bossing`** | **Boss Encounters**: Base QoL + 37 Shared Combat Helpers + Boss fight mechanics & room overlays. | `zulrah-helper`, `hunllef-helper`, `the-gauntlet`, `vorkath-run-warning`, `barrows-door-highlighter` |
| **`Raids (ToA / CoX / ToB)`** | **End-Game Raiding**: Base QoL + 37 Shared Combat Helpers + Raid puzzle solvers, points counters, and team gear checkers. | `tombs-of-amascut`, `toa-points-tracker`, `cox-additions`, `cox-qol`, `tobqol`, `nyloer` |
| **`Skilling & Minigames`** | **Skilling & Minigame Efficiency**: Base QoL + 62 dedicated skill training & minigame helpers. | `guardians-of-the-rift-helper`, `tempoross`, `wintertodt-solo-helper`, `mahogany-homes`, `easy-giantsfoundry`, `easy-empty` |
| **`Wilderness`** | **PvP & Wilderness Survival**: Base QoL + 37 Shared Combat Helpers + 12 Wilderness danger alerts & depth boundaries. | `wilderness-player-alarm`, `wilderness-multi-lines`, `protect-item-notifier`, `looting-bag-value`, `rogues-chest` |

---

## 🚀 Beginner Quick-Start: How to Import Profiles into RuneLite

Importing these profiles takes less than 2 minutes. Follow the step-by-step instructions below for your operating system:

### Step 1: Close RuneLite Completely
Make sure your RuneLite client is closed before copying files.

### Step 2: Open Your RuneLite Profiles Folder

#### 💻 On Windows:
1. Press `Win + R` on your keyboard to open the **Run** dialog box.
2. Copy and paste the following path and press **Enter**:
   ```text
   %USERPROFILE%\.runelite\profiles2
   ```

#### 🍎 On Mac:
1. Open **Finder**.
2. Press `Cmd + Shift + G` on your keyboard to open **Go to Folder**.
3. Copy and paste the following path and press **Enter**:
   ```text
   ~/.runelite/profiles2
   ```

### Step 3: Copy Profile Files
Copy all `.properties` files from this repo's `profiles/` folder into your open `profiles2` folder.

### Step 4: Open RuneLite & Switch Profiles
1. Launch RuneLite.
2. In the right-hand sidebar, open the **Profiles** plugin icon.
3. Select the profile for your current activity (`Bossing`, `Raids - ToA`, `Slayer`, `Skilling & Minigames`, etc.)!

---

## ⚙️ Optional Personal Customizations

After importing, here are quick optional settings you can personalize in RuneLite:

1. **Discord Webhooks (`Dink`, `Discord Collection Logger`, `OSRS-TCG`)**:
   - All active Discord Webhook URLs across all notification plugins are sanitized to `https://discord.com/api/webhooks/YOUR_WEBHOOK_HERE` for privacy.
   - If you want loot drops, level ups, collection logs, or trade pull notifications sent to your personal Discord server or clan channel, open the plugin settings in RuneLite for **Dink**, **Discord Collection Logger**, or **OSRS-TCG** and paste your Discord channel webhook URL.

2. **Character Model Visibility (`Entity Hider` vs `Player Outline`)**:
   - Character model transparency (`Hide Local Player`) is enabled by default alongside **Player Outline** so you can see ground markers beneath your feet.
   - If you prefer to see your normal 3D character model, open **Entity Hider** settings and uncheck `Hide Local Player`.

3. **Camera Controls (`Key Remapping`)**:
   - Camera movement is set to `WASD` keys. If you prefer classic arrow keys for camera rotation, open **Key Remapping** settings.

---

## 📖 Selective QoL Plugin Guide
If you only want specific plugin improvements rather than importing entire profiles, read [`AUDIT_REPORT.md`](AUDIT_REPORT.md) for a detailed list of all external plugins and performance recommendations.
