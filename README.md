# Discord AutoTyper Bot

 A **Discord AutoTyper Bot** that sends automated messages periodically in a specified channel. This bot is designed to work on multiple servers, allowing each guild to customize its own message interval and content.


## Features
-  **Automated Typing**: Sends messages periodically in a specified channel.
-  **Customizable Message & Interval**: Each server can set its own message and interval.
-  **Slash Commands**: Easy-to-use commands for starting, stopping, and modifying auto-typing settings.
-  **Multi-Guild Support**: Works independently for each server.

## Setup Instructions

### 1️⃣ Prerequisites
Ensure you have the following installed:
- Python 3.8+
- `discord.py` library
- A Discord bot token

### 2️⃣ Install Dependencies
```sh
pip install discord.py
```

### 3️⃣ Configure Secrets
Create a `Secrets.py` file with the following content:
```python
class Secrets:
    BOT_TOKEN = "your-bot-token-here"
    SERVER_ID = your-server-id-here
```

### 4️⃣ Run the Bot
```sh
python bot.py
```

---

## 🚀 Usage
The bot provides the following slash commands:

### **Start AutoTyper**
```
/start_bot
```
🔹 Starts the auto-typer in the current server.

### **Stop AutoTyper**
```
/stop_bot
```
🔹 Stops the auto-typer in the current server.

### **Set AutoTyper Message**
```
/set_message <new_message>
```
🔹 Updates the message the bot sends periodically.

### **Set AutoTyper Interval**
```
/set_interval <interval_in_seconds>
```
🔹 Updates the interval (seconds) between messages.

---

- Defines Discord slash commands.
- Manages bot startup and command synchronization.


