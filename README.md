# IF1210 - Dasar Pemrograman 2024
> Tugas Besar - IF1210 Dasar Pemrograman 2024

## About
> This project is a text-based game that allows users to engage in various activities such as registering, logging in, managing inventory, battling monsters, shopping, and more. The game is designed to provide an engaging and interactive experience through a command-line interface. Players can assume the role of an "agent" to explore and participate in different game modes or act as an "admin" to manage game data.

## Contributors
- Varel Tiara/19623183
- Frederiko Eldad Mugiyono/19623073
- Fahrian Maulana Fazry Nuriady/16523223
- Timothy Marvine/19623273
- Nakeisha Valya Shakila/19623133

## Features
> ### User Management
- **Register**: Allows new users to create an account and receive an initial monster.
- **Login**: Existing users can log in to access their account and game progress.
- **Logout**: Users can log out of their account.

> ### Game Modes
- **Inventory**: View and manage the user's inventory, including monsters and items.
- **Shop**: Purchase items or manage the shop depending on the user's role (agent or admin).
- **Laboratory**: Manage and enhance monsters in the laboratory.
- **Battle**: Engage in battles against other monsters.
- **Arena**: Participate in arena battles across multiple stages to earn rewards.

> ### Admin Features
- **Monster Management**: Admins can manage and update monster data.
- **Shop Management**: Admins can manage items and monsters available in the shop.

> ### Additional Features
- **Help**: Provides information on available commands and how to use them.
- **Jackpot**: A chance-based game where users can try their luck to win rewards.
- **Save**: Save the current game state to preserve progress.
- **Exit**: Exit the game and save the current state.

> ### Data Management
- **Loading and Saving**: Automatically load data from CSV files at the start and save data upon exiting or manually saving.
- **Inventory Management**: Track and update inventory items and monsters for each user.
- **Currency Management**: Handle in-game currency transactions for purchasing items and rewards.

## How to Run
### Overview
This script is part of a text-based game that allows users to register, log in, and perform various actions such as managing inventory, shopping, battling monsters, and more. It utilizes several modules to handle different aspects of the game, such as user management, inventory management, and game mechanics.

### Modules
The script imports the following modules:

- `B04`, `F01`, `F02`, `F03`, `F04`, `F07`, `F08`, `F09`, `F10`, `F11`, `F12`, `F13`, `F14`, `F15`, `F16`: Modules handling specific game functionalities.
- `operateCSV`: Module for CSV operations.
- `testloader`: Module for loading test data.

### Data Loading
Initial data is loaded from CSV files using the `F14.load()` function:

```python
user_data, monster_data, item_inventory, item_shop, monster_inventory, monster_shop = F14.load()

REGISTER: Allows a new user to register.
LOGIN: Allows an existing user to log in.
LOGOUT: Logs out the current user.
HELP: Displays help information.
INVENTORY: Displays the user's inventory.
SHOP: Allows the user to shop for items.
LABORATORY: Allows the user to manage their monsters in the laboratory.
BATTLE: Initiates a battle.
ARENA: Initiates an arena battle session.
MONSTER: Allows an admin to manage monsters.
JACKPOT: Allows the user to try their luck at the jackpot.
SAVE: Saves the current game state.
EXIT: Exits the game and saves the current state.