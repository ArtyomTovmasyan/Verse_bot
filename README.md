# Verse_bot

A simple bot that shares inspirational verses and encouragements.

## Features
- Sends random motivational verses from `verses.json`.
- Sends encouraging messages from `encouragements.json`.
- Easy to extend with more verses or encouragements.
---------------------------------
## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ArtyomTovmasyan/Verse_bot.git
---------------------------
2. Navigate into the project directory:
------------------------
cd Verse_bot
------------------------------------------
3.Create a virtual environment and activate it:
--------------------------------
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
----------------------------
4.Install dependencies:

pip install -r requirements.txt
-----------------------------
Usage

Add your bot token in .env.

Run the bot:

python bot.py

File Overview

bot.py – main bot script.

verses.json – list of inspirational verses.

encouragements.json – list of encouraging messages.

requirements.txt – Python dependencies.

--------------------
Contributing

Feel free to fork this repository and submit pull requests to add more features or verses.

License

This project is open-source and available under the MIT License.
