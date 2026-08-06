# Comprehensive RuneLite Profile & Plugin Audit Report (Standardized Source of Truth)

This document is the **standardized source of truth** for all **295 unique external plugins** installed across your **8 active RuneLite profiles** (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`). Every single plugin entry has the exact same 4 metadata fields: **Active Profiles**, **GitHub Repository**, **Last Updated on GitHub**, and **Function Summary**.

## 📊 Active Profile Suite Summary

| Profile Name | Filename | External Plugins Count | Scope & Purpose |
| :--- | :--- | :---: | :--- |
| **`default`** | `default-0.properties` | **164** | **Master Base QoL Profile:** Contains all 164 universal QoL, Sailing, open-world traversal, bank/inventory tools, and clue solvers. Synced to ALL profiles. |
| **`Slayer`** | `Slayer-1.properties` | **202** | **Slayer & Combat Tasks:** Base QoL + 38 Shared PvM Combat plugins + `slayer-boosting`. |
| **`Bossing`** | `Bossing-5.properties` | **208** | **Boss Fighting:** Base QoL + 38 Shared PvM Combat plugins + 6 Bossing exclusives (`zulrah-helper`, `hunllef-helper`, `the-gauntlet`, `vorkath-run-warning`, `gauntlet-crafting`, `barrows-door-highlighter`). |
| **`Raids - ToA`** | `Raids - ToA-2.properties` | **205** | **Tombs of Amascut:** Base QoL + 38 Shared PvM Combat plugins + 3 ToA exclusives (`tombs-of-amascut`, `toa-points-tracker`, `toa-gear-check`). |
| **`Raids - CoX`** | `Raids - CoX-3.properties` | **205** | **Chambers of Xeric:** Base QoL + 38 Shared PvM Combat plugins + 3 CoX exclusives (`cox-qol`, `cox-additions`, `raid-points-overlay`). |
| **`Raids - ToB`** | `Raids - ToB-4.properties` | **209** | **Theatre of Blood:** Base QoL + 38 Shared PvM Combat plugins + 7 ToB exclusives (`tobqol`, `tob-notification`, `nyloer`, `nylo-death-indicators`, `tob-light-colors`, `tob-gear-checker`, `tob-drop-chance`). |
| **`Skilling & Minigames`** | `Skilling & Minigames-6.properties` | **227** | **Skilling & Minigames:** Base QoL + 63 Minigame/Skill training exclusives (Tempoross, Wintertodt, GOTR, Mahogany Homes, Giants Foundry, etc.). |
| **`Wilderness`** | `Wilderness-8.properties` | **214** | **Wilderness & PvP:** Base QoL + 38 Shared PvM Combat plugins + 12 Wilderness Danger & Teleport exclusives (`wilderness-player-alarm`, `wilderness-multi-lines`, `protect-item-notifier`, etc.). |
| **`$rsprofile`** | `$rsprofile--1.properties` | **189** | **Account-Wide Profile:** RuneLite's underlying account-wide settings file. |

---

## 🧩 1. Master Base QoL Plugins (`default-0.properties` - 164 Plugins)

### 1. `117hd` (117hd)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/117HD/RLHD](https://github.com/117HD/RLHD)
* **Last Updated on GitHub:** `28 days ago`
* **Function Summary:** High-Definition 3D graphics engine adding dynamic lighting, shadow rendering, atmospheric fog, and enhanced PBR textures to Old School RuneScape.

### 2. `3d-weather` (3d Weather)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/ScreteMonge/3D-Weather](https://github.com/ScreteMonge/3D-Weather)
* **Last Updated on GitHub:** `2 months ago`
* **Function Summary:** Renders dynamic 3D weather effects (rain, snow, storm clouds, fog) with ambient environmental soundscapes across Gielinor.

### 3. `action-progress` (Action Progress)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/guillaume009/runelite-plugin-action-progress](https://github.com/guillaume009/runelite-plugin-action-progress)
* **Last Updated on GitHub:** `16 days ago`
* **Function Summary:** Displays exact tick progress bars over player head showing completion progress for skilling actions like woodcutting, mining, cooking, and crafting.

### 4. `afk-overlay` (Afk Overlay)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/zmertz/AFK-Overlay](https://github.com/zmertz/AFK-Overlay)
* **Last Updated on GitHub:** `1 month ago`
* **Function Summary:** Displays visual idle timers and warning flashes when your player character is inactive or about to log out.

### 5. `annoyance-mute` (Annoyance Mute)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Broooklyn/runelite-external-plugins](https://github.com/Broooklyn/runelite-external-plugins)
* **Last Updated on GitHub:** `4 days ago`
* **Function Summary:** Mutes annoying ambient sound effects in high-traffic areas (pet noises, splashers, whistle sounds, teleport loops).

### 6. `another-bronzeman-mode` (Another Bronzeman Mode)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/CodePanter/another-bronzeman-mode](https://github.com/CodePanter/another-bronzeman-mode)
* **Last Updated on GitHub:** `6 months ago`
* **Function Summary:** Tracks item unlocks for Bronze Man Mode accounts, notifying you when you obtain new items.

### 7. `bank-cleaner` (Bank Cleaner)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Jerpent/bank-cleaner-plugin](https://github.com/Jerpent/bank-cleaner-plugin)
* **Last Updated on GitHub:** `4 months ago`
* **Function Summary:** Highlights junk items, outdated quest items, and useless bank clutter to assist in cleaning bank space.

### 8. `bank-equipment-stat-filter` (Bank Equipment Stat Filter)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/adamgiles1/bank-equipment-stat-filter](https://github.com/adamgiles1/bank-equipment-stat-filter)
* **Last Updated on GitHub:** `2 years ago`
* **Function Summary:** Filters bank items by specific equipment bonuses (Slash, Crush, Mage, Range, Prayer, Strength).

### 9. `bank-multisearch` (Bank Multisearch)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/geheur/bank-multisearch](https://github.com/geheur/bank-multisearch)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Enables multi-keyword bank searching using logical boolean operators (AND, OR, NOT).

### 10. `bank-organizer` (Bank Organizer)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Ideonomy-web/bank-organizer](https://github.com/Ideonomy-web/bank-organizer)
* **Last Updated on GitHub:** `9 months ago`
* **Function Summary:** Provides automated tab organization, custom layout sorting, and item grouping in the bank interface.

### 11. `bank-slot-sync` (Bank Slot Sync)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/kitten-lissy/bank-slot-sync](https://github.com/kitten-lissy/bank-slot-sync)
* **Last Updated on GitHub:** `5 months ago`
* **Function Summary:** Synchronizes bank tab layouts and slot arrangements across different profiles.

### 12. `bank-tag-layouts` (Bank Tag Layouts)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/geheur/bank-tag-custom-layouts](https://github.com/geheur/bank-tag-custom-layouts)
* **Last Updated on GitHub:** `2 months ago`
* **Function Summary:** Enables custom drag-and-drop grid arrangements for Bank Tags without altering actual bank item positions.

### 13. `banked-experience` (Banked Experience)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/TheStonedTurtle/banked-experience](https://github.com/TheStonedTurtle/banked-experience)
* **Last Updated on GitHub:** `5 months ago`
* **Function Summary:** Calculates total skilling XP stored in your bank across Herblore, Cooking, Crafting, Smithing, and Farming supplies.

### 14. `better-npc-highlight` (Better Npc Highlight)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/riktenx/better-npc-highlight](https://github.com/riktenx/better-npc-highlight)
* **Last Updated on GitHub:** `1 month ago`
* **Function Summary:** Customizable NPC tile, hull, and outline highlighter with true tile tracking.

### 15. `better-skill-tooltips` (Better Skill Tooltips)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Enriath/external-plugins](https://github.com/Enriath/external-plugins)
* **Last Updated on GitHub:** `5 months ago`
* **Function Summary:** Displays detailed XP remaining, actions remaining until level up, and XP rates in skill tooltips.

### 16. `bingosrs` (Bingosrs)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/mistereman22/bingosrs-runelite-plugin](https://github.com/mistereman22/bingosrs-runelite-plugin)
* **Last Updated on GitHub:** `9 months ago`
* **Function Summary:** Bingo event tile tracker for clan events, tracking tile completions and task progress.

### 17. `birdhouse-overlay` (Birdhouse Overlay)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/hong-niu/runelite-birdhouse-overlay](https://github.com/hong-niu/runelite-birdhouse-overlay)
* **Last Updated on GitHub:** `3 years ago`
* **Function Summary:** Displays birdhouse trap states, seed requirements, and timer countdowns on Fossil Island.

### 18. `birdhouse-status` (Birdhouse Status)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Yosef-rm1/birdhouse-status](https://github.com/Yosef-rm1/birdhouse-status)
* **Last Updated on GitHub:** `7 months ago`
* **Function Summary:** Infobox timer showing when Fossil Island birdhouse traps are ready to be harvested.

### 19. `boat-hider` (Boat Hider)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/marknewan/newan-plugins](https://github.com/marknewan/newan-plugins)
* **Last Updated on GitHub:** `2 months ago`
* **Function Summary:** Hides surrounding player boats in busy harbors to improve visibility and frame rates.

### 20. `boat-upgrades` (Boat Upgrades)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/IEarnSolo/boat-upgrades](https://github.com/IEarnSolo/boat-upgrades)
* **Last Updated on GitHub:** `6 months ago`
* **Function Summary:** Displays boat hull, sail, and rudder upgrade requirements, stats, and installation status.

### 21. `boss-levels` (Boss Levels)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/rasimaosrs/BossLevels](https://github.com/rasimaosrs/BossLevels)
* **Last Updated on GitHub:** `6 months ago`
* **Function Summary:** Displays monster and boss combat level numbers in target overlays and right-click menus.

### 22. `bot-detector` (Bot Detector)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Bot-detector/bot-detector](https://github.com/Bot-detector/bot-detector)
* **Last Updated on GitHub:** `8 months ago`
* **Function Summary:** Community crowdsourcing plugin analyzing nearby player movement patterns to flag bot accounts.

### 23. `c-engineer-completed` (C Engineer Completed)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/m0bilebtw/c-engineer-completed](https://github.com/m0bilebtw/c-engineer-completed)
* **Last Updated on GitHub:** `6 months ago`
* **Function Summary:** Plays C Engineer voice lines when completing quests, levelling up, dying, or achieving collection log slots.

### 24. `camera-smoothing` (Camera Smoothing)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/ArtsicleOfficial/camera-smoothing](https://github.com/ArtsicleOfficial/camera-smoothing)
* **Last Updated on GitHub:** `25 days ago`
* **Function Summary:** Adds smooth acceleration and deceleration curves to camera movement and mouse drag rotations.

### 25. `center-skill-icons` (Center Skill Icons)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/jakebrehm/center-skill-icons](https://github.com/jakebrehm/center-skill-icons)
* **Last Updated on GitHub:** `5 months ago`
* **Function Summary:** Centers skill icons inside the Stats tab interface for improved visual alignment.

### 26. `chat-scroll-lock` (Chat Scroll Lock)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/jacwalste/chat-scroll-lock](https://github.com/jacwalste/chat-scroll-lock)
* **Last Updated on GitHub:** `7 months ago`
* **Function Summary:** Locks chatbox scroll position when scrolling up so incoming messages don't force auto-scroll to bottom.

### 27. `chatbox-opacity` (Chatbox Opacity)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Trevor159/runelite-external-plugins](https://github.com/Trevor159/runelite-external-plugins)
* **Last Updated on GitHub:** `6 years ago`
* **Function Summary:** Customizes chatbox background transparency and text shadow opacity.

### 28. `citizens` (Citizens)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/gc/citizens](https://github.com/gc/citizens)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Adds ambient NPC dialogue, idle animations, and walking paths to make towns feel more alive.

### 29. `clan-chat-country-flags` (Clan Chat Country Flags)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/rmobis/clan-chat-country-flags](https://github.com/rmobis/clan-chat-country-flags)
* **Last Updated on GitHub:** `19 days ago`
* **Function Summary:** Displays country flag icons next to member names in clan chat based on location settings.

### 30. `clan-event-attendance` (Clan Event Attendance)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/JoRouss/runelite-ClanEventAttendance](https://github.com/JoRouss/runelite-ClanEventAttendance)
* **Last Updated on GitHub:** `5 months ago`
* **Function Summary:** Automated clan event attendance tracker logging member names in area radii.

### 31. `clan-rank-up-notifier` (Clan Rank Up Notifier)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/serverlat/clan-rank-up-notifier](https://github.com/serverlat/clan-rank-up-notifier)
* **Last Updated on GitHub:** `5 months ago`
* **Function Summary:** Alerts clan leaders when members reach point or XP thresholds for rank promotions.

### 32. `clean-chat` (Clean Chat)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/ldavid432/chat-cleanup](https://github.com/ldavid432/chat-cleanup)
* **Last Updated on GitHub:** `1 month ago`
* **Function Summary:** Filters out toxic chat text, website spam, and repeated spam messages in public areas.

### 33. `click-minimap-orbs` (Click Minimap Orbs)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Macweese/runelite-external-plugins](https://github.com/Macweese/runelite-external-plugins)
* **Last Updated on GitHub:** `2 years ago`
* **Function Summary:** Customizes click actions on minimap HP, Prayer, Run, and Spec orbs.

### 34. `clue-details` (Clue Details)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Zoinkwiz/clue-details](https://github.com/Zoinkwiz/clue-details)
* **Last Updated on GitHub:** `2 months ago`
* **Function Summary:** Displays required items, skill requirements, and challenge answers for active clue steps.

### 35. `clue-scroll-juggling` (Clue Scroll Juggling)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/geheur/clue-juggling-timers](https://github.com/geheur/clue-juggling-timers)
* **Last Updated on GitHub:** `2 years ago`
* **Function Summary:** Ground item despawn timers and location beacons for juggled clue scrolls.

### 36. `clue-scroll-notifier` (Clue Scroll Notifier)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/SoaresPT/clue-scroll-notifier](https://github.com/SoaresPT/clue-scroll-notifier)
* **Last Updated on GitHub:** `7 months ago`
* **Function Summary:** Audio alert and screen flash when a clue scroll drops on the ground.

### 37. `clue-steps` (Clue Steps)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/SkyBouncer/clue_step_tracker](https://github.com/SkyBouncer/clue_step_tracker)
* **Last Updated on GitHub:** `4 months ago`
* **Function Summary:** Full clue scroll step solver displaying exact map coordinates, answer keys, and anagram solutions.

### 38. `clue-teleport-helper` (Clue Teleport Helper)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/kitten-lissy/clue-teleport-helper](https://github.com/kitten-lissy/clue-teleport-helper)
* **Last Updated on GitHub:** `3 months ago`
* **Function Summary:** Overlays map teleport destinations, fairy rings, spirit trees, and scroll locations directly on active clue steps.

### 39. `collection-log` (Collection Log)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/evansloan/collection-log](https://github.com/evansloan/collection-log)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Tracks collection log achievements, total slots unlocked, and drop rates.

### 40. `collection-log-luck` (Collection Log Luck)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/peanubnutter/collection-log-luck](https://github.com/peanubnutter/collection-log-luck)
* **Last Updated on GitHub:** `3 months ago`
* **Function Summary:** Calculates statistical RNG luck percentages on collection log drops compared to drop rates.

### 41. `compass-camera-control` (Compass Camera Control)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/RaazKH/CompassCameraControl](https://github.com/RaazKH/CompassCameraControl)
* **Last Updated on GitHub:** `4 days ago`
* **Function Summary:** Clicking compass aligns camera to North, East, South, or West with custom angles.

### 42. `cooking-buddy` (Cooking Buddy)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/MapleBytes/CookingBuddy](https://github.com/MapleBytes/CookingBuddy)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Displays burn rates, cooking timers, and food success thresholds on fires and ranges.

### 43. `corner-tile-indicators` (Corner Tile Indicators)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/geheur/Corner-Tile-Indicators](https://github.com/geheur/Corner-Tile-Indicators)
* **Last Updated on GitHub:** `8 months ago`
* **Function Summary:** Renders sleek corner tick outlines on target true tiles instead of full box outlines.

### 44. `cough-syrup` (Cough Syrup)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/edmeyer8851/cough-syrup](https://github.com/edmeyer8851/cough-syrup)
* **Last Updated on GitHub:** `11 months ago`
* **Function Summary:** Removes player 'Cough! Cough!' public chat text spam during Nex's Choke attack.

### 45. `customizable-xp-drops` (Customizable Xp Drops)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/l2-/template-plugin](https://github.com/l2-/template-plugin)
* **Last Updated on GitHub:** `5 days ago`
* **Function Summary:** Customizes XP drop font colors, icons, positioning, animations, and grouping.

### 46. `decimal-prices` (Decimal Prices)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/rmaes4/decimal-prices](https://github.com/rmaes4/decimal-prices)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Displays item prices in bank and examine texts with precise decimal points (e.g. 1.2M instead of 1M).

### 47. `default-minimap-zoom` (Default Minimap Zoom)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/YvesW/default-minimap-zoom](https://github.com/YvesW/default-minimap-zoom)
* **Last Updated on GitHub:** `10 days ago`
* **Function Summary:** Locks minimap zoom scale to your preferred default level upon login.

### 48. `did-i-compost` (Did I Compost)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/AbusiveTuna/DidICompost](https://github.com/AbusiveTuna/DidICompost)
* **Last Updated on GitHub:** `12 days ago`
* **Function Summary:** Overlays farming patches with visual indicators confirming whether ultracompost/supercompost was applied.

### 49. `dink` (Dink)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/pajlads/DinkPlugin](https://github.com/pajlads/DinkPlugin)
* **Last Updated on GitHub:** `6 days ago`
* **Function Summary:** Webhook integration sending Discord notifications for level ups, drops, deaths, and clue completions.

### 50. `discord-collection-logger` (Discord Collection Logger)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/PJGJ210/Discord-Collection-Logger](https://github.com/PJGJ210/Discord-Collection-Logger)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Sends custom Discord rich embeds whenever a collection log slot is unlocked.

### 51. `divine-skies` (Divine Skies)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/GarnetDivine/divine-skies](https://github.com/GarnetDivine/divine-skies)
* **Last Updated on GitHub:** `4 months ago`
* **Function Summary:** Custom skybox plugin rendering beautiful day/night environmental skies.

### 52. `drop-party-chest` (Drop Party Chest)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/pgroenbaek/drop-party-chest](https://github.com/pgroenbaek/drop-party-chest)
* **Last Updated on GitHub:** `9 months ago`
* **Function Summary:** Displays item values and countdown timers for Falador Drop Party Chest balloons.

### 53. `duck-duck-goose` (Duck Duck Goose)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/skeldoor/duck-duck-goose](https://github.com/skeldoor/duck-duck-goose)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Adds visual ducks floating in bodies of water across Gielinor (Yanille, Barbarian Village, Zul-Andra, Darkmeyer) that you can feed bread.

### 54. `dude-wheres-my-stuff` (Dude Wheres My Stuff)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Thource/dude-wheres-my-stuff](https://github.com/Thource/dude-wheres-my-stuff)
* **Last Updated on GitHub:** `2 months ago`
* **Function Summary:** Tracks item locations across your account (Death vaults, CoX chest, Coffer, Seed vault, Toolbelt, Minigame storage).

### 55. `easy-empty` (Easy Empty)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/jpeter17/easy-empty](https://github.com/jpeter17/easy-empty)
* **Last Updated on GitHub:** `4 years ago`
* **Function Summary:** Provides one-click 'Empty' menu entry swapper on Runecrafting pouches, Gem bags, and Herb sacks.

### 56. `easy-pharaoh-sceptre` (Easy Pharaoh Sceptre)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/dappermickie/easy-teleports](https://github.com/dappermickie/easy-teleports)
* **Last Updated on GitHub:** `3 days ago`
* **Function Summary:** Swaps right-click teleport options on Pharaoh's Sceptre for one-click teleports to Jaldraocht Pyramid or West Ardougne.

### 57. `effective-level` (Effective Level)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/XrioBtw/effectivelevel-plugin](https://github.com/XrioBtw/effectivelevel-plugin)
* **Last Updated on GitHub:** `9 months ago`
* **Function Summary:** Calculates effective combat skill levels including active potion boosts, prayers, and equipment bonuses.

### 58. `elysiumevents-plugin` (Elysiumevents Plugin)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/cmsu224/clan-events](https://github.com/cmsu224/clan-events)
* **Last Updated on GitHub:** `11 months ago`
* **Function Summary:** Clan event tracking and scoring helper for Elysium clan events.

### 59. `emote-clue-items` (Emote Clue Items)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/larsvansoest/emote-clue-items](https://github.com/larsvansoest/emote-clue-items)
* **Last Updated on GitHub:** `6 months ago`
* **Function Summary:** Badges items in your bank and inventory that are required for emote clue steps.

### 60. `equipment-inspector` (Equipment Inspector)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/botanicvelious/Equipment-Inspector](https://github.com/botanicvelious/Equipment-Inspector)
* **Last Updated on GitHub:** `1 month ago`
* **Function Summary:** Allows right-clicking nearby players to view their full equipped gear list and estimated market value.

### 61. `event-scouting` (Event Scouting)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/peanubnutter/scoutingplugin](https://github.com/peanubnutter/scoutingplugin)
* **Last Updated on GitHub:** `7 months ago`
* **Function Summary:** Scouts active world event spawns across Gielinor.

### 62. `examine-log` (Examine Log)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/CarlOmega/examine-log](https://github.com/CarlOmega/examine-log)
* **Last Updated on GitHub:** `5 months ago`
* **Function Summary:** Logs examine texts and trivia info for items, NPCs, and objects in a sidebar tab.

### 63. `fixed-resizable-hybrid` (Fixed Resizable Hybrid)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Lapask/fixed-resizable-hybrid](https://github.com/Lapask/fixed-resizable-hybrid)
* **Last Updated on GitHub:** `5 months ago`
* **Function Summary:** Enables hybrid fixed-in-resizable interface mode for classic feel on modern monitors.

### 64. `foodutils` (Foodutils)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/RayvonneM/FoodUtils](https://github.com/RayvonneM/FoodUtils)
* **Last Updated on GitHub:** `4 months ago`
* **Function Summary:** Displays food healing amounts and potion dose numbers directly on inventory icons.

### 65. `fossil-island` (Fossil Island)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Adam-/runelite-plugins](https://github.com/Adam-/runelite-plugins)
* **Last Updated on GitHub:** `5 years ago`
* **Function Summary:** Map highlights and activity guides for Fossil Island (Camp, Sulliusceps, Volcanic Mine, Underwater).

### 66. `friends-house` (Friends House)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/EwyBoy/Friends-House](https://github.com/EwyBoy/Friends-House)
* **Last Updated on GitHub:** `2 years ago`
* **Function Summary:** Remembers host names for Player-Owned Houses and provides quick-enter options.

### 67. `full-inv` (Full Inv)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Zazarothh/full-inv](https://github.com/Zazarothh/full-inv)
* **Last Updated on GitHub:** `6 months ago`
* **Function Summary:** Screen border warning flash when your inventory becomes completely full.

### 68. `fuzzy-bank-search` (Fuzzy Bank Search)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/i/rl-plugins](https://github.com/i/rl-plugins)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Enables fuzzy matching bank searches so typos still find the item you are looking for.

### 69. `glamourer` (Glamourer)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/jhughes/glamourer](https://github.com/jhughes/glamourer)
* **Last Updated on GitHub:** `29 days ago`
* **Function Summary:** Local cosmetic gear override plugin allowing custom visual gear appearances on your character.

### 70. `goal-tracker` (Goal Tracker)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Darkforge317/rl-goal-tracker](https://github.com/Darkforge317/rl-goal-tracker)
* **Last Updated on GitHub:** `15 days ago`
* **Function Summary:** Sidebar goal checklist tracker for account progress, quests, and gear upgrades.

### 71. `goggles-reminder` (Goggles Reminder)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Noatel/GogglesReminder](https://github.com/Noatel/GogglesReminder)
* **Last Updated on GitHub:** `11 months ago`
* **Function Summary:** Alerts you if required headgear (Earmuffs, Gas mask, Facemask) is missing when entering slayer dungeons.

### 72. `gp-per-hour` (Gp Per Hour)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/MosheBenZacharia/GP-Per-Hour](https://github.com/MosheBenZacharia/GP-Per-Hour)
* **Last Updated on GitHub:** `1 month ago`
* **Function Summary:** Tracks real-time GP profit per hour from loot drops, supply usage, and alching.

### 73. `group-iron-panel` (Group Iron Panel)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/toasty-toast/runelite-group-iron-panel](https://github.com/toasty-toast/runelite-group-iron-panel)
* **Last Updated on GitHub:** `8 months ago`
* **Function Summary:** Displays Group Iron Man member stats, inventory contents, bank, and online status in a sidebar panel.

### 74. `hd-minimap` (Hd Minimap)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Mark7625/runelite-external-plugins](https://github.com/Mark7625/runelite-external-plugins)
* **Last Updated on GitHub:** `5 months ago`
* **Function Summary:** Applies high-definition 117HD textures to the minimap.

### 75. `high-alc-highlight` (High Alc Highlight)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/bloogeyz/high-alc-value](https://github.com/bloogeyz/high-alc-value)
* **Last Updated on GitHub:** `27 days ago`
* **Function Summary:** Calculates profit margins and badges high-alch items in your inventory and bank.

### 76. `highlight-stackable-items` (Highlight Stackable Items)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/horse4lunch/Highlight-Stackable-Items](https://github.com/horse4lunch/Highlight-Stackable-Items)
* **Last Updated on GitHub:** `3 years ago`
* **Function Summary:** Highlights stackable items on ground loot overlays.

### 77. `hot-cold-helper` (Hot Cold Helper)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/lalochazia/hot-cold-helper](https://github.com/lalochazia/hot-cold-helper)
* **Last Updated on GitHub:** `4 months ago`
* **Function Summary:** Calculates exact target coordinates for Strange Device hot/cold clue steps using triangulation.

### 78. `improved-tile-indicators` (Improved Tile Indicators)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/LeikvollE/tileindicators](https://github.com/LeikvollE/tileindicators)
* **Last Updated on GitHub:** `9 months ago`
* **Function Summary:** Renders smooth anti-aliased true tile outlines for player and target entities.

### 79. `instant-inventory` (Instant Inventory)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/elgbar/instant-inventory](https://github.com/elgbar/instant-inventory)
* **Last Updated on GitHub:** `10 months ago`
* **Function Summary:** Eliminates visual delay when opening inventory or switching interface tabs.

### 80. `inventory-setups` (Inventory Setups)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/dillydill123/inventory-setups](https://github.com/dillydill123/inventory-setups)
* **Last Updated on GitHub:** `2 months ago`
* **Function Summary:** Allows creating, ordering, and tagging custom gear & inventory setups with bank highlighting and bank tag layouts.

### 81. `key-remapping-plus` (Key Remapping Plus)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/macica2/key-remapping-plus](https://github.com/macica2/key-remapping-plus)
* **Last Updated on GitHub:** `1 month ago`
* **Function Summary:** Remaps WASD keys to camera movement and custom keybindings without interfering with chat typing.

### 82. `kill-count-viewer` (Kill Count Viewer)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/RedSparr0w/runelite-plugins](https://github.com/RedSparr0w/runelite-plugins)
* **Last Updated on GitHub:** `8 days ago`
* **Function Summary:** Displays monster kill counts and boss PB times in target overlays.

### 83. `kitten-tracker` (Kitten Tracker)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/pieterjanbuntinx/kitten-tracker](https://github.com/pieterjanbuntinx/kitten-tracker)
* **Last Updated on GitHub:** `9 months ago`
* **Function Summary:** Tracks kitten hunger, attention, and growth stage countdown timer until it becomes a cat.

### 84. `konar-milestone-reminder` (Konar Milestone Reminder)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/michael-gutman/konar-milestone-reminder](https://github.com/michael-gutman/konar-milestone-reminder)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Alerts you to use Konar every 10th/50th Slayer task for bonus points.

### 85. `large-logout` (Large Logout)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/dekvall/runelite-external-plugins](https://github.com/dekvall/runelite-external-plugins)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Enlarges the logout button for quick panic logouts.

### 86. `last-seen-online` (Last Seen Online)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/molo-pl/runelite-plugins](https://github.com/molo-pl/runelite-plugins)
* **Last Updated on GitHub:** `3 months ago`
* **Function Summary:** Tracks when friends and clan members were last seen online in your friend list.

### 87. `location-display` (Location Display)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/trinhc2/Location-Display](https://github.com/trinhc2/Location-Display)
* **Last Updated on GitHub:** `5 months ago`
* **Function Summary:** Displays current area region name, chunk ID, and world coordinates on screen.

### 88. `lootbag-utilities` (Lootbag Utilities)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/LootBagger/LootbagUtilities](https://github.com/LootBagger/LootbagUtilities)
* **Last Updated on GitHub:** `2 years ago`
* **Function Summary:** One-click 'Deposit' menu entry swapper for Looting Bag.

### 89. `master-scroll-book` (Master Scroll Book)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Enriath/external-plugins](https://github.com/Enriath/external-plugins)
* **Last Updated on GitHub:** `2 years ago`
* **Function Summary:** Displays charges, teleport destinations, and quick-scroll options for the Master Scroll Book.

### 90. `max-skill-trim` (Max Skill Trim)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Nerdpuff/max-skill-trim](https://github.com/Nerdpuff/max-skill-trim)
* **Last Updated on GitHub:** `3 months ago`
* **Function Summary:** Displays custom cosmetic trims on skill capes when reaching max skill milestones.

### 91. `milestone-levels` (Milestone Levels)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Antimated/milestone-levels](https://github.com/Antimated/milestone-levels)
* **Last Updated on GitHub:** `8 months ago`
* **Function Summary:** Highlights upcoming total level milestone thresholds (e.g. Total 1750, 2000).

### 92. `missing-pet-notifier` (Missing Pet Notifier)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/tylerwgrass/missing-pet-notifier](https://github.com/tylerwgrass/missing-pet-notifier)
* **Last Updated on GitHub:** `8 months ago`
* **Function Summary:** Warning notification if your pet accidentally gets un-summoned or lost.

### 93. `modern-chat` (Modern Chat)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/BenDol/Modern-Chat](https://github.com/BenDol/Modern-Chat)
* **Last Updated on GitHub:** `3 months ago`
* **Function Summary:** Modernizes chatbox UI font style, spacing, and chat bubble aesthetics.

### 94. `more-fireworks` (More Fireworks)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/MarbleTurtle/MoreFireworks](https://github.com/MarbleTurtle/MoreFireworks)
* **Last Updated on GitHub:** `5 years ago`
* **Function Summary:** Adds extra celebratory fireworks particle effects on level ups and quest completes.

### 95. `named-pets` (Named Pets)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Sacca-1/named-pets-runelite](https://github.com/Sacca-1/named-pets-runelite)
* **Last Updated on GitHub:** `13 days ago`
* **Function Summary:** Allows giving custom display names to your follower pets.

### 96. `nexus-map` (Nexus Map)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Antipixel/nexus-map](https://github.com/Antipixel/nexus-map)
* **Last Updated on GitHub:** `2 months ago`
* **Function Summary:** Displays interactive portal destination map on POH Portal Nexus.

### 97. `night-day-cycle` (Night Day Cycle)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/rodhfr/DayNightCycle](https://github.com/rodhfr/DayNightCycle)
* **Last Updated on GitHub:** `9 months ago`
* **Function Summary:** Simulates real-world day and night ambient lighting cycles across Gielinor.

### 98. `no-bad-alchs` (No Bad Alchs)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/CreativeTechGuy/no-bad-alchs](https://github.com/CreativeTechGuy/no-bad-alchs)
* **Last Updated on GitHub:** `4 months ago`
* **Function Summary:** Provides a safety confirmation pop-up when attempting to high-alch high-value gear or untradeables.

### 99. `npc-contact-filter` (Npc Contact Filter)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/OldShrimp/npc-contact-filter](https://github.com/OldShrimp/npc-contact-filter)
* **Last Updated on GitHub:** `1 day ago`
* **Function Summary:** Filters NPC Contact spell list for quick one-click casting to preferred NPCs (Slayer masters, Dark Mage).

### 100. `osrs-tcg` (Osrs Tcg)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Azderi/osrs-tcg](https://github.com/Azderi/osrs-tcg)
* **Last Updated on GitHub:** `3 days ago`
* **Function Summary:** Trading card game overlay minigame inside RuneLite.

### 101. `osrs-wiki-crowdsourcing` (Osrs Wiki Crowdsourcing)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/leejt/osrs-wiki-crowdsourcing](https://github.com/leejt/osrs-wiki-crowdsourcing)
* **Last Updated on GitHub:** `2 months ago`
* **Function Summary:** Background data collection plugin submitting drop data to the official OSRS Wiki.

### 102. `partial-sets` (Partial Sets)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Fiskmans/rl_partial_sets](https://github.com/Fiskmans/rl_partial_sets)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Highlights partial barrows/equipment sets in bank missing 1 or 2 pieces.

### 103. `party-panel` (Party Panel)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/TheStonedTurtle/party-panel](https://github.com/TheStonedTurtle/party-panel)
* **Last Updated on GitHub:** `1 month ago`
* **Function Summary:** Displays party member HP, Prayer, spec energy, inventory, and location in a sidebar panel.

### 104. `path-marker` (Path Marker)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/GeChallengeM/path-marker](https://github.com/GeChallengeM/path-marker)
* **Last Updated on GitHub:** `3 days ago`
* **Function Summary:** Renders exact tile path lines your character will walk along when clicking a destination.

### 105. `pet-info` (Pet Info)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/microtavor5/PetInfoPlugin](https://github.com/microtavor5/PetInfoPlugin)
* **Last Updated on GitHub:** `1 month ago`
* **Function Summary:** Displays pet drop rates, examine info, and fun facts when inspecting follower pets.

### 106. `pet-spell-blocker` (Pet Spell Blocker)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Sacca-1/Wildy-QoL](https://github.com/Sacca-1/Wildy-QoL)
* **Last Updated on GitHub:** `20 days ago`
* **Function Summary:** Prevents accidental spell casts or attack clicks on follower pets.

### 107. `placeholders-warning` (Placeholders Warning)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/CheesyCracks/placeholders-warning](https://github.com/CheesyCracks/placeholders-warning)
* **Last Updated on GitHub:** `5 months ago`
* **Function Summary:** Warning alert when withdrawing the last item of a stack without bank placeholders enabled.

### 108. `player-outline` (Player Outline)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Adam-/runelite-plugins](https://github.com/Adam-/runelite-plugins)
* **Last Updated on GitHub:** `4 years ago`
* **Function Summary:** Renders sleek character outlines around your player character for high visibility during raids.

### 109. `pleae` (Pleae)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/toasty-toast/runelite-pleae](https://github.com/toasty-toast/runelite-pleae)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Replaces death message text with classic 'pleae' meme text on player death.

### 110. `poh-storage` (Poh Storage)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/tcpowell/poh-storage](https://github.com/tcpowell/poh-storage)
* **Last Updated on GitHub:** `3 years ago`
* **Function Summary:** Displays POH Costume Room, Toy Box, and Armour Case item requirements and stored set status.

### 111. `potion-storage-bars` (Potion Storage Bars)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Hannamber/potion-bars](https://github.com/Hannamber/potion-bars)
* **Last Updated on GitHub:** `26 days ago`
* **Function Summary:** Displays dosage bars over potion decanting storage barrels.

### 112. `prifddinas` (Prifddinas)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/DavidVentura/runelite-plugins](https://github.com/DavidVentura/runelite-plugins)
* **Last Updated on GitHub:** `4 years ago`
* **Function Summary:** City guide map overlays for Prifddinas crystal implings and agility shortcuts.

### 113. `purchase-progress` (Purchase Progress)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/BrastaSauce/purchase-progress](https://github.com/BrastaSauce/purchase-progress)
* **Last Updated on GitHub:** `2 years ago`
* **Function Summary:** Tracks total GP spent on gear upgrades towards your dream gear set.

### 114. `pvm-score` (Pvm Score)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/fatmownes/pvm-score](https://github.com/fatmownes/pvm-score)
* **Last Updated on GitHub:** `23 days ago`
* **Function Summary:** Calculates custom PvM performance score based on boss KCs and Combat Achievements.

### 115. `qol-interfaces` (Qol Interfaces)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Col-Log/QOL-Interface](https://github.com/Col-Log/QOL-Interface)
* **Last Updated on GitHub:** `3 months ago`
* **Function Summary:** General UI enhancements for shop interfaces, trade screens, and dialogue boxes.

### 116. `quest-helper` (Quest Helper)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Zoinkwiz/quest-helper](https://github.com/Zoinkwiz/quest-helper)
* **Last Updated on GitHub:** `28 days ago`
* **Function Summary:** Step-by-step quest guide rendering world arrow indicators, puzzle solutions, and dialogue choices.

### 117. `random-event-hider` (Random Event Hider)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/YvesW/random-event-hider](https://github.com/YvesW/random-event-hider)
* **Last Updated on GitHub:** `2 years ago`
* **Function Summary:** Hides useless random events (Genie, Quiz master) while keeping valuable ones visible.

### 118. `recolored-herb-seeds` (Recolored Herb Seeds)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Mike-U5/HerbSeedIcons](https://github.com/Mike-U5/HerbSeedIcons)
* **Last Updated on GitHub:** `2 years ago`
* **Function Summary:** Recolors herb seed icons in bank and inventory based on herb tier and farming value.

### 119. `relative-tile-markers` (Relative Tile Markers)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/millman97/RelativeTileMarkers](https://github.com/millman97/RelativeTileMarkers)
* **Last Updated on GitHub:** `10 months ago`
* **Function Summary:** Marks tiles relative to your player character position for tick manipulation methods.

### 120. `resizable-chat` (Resizable Chat)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Thource/resizable-chat](https://github.com/Thource/resizable-chat)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Allows resizing chatbox height and width dynamically in resizable mode.

### 121. `rich-text-notes` (Rich Text Notes)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/lgwood/rich-text-notes](https://github.com/lgwood/rich-text-notes)
* **Last Updated on GitHub:** `10 months ago`
* **Function Summary:** Rich text notepad sidebar plugin supporting formatted notes, checkboxes, and task lists.

### 122. `runepouch-loadouts` (Runepouch Loadouts)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/DapperMickie/runepouch-loadout-names](https://github.com/DapperMickie/runepouch-loadout-names)
* **Last Updated on GitHub:** `21 days ago`
* **Function Summary:** Save and load custom rune pouch configurations for quick one-click filling.

### 123. `runeprofile` (Runeprofile)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/ReinhardtR/runeprofile-plugin](https://github.com/ReinhardtR/runeprofile-plugin)
* **Last Updated on GitHub:** `13 days ago`
* **Function Summary:** Profile sync helper saving settings to RuneProfile cloud.

### 124. `runewatch` (Runewatch)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/while-loop/runelite-plugins](https://github.com/while-loop/runelite-plugins)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Integrates RuneWatch scammer database warnings on trade screens and party invites.

### 125. `sailing` (Sailing)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/LlemonDuck/sailing](https://github.com/LlemonDuck/sailing)
* **Last Updated on GitHub:** `1 month ago`
* **Function Summary:** Main Sailing skill overlay providing boat steering controls, wind direction overlays, island navigation, and speed indicators.

### 126. `scrollboxcounter` (Scrollboxcounter)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/IEarnSolo/scrollboxcounter](https://github.com/IEarnSolo/scrollboxcounter)
* **Last Updated on GitHub:** `2 months ago`
* **Function Summary:** Badges unopened clue scroll boxes in your bank and inventory with count indicators.

### 127. `ship-renamer` (Ship Renamer)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Logical-sh/ship-renamer](https://github.com/Logical-sh/ship-renamer)
* **Last Updated on GitHub:** `8 months ago`
* **Function Summary:** Allows custom naming and formatting for your player ship.

### 128. `shortest-clue` (Shortest Clue)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/KeiranY/clue-pathing-runelite-plugin](https://github.com/KeiranY/clue-pathing-runelite-plugin)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Generates optimal pathfinding routes using teleports, fairy rings, and spirit trees to reach clue steps fast.

### 129. `shortest-path` (Shortest Path)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Skretzo/shortest-path](https://github.com/Skretzo/shortest-path)
* **Last Updated on GitHub:** `1 month ago`
* **Function Summary:** Generates optimal pathfinding routes across Gielinor rendering world tile lines to any target.

### 130. `six-hour-reminder` (Six Hour Reminder)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Richardant/Six-Hour-Reminder](https://github.com/Richardant/Six-Hour-Reminder)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Displays countdown timer until 6-hour force logout limit occurs.

### 131. `skilling-boost-reminder` (Skilling Boost Reminder)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/JonneSaloranta/skilling-boost-reminder](https://github.com/JonneSaloranta/skilling-boost-reminder)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Notifies you when stat or potion boosts (Super combat, Ranging, Imbued heart) expire.

### 132. `skills-tab-progress-bars` (Skills Tab Progress Bars)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/m0bilebtw/skills-tab-progress-bars](https://github.com/m0bilebtw/skills-tab-progress-bars)
* **Last Updated on GitHub:** `8 months ago`
* **Function Summary:** Displays visual XP progress bars under each skill icon in the Stats tab.

### 133. `slayer-task-sorter` (Slayer Task Sorter)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/MJHylkema/slayer-task-sorter](https://github.com/MJHylkema/slayer-task-sorter)
* **Last Updated on GitHub:** `11 months ago`
* **Function Summary:** Sorts and filters Slayer tasks in your Slayer log by location, difficulty, and block status.

### 134. `spamfilter` (Spamfilter)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/jackriccomini/spamfilter-plugin-runelite](https://github.com/jackriccomini/spamfilter-plugin-runelite)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Advanced chat filter blocking website spam, auto-typers, and gambling bots.

### 135. `spawn-marker` (Spawn Marker)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/TalesRK/spawn_marker](https://github.com/TalesRK/spawn_marker)
* **Last Updated on GitHub:** `5 years ago`
* **Function Summary:** Marks NPC spawn point tiles with countdown respawn timers.

### 136. `spawnpredictor` (Spawnpredictor)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/damencs/spawn-predictor](https://github.com/damencs/spawn-predictor)
* **Last Updated on GitHub:** `9 days ago`
* **Function Summary:** Predicts monster spawn locations in Fight Caves, Inferno, and boss rooms.

### 137. `spirit-tree-map` (Spirit Tree Map)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/MJHylkema/spirit-tree-map](https://github.com/MJHylkema/spirit-tree-map)
* **Last Updated on GitHub:** `7 months ago`
* **Function Summary:** Displays interactive world map selector when using Spirit Trees.

### 138. `steps-per-clue` (Steps Per Clue)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Chubs1/StepsPerClue](https://github.com/Chubs1/StepsPerClue)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Tracks completed clue step counts and average steps per tier.

### 139. `target-true-tile` (Target True Tile)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Notloc/runelite-target-true-tile](https://github.com/Notloc/runelite-target-true-tile)
* **Last Updated on GitHub:** `8 days ago`
* **Function Summary:** Renders true tile outlines for current targeted monster or player.

### 140. `tasks-tracker` (Tasks Tracker)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/osrs-reldo/tasks-tracker-plugin](https://github.com/osrs-reldo/tasks-tracker-plugin)
* **Last Updated on GitHub:** `2 months ago`
* **Function Summary:** Task progress tracker for League tasks and Master clue steps.

### 141. `temple-osrs` (Temple Osrs)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/SMaloney2017/Temple-OSRS-Plugin](https://github.com/SMaloney2017/Temple-OSRS-Plugin)
* **Last Updated on GitHub:** `3 months ago`
* **Function Summary:** Integrates Temple OSRS stat tracking and XP gain leaderboards into sidebar.

### 142. `tick-fixer-for-mac` (Tick Fixer For Mac)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/jonathangarelick/tick-fixer](https://github.com/jonathangarelick/tick-fixer)
* **Last Updated on GitHub:** `4 months ago`
* **Function Summary:** Fixes macOS specific frame timing and input latency stutter in RuneLite.

### 143. `tick-manipulation-helper` (Tick Manipulation Helper)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/pwatts6060/runelite-plugins](https://github.com/pwatts6060/runelite-plugins)
* **Last Updated on GitHub:** `2 months ago`
* **Function Summary:** Visual metronome and audio click cues for 3-tick and 2-tick skilling methods.

### 144. `ticktracker` (Ticktracker)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Tatters654/tick-tracker](https://github.com/Tatters654/tick-tracker)
* **Last Updated on GitHub:** `3 years ago`
* **Function Summary:** Monitors server tick stability, tick lag, and ping drops.

### 145. `tictac7x-camera-pitch-limiter` (Tictac7x Camera Pitch Limiter)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/TicTac7x/runelite-plugins](https://github.com/TicTac7x/runelite-plugins)
* **Last Updated on GitHub:** `24 days ago`
* **Function Summary:** Customizes camera pitch limits allowing higher or lower camera viewing angles.

### 146. `tictac7x-charges` (Tictac7x Charges)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/TicTac7x/runelite-plugins](https://github.com/TicTac7x/runelite-plugins)
* **Last Updated on GitHub:** `8 days ago`
* **Function Summary:** Unified item charge counter overlay tracking Barrows gear, Ardougne cloak, Blowpipe, and Ring charges.

### 147. `tictac7x-daily` (Tictac7x Daily)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/TicTac7x/runelite-plugins](https://github.com/TicTac7x/runelite-plugins)
* **Last Updated on GitHub:** `22 days ago`
* **Function Summary:** Daily task checklist tracking Herb runs, Birdhouse runs, Tears of Guthix, and Daily battlestaves.

### 148. `tictac7x-deposit-worn-items` (Tictac7x Deposit Worn Items)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/TicTac7x/runelite-plugins](https://github.com/TicTac7x/runelite-plugins)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** One-click 'Deposit Worn Items' button customization in bank.

### 149. `tictac7x-storage` (Tictac7x Storage)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/TicTac7x/runelite-plugins](https://github.com/TicTac7x/runelite-plugins)
* **Last Updated on GitHub:** `24 days ago`
* **Function Summary:** Displays items stored inside POH costume room and seed vault.

### 150. `tile-packs` (Tile Packs)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/TrevorMDev/tile-packs](https://github.com/TrevorMDev/tile-packs)
* **Last Updated on GitHub:** `18 days ago`
* **Function Summary:** Pre-configured tile marker packs for bosses, quests, and minigames.

### 151. `time-to-max` (Time To Max)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Hamelot/time-to-max](https://github.com/Hamelot/time-to-max)
* **Last Updated on GitHub:** `2 months ago`
* **Function Summary:** Calculates estimated remaining play hours to reach 99 in all skills based on current XP rates.

### 152. `time-tracking-reminder` (Time Tracking Reminder)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/queicherius/runelite-time-tracking-reminder](https://github.com/queicherius/runelite-time-tracking-reminder)
* **Last Updated on GitHub:** `23 days ago`
* **Function Summary:** Sidebar notification panel for farm patch growth, birdhouse traps, and kingdom favor.

### 153. `tool-required` (Tool Required)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Unmoon/tool-required](https://github.com/Unmoon/tool-required)
* **Last Updated on GitHub:** `2 months ago`
* **Function Summary:** Displays warning icons when attempting skilling or traversal activities without the required tool in inventory or toolbelt.

### 154. `turning-circles` (Turning Circles)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/anmcgrath/turning-circles](https://github.com/anmcgrath/turning-circles)
* **Last Updated on GitHub:** `7 months ago`
* **Function Summary:** Renders player turning radius circles to assist in diagonal movement pathing.

### 155. `unbalanced-trade-prevention` (Unbalanced Trade Prevention)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/TheStonedTurtle/unbalanced-trade-prevention](https://github.com/TheStonedTurtle/unbalanced-trade-prevention)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Warning pop-up when accepting trades with unbalanced GP value.

### 156. `unresponsive-cursor` (Unresponsive Cursor)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/bluelightzero/unresponsive-cursor](https://github.com/bluelightzero/unresponsive-cursor)
* **Last Updated on GitHub:** `5 years ago`
* **Function Summary:** Changes cursor icon when client is loading or unresponsive.

### 157. `valuable-drop-recolor` (Valuable Drop Recolor)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/Mafham/mafham-plugins](https://github.com/Mafham/mafham-plugins)
* **Last Updated on GitHub:** `2 years ago`
* **Function Summary:** Recolors ground item loot text based on GE market value tiers.

### 158. `visual-metronome` (Visual Metronome)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/vincent0955/Visual-metronome](https://github.com/vincent0955/Visual-metronome)
* **Last Updated on GitHub:** `28 days ago`
* **Function Summary:** Flashes screen borders or overhead tiles on exact game tick intervals (100 bpm / 0.6s).

### 159. `wasted-bank-space` (Wasted Bank Space)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/mcgeer/WastedBankSpace](https://github.com/mcgeer/WastedBankSpace)
* **Last Updated on GitHub:** `9 months ago`
* **Function Summary:** Identifies duplicate placeholder slots and unnecessary bank space waste.

### 160. `watson-clue-tracker` (Watson Clue Tracker)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/geheur/watson-master-clue-tracker](https://github.com/geheur/watson-master-clue-tracker)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Displays turn-in status for Easy, Medium, Hard, and Elite clues at Watson's house.

### 161. `what-pet-is-that-anyway` (What Pet Is That Anyway)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/sololegends/runelite-what-pet-is-that-anyway](https://github.com/sololegends/runelite-what-pet-is-that-anyway)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Displays pet names and drop sources when examining follower pets.

### 162. `wheresmyboat` (Wheresmyboat)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/ArchRBX/wheresmyboat](https://github.com/ArchRBX/wheresmyboat)
* **Last Updated on GitHub:** `26 days ago`
* **Function Summary:** Highlights your docked ship on the minimap and main game screen with a directional compass indicator.

### 163. `wikisync` (Wikisync)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/weirdgloop/WikiSync](https://github.com/weirdgloop/WikiSync)
* **Last Updated on GitHub:** `4 months ago`
* **Function Summary:** Synchronizes account quest status and skill levels with official OSRS Wiki account lookup.

### 164. `wom-utils` (Wom Utils)
* **Active Profiles:** All 8 Profiles (`default`, `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Skilling & Minigames`, `Wilderness`)
* **GitHub Repository:** [https://github.com/wise-old-man/wiseoldman-runelite-plugin](https://github.com/wise-old-man/wiseoldman-runelite-plugin)
* **Last Updated on GitHub:** `2 days ago`
* **Function Summary:** Integrates Wise Old Man clan XP competitions and member tracking into sidebar.

---

## ⚔️ 2. Shared PvM Combat Helper Group (38 Plugins)

### 1. `antifire-checker` (Antifire Checker)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/sariyamelody/antifire-checker](https://github.com/sariyamelody/antifire-checker)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Warning overlay when antifire or super antifire potion coverage expires during dragon fights.

### 2. `arceuus-timers` (Arceuus Timers)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/Mantic-says-hi/arceuus-timers](https://github.com/Mantic-says-hi/arceuus-timers)
* **Last Updated on GitHub:** `1 month ago`
* **Function Summary:** Timers for Arceuus spellbook buffs (Death Charge, Ward of Arceuus, Shadow Veil, Greater Corruption).

### 3. `attack-ranges` (Attack Ranges)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/tylerwgrass/attack-ranges](https://github.com/tylerwgrass/attack-ranges)
* **Last Updated on GitHub:** `6 days ago`
* **Function Summary:** Visual tile overlay displaying monster attack ranges, dragon fire breath ranges, and mage cast radii.

### 4. `auto-retaliate-warning` (Auto Retaliate Warning)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/ste-h/auto-retaliate-warning](https://github.com/ste-h/auto-retaliate-warning)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Warning indicator when Auto Retaliate is toggled OFF during dangerous combat encounters.

### 5. `autocast-utilities` (Autocast Utilities)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/jcarbelbide/autocasting](https://github.com/jcarbelbide/autocasting)
* **Last Updated on GitHub:** `11 months ago`
* **Function Summary:** Reminds you to re-select ancient/standard autocast spells after weapon switches.

### 6. `book-of-the-dead-reminder` (Book Of The Dead Reminder)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/jakevollkommer/book-of-the-dead-reminder](https://github.com/jakevollkommer/book-of-the-dead-reminder)
* **Last Updated on GitHub:** `7 months ago`
* **Function Summary:** Alerts you if Book of the Dead is missing from inventory when entering Chambers of Xeric or ToA.

### 7. `boss-health-indicators` (Boss Health Indicators)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/rugg0064/boss-health-indicators](https://github.com/rugg0064/boss-health-indicators)
* **Last Updated on GitHub:** `2 years ago`
* **Function Summary:** Enlarged boss health bar overlay displaying exact HP numbers, phase thresholds, and enrage timers.

### 8. `bracelet-reminder` (Bracelet Reminder)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/chocobo-s/Slaughter-bracelet-reminder](https://github.com/chocobo-s/Slaughter-bracelet-reminder)
* **Last Updated on GitHub:** `11 months ago`
* **Function Summary:** Notifies you when Bracelet of Slaughter or Expeditious Bracelet degrades to 0 charges.

### 9. `casket-saver` (Casket Saver)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/Notespeon/casket-saver](https://github.com/Notespeon/casket-saver)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Prevents opening clue caskets in dangerous Wilderness zones or full inventory scenarios.

### 10. `chugging-barrel` (Chugging Barrel)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/Syhlex/chugging-barrel](https://github.com/Syhlex/chugging-barrel)
* **Last Updated on GitHub:** `3 months ago`
* **Function Summary:** Tracks liquid barrel doses and automated potion consumption during long Slayer/boss trips.

### 11. `combat-achievements-tracker` (Combat Achievements Tracker)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/ehubbartt/combat-achievements-tracker](https://github.com/ehubbartt/combat-achievements-tracker)
* **Last Updated on GitHub:** `8 months ago`
* **Function Summary:** Displays Combat Achievement task progress, tier rewards, and boss task requirements.

### 12. `consumable-cooldowns` (Consumable Cooldowns)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/CopyPastaOSRS/consumable-cooldowns](https://github.com/CopyPastaOSRS/consumable-cooldowns)
* **Last Updated on GitHub:** `26 days ago`
* **Function Summary:** Displays food, brew, Karambwan, and potion eating cooldown timers on your player overhead.

### 13. `crab-solver` (Crab Solver)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/TheStonedTurtle/CrabSolver](https://github.com/TheStonedTurtle/CrabSolver)
* **Last Updated on GitHub:** `6 months ago`
* **Function Summary:** Solves elemental crab light beam puzzles in Chambers of Xeric and quest instances.

### 14. `deathindicator` (Deathindicator)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/Adam-/runelite-plugins](https://github.com/Adam-/runelite-plugins)
* **Last Updated on GitHub:** `6 years ago`
* **Function Summary:** Marks death location grave tiles and gravestone timer countdowns across Gielinor.

### 15. `delayed-healing` (Delayed Healing)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/DapperMickie/delayed-healing](https://github.com/DapperMickie/delayed-healing)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Calculates incoming tick delays for food, Karambwans, and potions during high-level PvM.

### 16. `dont-telegrab-npcs` (Dont Telegrab Npcs)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/ldavid432/dont-telekinetic-grab-npcs](https://github.com/ldavid432/dont-telekinetic-grab-npcs)
* **Last Updated on GitHub:** `8 days ago`
* **Function Summary:** Prevents accidental telegrab clicks on non-lootable monster entities.

### 17. `ectoplasmator-reminder` (Ectoplasmator Reminder)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/staytheknight/ectoplasmator-reminder](https://github.com/staytheknight/ectoplasmator-reminder)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Alerts you if Ectoplasmator is not equipped or charged when fighting ghost/aberrant tasks.

### 18. `emblem-trader-skull-timer` (Emblem Trader Skull Timer)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/Teekiz/skull-timer](https://github.com/Teekiz/skull-timer)
* **Last Updated on GitHub:** `4 months ago`
* **Function Summary:** Tracks Bounty Hunter / Emblem Trader skull timers in PvP zones.

### 19. `fight-cave-waves` (Fight Cave Waves)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/nightfirecat/plugin-hub-plugins](https://github.com/nightfirecat/plugin-hub-plugins)
* **Last Updated on GitHub:** `3 years ago`
* **Function Summary:** Displays incoming TzHaar Fight Cave wave spawns, monster types, and prayer priorities.

### 20. `godwars-protection-overlay` (Godwars Protection Overlay)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/UnExploration/godwars-prot](https://github.com/UnExploration/godwars-prot)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Displays God Wars Dungeon god protection status based on equipped gear (Zamorak, Saradomin, Bandos, Armadyl).

### 21. `lite-regen-meter` (Lite Regen Meter)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/Varietyz/literegenmeter](https://github.com/Varietyz/literegenmeter)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Overlay showing exact tick countdowns until HP and Prayer natural regen ticks trigger.

### 22. `lizardman-shaman-minion-alert` (Lizardman Shaman Minion Alert)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/baloooouu/lizardman-shaman-minion-alert](https://github.com/baloooouu/lizardman-shaman-minion-alert)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Audio and tile alert when Lizardman Shaman purple acid minions spawn.

### 23. `low-detail-raids` (Low Detail Raids)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/bepzi/runelite-plugins](https://github.com/bepzi/runelite-plugins)
* **Last Updated on GitHub:** `2 years ago`
* **Function Summary:** Simplifies floor textures and reduces visual clutter inside Raids dungeons to improve FPS.

### 24. `max-hit-calculator` (Max Hit Calculator)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/j-cob44/max-hit-calc](https://github.com/j-cob44/max-hit-calc)
* **Last Updated on GitHub:** `4 months ago`
* **Function Summary:** Calculates exact maximum hit for melee, ranged, and magic based on gear, prayers, and active boosts.

### 25. `menuhp` (Menuhp)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/AnkouOSRS/npc-menu-hp](https://github.com/AnkouOSRS/npc-menu-hp)
* **Last Updated on GitHub:** `8 months ago`
* **Function Summary:** Displays target HP numbers directly inside right-click menu options.

### 26. `monster-hp-percentage` (Monster Hp Percentage)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/lejeffe/MonsterHP](https://github.com/lejeffe/MonsterHP)
* **Last Updated on GitHub:** `26 days ago`
* **Function Summary:** Displays exact numerical HP percentage over monster hitbars and target overlays.

### 27. `poison-moo` (Poison Moo)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/remindful7560/OSRS-Plugins](https://github.com/remindful7560/OSRS-Plugins)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Custom audio cue and visual alert when taking poison or venom damage ticks.

### 28. `poison-ring` (Poison Ring)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/corhen/poison-ring](https://github.com/corhen/poison-ring)
* **Last Updated on GitHub:** `5 months ago`
* **Function Summary:** Tracks Ring of Suffering recoil charges and venom protection timers.

### 29. `poisoned-npcs` (Poisoned Npcs)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/tautges/runelite-poisoned-npcs-plugin](https://github.com/tautges/runelite-poisoned-npcs-plugin)
* **Last Updated on GitHub:** `2 years ago`
* **Function Summary:** Highlights poisoned or envenomed NPCs with color-coded damage overlays.

### 30. `prayer-regeneration-helper` (Prayer Regeneration Helper)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/Supalosa/prayer-regeneration-timer](https://github.com/Supalosa/prayer-regeneration-timer)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Tracks prayer potion restoration efficiency and prayer point drain rates per minute.

### 31. `ring-of-recoil-notifier` (Ring Of Recoil Notifier)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/delps1001/recoil-plugin](https://github.com/delps1001/recoil-plugin)
* **Last Updated on GitHub:** `5 years ago`
* **Function Summary:** Alerts you when Ring of Recoil breaks or reaches low charges.

### 32. `skull-notifier` (Skull Notifier)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/Trevor159/runelite-external-plugins](https://github.com/Trevor159/runelite-external-plugins)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Screen edge alert and warning when entering Wilderness zones or holding skulling items.

### 33. `spec-regen-timer` (Spec Regen Timer)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/Bram91/SpecRegenTimerPlugin](https://github.com/Bram91/SpecRegenTimerPlugin)
* **Last Updated on GitHub:** `2 months ago`
* **Function Summary:** Displays exact tick timer until the next 10% special attack energy regen occurs.

### 34. `thrall-helper` (Thrall Helper)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/PortAGuy/thrall-helper](https://github.com/PortAGuy/thrall-helper)
* **Last Updated on GitHub:** `3 months ago`
* **Function Summary:** Overlay and audio alert reminding you to re-summon thralls before they despawn during combat.

### 35. `timers-ca` (Timers Ca)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/PaJauKat/Timers-CA](https://github.com/PaJauKat/Timers-CA)
* **Last Updated on GitHub:** `13 days ago`
* **Function Summary:** Combat Achievement challenge speedrun timers.

### 36. `tzhaar-hp-tracker` (Tzhaar Hp Tracker)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/bopsec/buchus-plugins](https://github.com/bopsec/buchus-plugins)
* **Last Updated on GitHub:** `2 months ago`
* **Function Summary:** Tracks total wave HP and remaining mob counts in Fight Caves and Inferno.

### 37. `unpotted-reminder` (Unpotted Reminder)
* **Active Profiles:** `Slayer`, `Bossing`, `Raids - ToA`, `Raids - CoX`, `Raids - ToB`, `Wilderness`
* **GitHub Repository:** [https://github.com/AnkouOSRS/unpotted-reminder](https://github.com/AnkouOSRS/unpotted-reminder)
* **Last Updated on GitHub:** `2 years ago`
* **Function Summary:** Alerts you when combat boosts (Super combat, Ranging potion) drop back to base stats during bossing.

---

## 🐉 3. Bossing Profile Exclusives (`Bossing-5.properties` - 6 Plugins)

### 1. `barrows-door-highlighter` (Barrows Door Highlighter)
* **Active Profiles:** `Bossing`
* **GitHub Repository:** [https://github.com/hansjm10/Barrows-Door-Highlighter](https://github.com/hansjm10/Barrows-Door-Highlighter)
* **Last Updated on GitHub:** `4 months ago`
* **Function Summary:** Highlights unlocked doors and solves the puzzle door in the Barrows catacombs.

### 2. `gauntlet-crafting` (Gauntlet Crafting)
* **Active Profiles:** `Bossing`
* **GitHub Repository:** [https://github.com/trs/runelite-gauntlet-crafting](https://github.com/trs/runelite-gauntlet-crafting)
* **Last Updated on GitHub:** `14 days ago`
* **Function Summary:** Highlights 2D interface crafting buttons at the crafting bowl to prevent accidental armor/weapon upgrade mistakes.

### 3. `hunllef-helper` (Hunllef Helper)
* **Active Profiles:** `Bossing`
* **GitHub Repository:** [https://github.com/Loze-Put/hunllef-helper](https://github.com/Loze-Put/hunllef-helper)
* **Last Updated on GitHub:** `7 months ago`
* **Function Summary:** Audio tick counter and prayer switcher callout for Corrupted Hunllef in the Gauntlet.

### 4. `the-gauntlet` (The Gauntlet)
* **Active Profiles:** `Bossing`
* **GitHub Repository:** [https://github.com/LlemonDuck/the-gauntlet](https://github.com/LlemonDuck/the-gauntlet)
* **Last Updated on GitHub:** `14 days ago`
* **Function Summary:** 3D maze resource node outlines, crafting requirements tracker, and boss attack timer overlay for the Gauntlet.

### 5. `vorkath-run-warning` (Vorkath Run Warning)
* **Active Profiles:** `Bossing`
* **GitHub Repository:** [https://github.com/jkvlntn/vorkath-run-warning](https://github.com/jkvlntn/vorkath-run-warning)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Audio and visual warning when Vorkath launches high-damage fireball projectile.

### 6. `zulrah-helper` (Zulrah Helper)
* **Active Profiles:** `Bossing`
* **GitHub Repository:** [https://github.com/while-loop/runelite-plugins](https://github.com/while-loop/runelite-plugins)
* **Last Updated on GitHub:** `1 month ago`
* **Function Summary:** Interactive Zulrah rotation guide displaying phase colors, prayer recommendations, and safe tiles.

---

## 🏹 4. Slayer Profile Exclusives (`Slayer-1.properties` - 1 Plugin)

### 1. `slayer-boosting` (Slayer Boosting)
* **Active Profiles:** `Bossing`, `Raids`, `Raids`, `Raids`, `Skilling & Minigames`, `Slayer`, `Wilderness`
* **GitHub Repository:** [https://github.com/TheInsomnolent/slayer-boosting](https://github.com/TheInsomnolent/slayer-boosting)
* **Last Updated on GitHub:** `3 months ago`
* **Function Summary:** Calculates optimal Slayer boost thresholds and reminds you which Slayer master to use for milestone tasks.

---

## 🏺 5. Raids Profile Exclusives

## Tombs of Amascut (`Raids - ToA-2.properties` - 3 Plugins)

### 1. `toa-gear-check` (Toa Gear Check)
* **Active Profiles:** `Raids`
* **GitHub Repository:** [https://github.com/Need-Femboy/ToAGearCheck](https://github.com/Need-Femboy/ToAGearCheck)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Verifies team gear loadouts and missing required items before starting ToA raids.

### 2. `toa-points-tracker` (Toa Points Tracker)
* **Active Profiles:** `Raids`
* **GitHub Repository:** [https://github.com/AbusiveTuna/ToA_Points](https://github.com/AbusiveTuna/ToA_Points)
* **Last Updated on GitHub:** `2 years ago`
* **Function Summary:** Calculates real-time raid points and estimated purple drop chance (including Warden P2 & Zebak).

### 3. `tombs-of-amascut` (Tombs Of Amascut)
* **Active Profiles:** `Raids`
* **GitHub Repository:** [https://github.com/LlemonDuck/tombs-of-amascut](https://github.com/LlemonDuck/tombs-of-amascut)
* **Last Updated on GitHub:** `2 months ago`
* **Function Summary:** Full ToA invocation manager, puzzle solvers (Akkha light, Kephri puzzle), and boss phase overlays.

## Chambers of Xeric (`Raids - CoX-3.properties` - 3 Plugins)

### 1. `cox-additions` (Cox Additions)
* **Active Profiles:** `Raids`
* **GitHub Repository:** [https://github.com/dey0/pluginhub-plugins](https://github.com/dey0/pluginhub-plugins)
* **Last Updated on GitHub:** `4 months ago`
* **Function Summary:** Speedrun split timer for Chambers of Xeric rooms, floors, and Olm phase times.

### 2. `cox-qol` (Cox Qol)
* **Active Profiles:** `Raids`
* **GitHub Repository:** [https://github.com/MoreBuchus/buchus-plugins](https://github.com/MoreBuchus/buchus-plugins)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Chambers of Xeric QoL enhancements including ice demon, tightrope, and Muttadile puzzle solvers.

### 3. `raid-points-overlay` (Raid Points Overlay)
* **Active Profiles:** `Raids`
* **GitHub Repository:** [https://github.com/Trevor159/runelite-external-plugins](https://github.com/Trevor159/runelite-external-plugins)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Displays personal and team point totals inside CoX dungeons.

## Theatre of Blood (`Raids - ToB-4.properties` - 7 Plugins)

### 1. `nylo-death-indicators` (Nylo Death Indicators)
* **Active Profiles:** `Raids`
* **GitHub Repository:** [https://github.com/InfernoStats/Nylo-Death-Indicators](https://github.com/InfernoStats/Nylo-Death-Indicators)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Instantly hides Nylocas death animations to improve wave visibility.

### 2. `nyloer` (Nyloer)
* **Active Profiles:** `Raids`
* **GitHub Repository:** [https://github.com/EIKOOT/nyloer](https://github.com/EIKOOT/nyloer)
* **Last Updated on GitHub:** `3 months ago`
* **Function Summary:** Displays Nylocas wave spawn order, pillar health, and aggressive wave callouts in ToB.

### 3. `tob-drop-chance` (Tob Drop Chance)
* **Active Profiles:** `Raids`
* **GitHub Repository:** [https://github.com/Adam-/runelite-plugins](https://github.com/Adam-/runelite-plugins)
* **Last Updated on GitHub:** `4 years ago`
* **Function Summary:** Calculates unique purple drop chances based on team deaths and points in ToB.

### 4. `tob-gear-checker` (Tob Gear Checker)
* **Active Profiles:** `Raids`
* **GitHub Repository:** [https://github.com/ArtsicleOfficial/tob-gear-checker](https://github.com/ArtsicleOfficial/tob-gear-checker)
* **Last Updated on GitHub:** `4 years ago`
* **Function Summary:** Verifies team inventory and gear loadouts before entering Theatre of Blood.

### 5. `tob-light-colors` (Tob Light Colors)
* **Active Profiles:** `Raids`
* **GitHub Repository:** [https://github.com/Maurits825/tob-light-colors](https://github.com/Maurits825/tob-light-colors)
* **Last Updated on GitHub:** `4 years ago`
* **Function Summary:** Customizes final reward chest light beam colors in ToB loot room.

### 6. `tob-notification` (Tob Notification)
* **Active Profiles:** `Raids`
* **GitHub Repository:** [https://github.com/jlee513/tob-notification](https://github.com/jlee513/tob-notification)
* **Last Updated on GitHub:** `2 years ago`
* **Function Summary:** Flashes a full-screen alert for dangerous ToB mechanics even when chatbox is minimized.

### 7. `tobqol` (Tobqol)
* **Active Profiles:** `Raids`
* **GitHub Repository:** [https://github.com/damencs/tob-qol](https://github.com/damencs/tob-qol)
* **Last Updated on GitHub:** `1 month ago`
* **Function Summary:** Theatre of Blood mechanics overlays including Maiden blood spawns, Bloat walk timer, and Xarpus turns.

---

## 🔨 6. Skilling & Minigames Exclusives (`Skilling & Minigames-6.properties` - 63 Plugins)

### 1. `abc-alch` (Abc Alch)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/vartan/abc-alch](https://github.com/vartan/abc-alch)
* **Last Updated on GitHub:** `3 months ago`
* **Function Summary:** Calculates profit margins and optimal alch timers for alch-agility training.

### 2. `aerial-fishing-pearl-luck` (Aerial Fishing Pearl Luck)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/H4waiianPunch/Pearl-Luck-Tracker](https://github.com/H4waiianPunch/Pearl-Luck-Tracker)
* **Last Updated on GitHub:** `11 months ago`
* **Function Summary:** Tracks Molch pearl drop rates and fish catch statistics during aerial fishing.

### 3. `afk-marks-canafis` (Afk Marks Canafis)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/powerus117/RLAfkMarksCanafis](https://github.com/powerus117/RLAfkMarksCanafis)
* **Last Updated on GitHub:** `5 months ago`
* **Function Summary:** Tracks 3-minute Mark of Grace spawn cooldown timer during agility runs.

### 4. `ardougne-cooldown-timer` (Ardougne Cooldown Timer)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/coopermor/ardougne-cooldown-timer](https://github.com/coopermor/ardougne-cooldown-timer)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Tracks Ardougne lever teleport cooldowns and Thieving stun timers.

### 5. `avgseplaptime` (Avgseplaptime)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/spookirs/average-sep-lap](https://github.com/spookirs/average-sep-lap)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Lap timer and obstacle split tracker for Hallowed Sepulchre Agility.

### 6. `ba-call-highlight` (Ba Call Highlight)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/rugg0064/ba-call-highlight](https://github.com/rugg0064/ba-call-highlight)
* **Last Updated on GitHub:** `3 years ago`
* **Function Summary:** Highlights correct horn calls in Barbarian Assault.

### 7. `ba-minigame` (Ba Minigame)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/SkylerPIlot/Ba-Minigame](https://github.com/SkylerPIlot/Ba-Minigame)
* **Last Updated on GitHub:** `3 months ago`
* **Function Summary:** Barbarian Assault callout timers, role guides, runner wave pathing, and egg collector overlays.

### 8. `barrows-potential` (Barrows Potential)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/Godofdrakes/barrows-potential](https://github.com/Godofdrakes/barrows-potential)
* **Last Updated on GitHub:** `4 months ago`
* **Function Summary:** Calculates exact Barrows chest reward potential percentage based on monster kills.

### 9. `bone-shard-helper` (Bone Shard Helper)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/CarelessEsper/Bone-Shard-Helper](https://github.com/CarelessEsper/Bone-Shard-Helper)
* **Last Updated on GitHub:** `5 months ago`
* **Function Summary:** Calculates bone shard prayer XP gains at the Blessed Sunfire Wine altar.

### 10. `butler` (Butler)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/AltarOSRS/butler-info-plugin](https://github.com/AltarOSRS/butler-info-plugin)
* **Last Updated on GitHub:** `3 months ago`
* **Function Summary:** One-click Demon Butler plank/brick fetch swapper for POH Construction training.

### 11. `cam-torum-mining` (Cam Torum Mining)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/cwjoshuak/cam-torum-mining](https://github.com/cwjoshuak/cam-torum-mining)
* **Last Updated on GitHub:** `2 years ago`
* **Function Summary:** Calcified deposit mining timers and bone shard yield calculator in Cam Torum.

### 12. `camdozaal-fishing-helper` (Camdozaal Fishing Helper)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/ConorJS/CamdozaalFishingHelper](https://github.com/ConorJS/CamdozaalFishingHelper)
* **Last Updated on GitHub:** `2 years ago`
* **Function Summary:** Barronite deposit mining and fishing luck overlays in Below Ice Mountain ruins.

### 13. `castle-war-afk` (Castle War Afk)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/Togtja/castle_war_afk](https://github.com/Togtja/castle_war_afk)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Activity meter warnings and flag capture overlays in Castle Wars.

### 14. `castlewarsindicators` (Castlewarsindicators)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/marvinb16/Castle-Wars-Indicators](https://github.com/marvinb16/Castle-Wars-Indicators)
* **Last Updated on GitHub:** `8 months ago`
* **Function Summary:** Displays team scores, bandage cabinet supplies, and door health bars in Castle Wars.

### 15. `chompy-hunter` (Chompy Hunter)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/PJGJ210/chompy-hunter](https://github.com/PJGJ210/chompy-hunter)
* **Last Updated on GitHub:** `7 months ago`
* **Function Summary:** Tracks total Chompy bird kills, swamp toad inflation, and Chompy bird hat tiers.

### 16. `compost-helper` (Compost Helper)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/PidgeBirb/compost-helper](https://github.com/PidgeBirb/compost-helper)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Compost bucket fill state and ultracompost creation calculator.

### 17. `easy-arceuus-runecrafting` (Easy Arceuus Runecrafting)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/poi56iop/easy-arceuus-runecrafting](https://github.com/poi56iop/easy-arceuus-runecrafting)
* **Last Updated on GitHub:** `2 years ago`
* **Function Summary:** Dense runestone mining timers, dark altar pathing, and essence block chipping helpers.

### 18. `easy-giantsfoundry` (Easy Giantsfoundry)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/Toofifty/easy-giantsfoundry](https://github.com/Toofifty/easy-giantsfoundry)
* **Last Updated on GitHub:** `11 months ago`
* **Function Summary:** Displays temperature gauge zone thresholds, mold scores, and weapon quality in Giants Foundry.

### 19. `farming-guild-overview` (Farming Guild Overview)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/wouterrutgers/farming-guild-overview](https://github.com/wouterrutgers/farming-guild-overview)
* **Last Updated on GitHub:** `11 months ago`
* **Function Summary:** Displays contract tier requirements, patch readiness, and seed vault inventory.

### 20. `forestry-banking-helper` (Forestry Banking Helper)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/Nuktukk/forestry-banking-helper](https://github.com/Nuktukk/forestry-banking-helper)
* **Last Updated on GitHub:** `2 months ago`
* **Function Summary:** Forestry event reward shop interface and item converter helper.

### 21. `forestry-spawn-helper` (Forestry Spawn Helper)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/Oelderoth/forestry-force-spawn-plugin](https://github.com/Oelderoth/forestry-force-spawn-plugin)
* **Last Updated on GitHub:** `3 months ago`
* **Function Summary:** Alerts and location markers for Forestry events (Rising Roots, Friendly Pheasant, Poachers, Flowering Bush).

### 22. `gnome-restaurant` (Gnome Restaurant)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/hex-agon/gnome-restaurant](https://github.com/hex-agon/gnome-restaurant)
* **Last Updated on GitHub:** `2 months ago`
* **Function Summary:** Gnome Restaurant delivery NPC locations, food recipes, and token rewards.

### 23. `great-guardian-hider` (Great Guardian Hider)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/horse4lunch/Great-Guardian-Hider](https://github.com/horse4lunch/Great-Guardian-Hider)
* **Last Updated on GitHub:** `3 years ago`
* **Function Summary:** Hides Great Guardian entity in GOTR to reduce click misdirection.

### 24. `guardians-of-the-rift-helper` (Guardians Of The Rift Helper)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/DatBear/Guardians-of-the-Rift-Helper](https://github.com/DatBear/Guardians-of-the-Rift-Helper)
* **Last Updated on GitHub:** `1 month ago`
* **Function Summary:** Portal timers, rift percentage, cell tiers, and active altar indicators in GOTR.

### 25. `herbi-afk` (Herbi Afk)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/Maurits825/herbi-afk](https://github.com/Maurits825/herbi-afk)
* **Last Updated on GitHub:** `1 month ago`
* **Function Summary:** Herbiboar tracking path highlights and herb harvest yield overlays.

### 26. `home-improvement` (Home Improvement)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/Mike-U5/rl-plugin-home-improvement](https://github.com/Mike-U5/rl-plugin-home-improvement)
* **Last Updated on GitHub:** `2 years ago`
* **Function Summary:** POH construction building guide and plank requirement calculator.

### 27. `hunter-rumours` (Hunter Rumours)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/geel9/runelite-hunter-rumours](https://github.com/geel9/runelite-hunter-rumours)
* **Last Updated on GitHub:** `26 days ago`
* **Function Summary:** Guild Hunter rumour master assignments, animal location maps, and rare part drop rates.

### 28. `improved-tears-of-guthix-interface` (Improved Tears Of Guthix Interface)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/Cyborger1/improved-tears-of-guthix-interface](https://github.com/Cyborger1/improved-tears-of-guthix-interface)
* **Last Updated on GitHub:** `16 days ago`
* **Function Summary:** Clean UI overlay for Tears of Guthix point collection.

### 29. `log-basket` (Log Basket)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/aidanmastro/log-basket-plugin](https://github.com/aidanmastro/log-basket-plugin)
* **Last Updated on GitHub:** `1 month ago`
* **Function Summary:** Displays log counts and tree species stored inside the Forester's Log Basket.

### 30. `log-basket-swapper` (Log Basket Swapper)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/VicSegers/log-basket-swapper](https://github.com/VicSegers/log-basket-swapper)
* **Last Updated on GitHub:** `5 months ago`
* **Function Summary:** One-click deposit/fill menu entry swapper for Forester's Log Basket.

### 31. `lunar-chest-value` (Lunar Chest Value)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/bradur/lunar-chest-value](https://github.com/bradur/lunar-chest-value)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Calculates loot value from Perilous Moons Lunar Chest.

### 32. `mahogany-homes` (Mahogany Homes)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/TheStonedTurtle/Mahogany-Homes](https://github.com/TheStonedTurtle/Mahogany-Homes)
* **Last Updated on GitHub:** `7 months ago`
* **Function Summary:** Highlights contract NPCs, required materials, furniture repair locations, and optimal teleports.

### 33. `mastering-mixology` (Mastering Mixology)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/hex-agon/mastering-mixology](https://github.com/hex-agon/mastering-mixology)
* **Last Updated on GitHub:** `6 months ago`
* **Function Summary:** Potion recipe mixer guide, paste storage counters, and order fulfillments in Varlamore Mixology.

### 34. `nmz-optimal-points` (Nmz Optimal Points)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/bloogeyz/nmz-optimal-points](https://github.com/bloogeyz/nmz-optimal-points)
* **Last Updated on GitHub:** `4 years ago`
* **Function Summary:** Calculates optimal boss selection for max NMZ points per hour.

### 35. `pickpocket-helper` (Pickpocket Helper)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/pajlads/runelite-pickpocket-helper](https://github.com/pajlads/runelite-pickpocket-helper)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Tracks thieving success rates, pouch counts, and stunned state timers during pickpocketing.

### 36. `plank-sack` (Plank Sack)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/Talkarcabbage/planksacktracker](https://github.com/Talkarcabbage/planksacktracker)
* **Last Updated on GitHub:** `7 months ago`
* **Function Summary:** Displays plank counts (Oak, Teak, Mahogany) stored inside Plank Sack.

### 37. `poh-treasure-chest-ge-value` (Poh Treasure Chest Ge Value)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/nicDamours/POHTreasureChestGEValue](https://github.com/nicDamours/POHTreasureChestGEValue)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Calculates GE market value of cosmetics stored in POH Treasure Chest.

### 38. `razor-kebbit-tracking` (Razor Kebbit Tracking)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/cwjoshuak/razor-backed-kebbits](https://github.com/cwjoshuak/razor-backed-kebbits)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Razor-backed kebbit tracking trail highlights and fur yield counters.

### 39. `rc-pouch-usage` (Rc Pouch Usage)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/DavidVentura/rc-pouch-alert](https://github.com/DavidVentura/rc-pouch-alert)
* **Last Updated on GitHub:** `3 years ago`
* **Function Summary:** Tracks essence pouch capacity and alerts you before pouches degrade.

### 40. `shade-chests` (Shade Chests)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/eemkukko/shade-chests](https://github.com/eemkukko/shade-chests)
* **Last Updated on GitHub:** `2 years ago`
* **Function Summary:** Shades of Mort'ton sanctuary chest key requirements, pyre log tiers, and gold lockbox rewards.

### 41. `slayer-boosting` (Slayer Boosting)
* **Active Profiles:** `Bossing`, `Raids`, `Raids`, `Raids`, `Skilling & Minigames`, `Slayer`, `Wilderness`
* **GitHub Repository:** [https://github.com/TheInsomnolent/slayer-boosting](https://github.com/TheInsomnolent/slayer-boosting)
* **Last Updated on GitHub:** `3 months ago`
* **Function Summary:** Calculates optimal Slayer boost thresholds and reminds you which Slayer master to use for milestone tasks.

### 42. `soul-wars` (Soul Wars)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/Lucidare/soul-wars](https://github.com/Lucidare/soul-wars)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Avatar health bars, soul fragment counters, and graveyard capture timers in Soul Wars.

### 43. `startierindicator` (Startierindicator)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/pwatts6060/runelite-plugins](https://github.com/pwatts6060/runelite-plugins)
* **Last Updated on GitHub:** `2 months ago`
* **Function Summary:** Displays Shooting Star tier levels, miner counts, and star mining XP rates.

### 44. `stealing-artefacts` (Stealing Artefacts)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/pajlads/StealingArtefacts](https://github.com/pajlads/StealingArtefacts)
* **Last Updated on GitHub:** `4 months ago`
* **Function Summary:** Guard vision cones, artefact turn-in routes, and Captain Guide location overlay in Piscarilius.

### 45. `tempoross` (Tempoross)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/nmlynch94/runelite-external-plugins](https://github.com/nmlynch94/runelite-external-plugins)
* **Last Updated on GitHub:** `8 months ago`
* **Function Summary:** Displays Tempoross wave alerts, fires, fish essence count, and double spot highlights.

### 46. `tictac7x-motherlode` (Tictac7x Motherlode)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/TicTac7x/runelite-plugins](https://github.com/TicTac7x/runelite-plugins)
* **Last Updated on GitHub:** `20 days ago`
* **Function Summary:** Sack capacity counter, pay-dirt vein respawn timers, and hopper status in Motherlode Mine.

### 47. `tictac7x-rooftops` (Tictac7x Rooftops)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/TicTac7x/runelite-plugins](https://github.com/TicTac7x/runelite-plugins)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Clickable obstacle highlights and Mark of Grace badges for all Rooftop Agility courses.

### 48. `tictac7x-sulliuscep` (Tictac7x Sulliuscep)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/TicTac7x/runelite-plugins](https://github.com/TicTac7x/runelite-plugins)
* **Last Updated on GitHub:** `3 years ago`
* **Function Summary:** Sulliuscep mushroom chopping guide, tar monster alerts, and numulite node highlights.

### 49. `tictac7x-tithe` (Tictac7x Tithe)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/TicTac7x/runelite-plugins](https://github.com/TicTac7x/runelite-plugins)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Plant watering timers, fruit count, and patch rotation order overlay for Tithe Farm.

### 50. `tog-indicator` (Tog Indicator)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/LlemonDuck/tog-indicator](https://github.com/LlemonDuck/tog-indicator)
* **Last Updated on GitHub:** `6 months ago`
* **Function Summary:** Highlights blue tears, green tears, and countdown timers in Tears of Guthix.

### 51. `totem-fletching` (Totem Fletching)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/TheRealGuru/totem-fletching](https://github.com/TheRealGuru/totem-fletching)
* **Last Updated on GitHub:** `8 months ago`
* **Function Summary:** Fletching guide and material tracker for island totem carving.

### 52. `tree-despawn-timer` (Tree Despawn Timer)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/CreativeTechGuy/tree-despawn-timer](https://github.com/CreativeTechGuy/tree-despawn-timer)
* **Last Updated on GitHub:** `1 month ago`
* **Function Summary:** Displays exact woodcutting tree despawn timers and chop tick cycles.

### 53. `treecount` (Treecount)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/Infinitay/tree-count-plugin](https://github.com/Infinitay/tree-count-plugin)
* **Last Updated on GitHub:** `8 months ago`
* **Function Summary:** Tracks active woodcutters on trees to calculate Forestry chop bonuses.

### 54. `trouble-brewing` (Trouble Brewing)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/Biffo89/Trouble-Brewing](https://github.com/Biffo89/Trouble-Brewing)
* **Last Updated on GitHub:** `29 days ago`
* **Function Summary:** Minigame recipe helper, rum batch count, and ingredient bucket trackers for Trouble Brewing.

### 55. `ultimate-vm` (Ultimate Vm)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/rtaylor4444/UltimateVolcanicMine](https://github.com/rtaylor4444/UltimateVolcanicMine)
* **Last Updated on GitHub:** `9 days ago`
* **Function Summary:** Volcanic Mine stability meter, vent status, platform eruption timers, and boulder movement guide.

### 56. `underwateragility` (Underwateragility)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/coopermor/underwateragility](https://github.com/coopermor/underwateragility)
* **Last Updated on GitHub:** `9 months ago`
* **Function Summary:** Oxygen meter timers, mermaid tear locations, and obstacle highlights for Fossil Island underwater agility.

### 57. `varlamore-house-thieving` (Varlamore House Thieving)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/sololegends/runelite-varlamore-house-thieving](https://github.com/sololegends/runelite-varlamore-house-thieving)
* **Last Updated on GitHub:** `9 months ago`
* **Function Summary:** Highlights wealthy citizen keys, distraction NPCs, and house thieving chests in Varlamore.

### 58. `wintertodt-notifications` (Wintertodt Notifications)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/jodelahithit/runelite-plugins](https://github.com/jodelahithit/runelite-plugins)
* **Last Updated on GitHub:** `4 years ago`
* **Function Summary:** Audio and screen flash alerts for cold damage ticks and snowfall hazards.

### 59. `wintertodt-solo-helper` (Wintertodt Solo Helper)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/aquaosrs/wintertodt-solo-helper](https://github.com/aquaosrs/wintertodt-solo-helper)
* **Last Updated on GitHub:** `3 years ago`
* **Function Summary:** Tracks Wintertodt health, warm clothing tier, and optimal pyromancer heal timing for solos.

### 60. `zmi` (Zmi)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/Rubueno/zmi](https://github.com/Rubueno/zmi)
* **Last Updated on GitHub:** `2 years ago`
* **Function Summary:** Ourania Altar Runecrafting pathing, Banker fee swapper, and Enfeeble cast reminders.

### 61. `zom-afk-gotr` (Zom Afk Gotr)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/JZomDev/zom-external-plugins](https://github.com/JZomDev/zom-external-plugins)
* **Last Updated on GitHub:** `2 months ago`
* **Function Summary:** AFK timer alerts and altar rotation reminders for Guardians of the Rift.

### 62. `zom-dense-essence` (Zom Dense Essence)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/JZomDev/zom-external-plugins](https://github.com/JZomDev/zom-external-plugins)
* **Last Updated on GitHub:** `2 years ago`
* **Function Summary:** Dense essence block mining and dark altar runecrafting efficiency helper.

### 63. `zom-nmz-util` (Zom Nmz Util)
* **Active Profiles:** `Skilling & Minigames`
* **GitHub Repository:** [https://github.com/redrumze/zom-external-plugins](https://github.com/redrumze/zom-external-plugins)
* **Last Updated on GitHub:** `5 years ago`
* **Function Summary:** Nightmare Zone dream points counter, power-up spawn highlights (Zapper, Ultimate Force), and absorption prayer swapper.

---

## 💀 7. Wilderness & PvP Exclusives (`Wilderness-8.properties` - 12 Plugins)

### 1. `looting-bag-value` (Looting Bag Value)
* **Active Profiles:** `Wilderness`
* **GitHub Repository:** [https://github.com/pwatts6060/runelite-plugins](https://github.com/pwatts6060/runelite-plugins)
* **Last Updated on GitHub:** `6 months ago`
* **Function Summary:** Calculates total GE market value of items stored inside your Looting Bag.

### 2. `protect-item-notifier` (Protect Item Notifier)
* **Active Profiles:** `Wilderness`
* **GitHub Repository:** [https://github.com/cubeee/protect-item-notify](https://github.com/cubeee/protect-item-notify)
* **Last Updated on GitHub:** `1 month ago`
* **Function Summary:** Flashes warning overlay if Protect Item prayer is toggled OFF while carrying valuable gear in Wilderness.

### 3. `rogues-chest` (Rogues Chest)
* **Active Profiles:** `Wilderness`
* **GitHub Repository:** [https://github.com/pwatts6060/runelite-plugins](https://github.com/pwatts6060/runelite-plugins)
* **Last Updated on GitHub:** `2 years ago`
* **Function Summary:** Chest unlock timers, rogue spawn alerts, and loot tracker for Wilderness Rogues' Chest.

### 4. `skull-prevention-reminder` (Skull Prevention Reminder)
* **Active Profiles:** `Wilderness`
* **GitHub Repository:** [https://github.com/lostcoastwizard/skull-prevention-reminder](https://github.com/lostcoastwizard/skull-prevention-reminder)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Alerts you if Player Attack Options are set to 'Always Right-Click' or 'Left-Click' in Wilderness.

### 5. `trouver-parchment-alerts` (Trouver Parchment Alerts)
* **Active Profiles:** `Wilderness`
* **GitHub Repository:** [https://github.com/zlight97/runelite-plugins](https://github.com/zlight97/runelite-plugins)
* **Last Updated on GitHub:** `6 months ago`
* **Function Summary:** Warning overlay if untradeable gear (Fire cape, Torso, Defender) lacks Trouver Parchment protection in Wilderness.

### 6. `wilderness-boss-peek` (Wilderness Boss Peek)
* **Active Profiles:** `Wilderness`
* **GitHub Repository:** [https://github.com/pwatts6060/runelite-plugins](https://github.com/pwatts6060/runelite-plugins)
* **Last Updated on GitHub:** `3 years ago`
* **Function Summary:** Peeks inside Wilderness boss caves (Venenatis, Vet'ion, Callisto) to report active player counts.

### 7. `wilderness-course-ticket-reminder` (Wilderness Course Ticket Reminder)
* **Active Profiles:** `Wilderness`
* **GitHub Repository:** [https://github.com/neafey/Wilderness-course-ticket-reminder](https://github.com/neafey/Wilderness-course-ticket-reminder)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Alerts you if Wilderness Agility course ticket fee is uncollected or missing.

### 8. `wilderness-map-locations` (Wilderness Map Locations)
* **Active Profiles:** `Wilderness`
* **GitHub Repository:** [https://github.com/DapperMickie/wilderness-map-locations](https://github.com/DapperMickie/wilderness-map-locations)
* **Last Updated on GitHub:** `1 year ago`
* **Function Summary:** Displays Wilderness obelisks, chaos temples, lever destinations, and KBD lair entrances on map.

### 9. `wilderness-multi-lines` (Wilderness Multi Lines)
* **Active Profiles:** `Wilderness`
* **GitHub Repository:** [https://github.com/Nightfirecat/plugin-hub-plugins](https://github.com/Nightfirecat/plugin-hub-plugins)
* **Last Updated on GitHub:** `7 months ago`
* **Function Summary:** Draws clear tile lines on screen demarcating single-combat and multi-combat Wilderness zones.

### 10. `wilderness-player-alarm` (Wilderness Player Alarm)
* **Active Profiles:** `Wilderness`
* **GitHub Repository:** [https://github.com/adhansen/plugin-repo](https://github.com/adhansen/plugin-repo)
* **Last Updated on GitHub:** `2 months ago`
* **Function Summary:** Flashes screen edges in bright red whenever an enemy player enters your render distance in the Wilderness.

### 11. `wilderness-teleports` (Wilderness Teleports)
* **Active Profiles:** `Wilderness`
* **GitHub Repository:** [https://github.com/nightfirecat/plugin-hub-plugins](https://github.com/nightfirecat/plugin-hub-plugins)
* **Last Updated on GitHub:** `3 years ago`
* **Function Summary:** Displays quick-teleport options and level 20/30 Wilderness depth boundaries.

### 12. `wilderness-warnings` (Wilderness Warnings)
* **Active Profiles:** `Wilderness`
* **GitHub Repository:** [https://github.com/LuxOG/wildernesswarnings](https://github.com/LuxOG/wildernesswarnings)
* **Last Updated on GitHub:** `1 day ago`
* **Function Summary:** Warning overlay when crossing Wilderness ditch or entering dangerous PvP portals.

