# Slack Notification Plugin

This plugin delivers messages to users using Slack.

## Initial Setup

### Creating a Webhook URL

1. Visit [Slack API: Incoming Webhooks](https://api.slack.com/messaging/webhooks) and click **Create your Slack app**.
2. Provide an app name and select the workspace where you want to install the app.
3. After creating the app, go to **Incoming Webhooks** under the **Features** section.
4. Toggle **Activate Incoming Webhooks** to **On**.
5. Click **Add New Webhook to Workspace**, then choose the channel where the messages will be posted.
6. Once authorized, you’ll be given a **Webhook URL**. Copy and save this URL in a secure place.

### Initializing the Plugin

1. If a file named `pn_slack.json` exists in the same directory as `pn_slack.exe`, rename it to `pn_slack.json.bak` or delete it.
2. Run the `pn_slack.exe` file.
3. When prompted with `Please enter your Slack webhook URL:`, paste the Webhook URL you copied in the **Creating a Webhook URL** step.

## Testing

To check if messages are being sent correctly, run the following command in Command Prompt or PowerShell:

```powershell
.\pn_slack.exe "Message sending test"
```

## Limitations
This plugin only supports notification text formats of either `plain` or `slack`.
