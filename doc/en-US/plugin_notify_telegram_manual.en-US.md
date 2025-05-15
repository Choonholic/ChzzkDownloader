# Telegram-based Notification Plugin

This plugin delivers messages to users using Telegram's bot functionality.

## Initial Setup

### Creating a Bot

1. Search for `@BotFather` on Telegram and start a conversation.
2. Type `/newbot` to create a new bot.
3. When asked for the bot's name, enter a new name. The name must be unique and not already in use.
4. When asked for the bot's username, enter a new username. It must end with `bot` and is case-insensitive.
5. Once the bot is created, a message will be shown with your bot’s token. Copy and save this token in a secure place.

### Checking Your User ID

1. Search for `@userinfobot` on Telegram and start a conversation.
2. Type `/start` to view your user information.
3. Copy the `Id` value and save it in a secure place.

### Initializing the Plugin

1. If a file named `pn_telegram.json` exists in the same directory as `pn_telegram.exe`, rename it to `pn_telegram.json.bak` or delete it.
2. Run the `pn_telegram.exe` file.
3. When prompted with `Please enter your Telegram bot token:`, enter the bot token you copied in the **Creating a Bot** step.
4. When prompted with `Please enter your Telegram chat ID:`, enter the user ID you copied in the **Checking Your User ID** step.

## Testing
To check if messages are being sent correctly, run the following command in Command Prompt or PowerShell:

```powershell
.\pn_telegram.exe "Message sending test"
```
