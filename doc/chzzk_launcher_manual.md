# Chzzk Launcher
Launcher for Chzzk Live Downloader

## Version
Version 0.87, October 06, 2024 20:00:00

## Prerequisites
Since Chzzk Launcher is the GUI frontend application for Chzzk Live Downloader, Chzzk Live Downloader must be installed as well. If installed using the `Setup`, both will be installed in the same directory. If using a portable version, please ensure they are stored in the same directory.

## How To Execute
Click `Launcher Chzzk Live Downloaer` in Start menu, or execute `ChzzkLauncher.exe` in `Chzzk Downloader Environment`.

## Opening Main Menu
Clicking the ☰ icon located at the top-left corner of the window will open the Main Menu.

## Adding a Channel
When selecting `Add Channel...` from the Main Menu, the Add Channel dialog box will appear. Enter the UID, URL of the channel to be added, or the live streaming URL, then click the `OK` button to add the channel.

Additionally, the following items can be specified in this dialog box:

### Streamer UID / Live URL
Streamer unique identifier will automatically recognize one of the following three values when entered:

* Stream URL - `https://chzzk.naver.com/live/UID`
* Channel URL - `https://chzzk.naver.com/UID`
* Streamer UID - `UID`

### Desired Quality
You can enter values such as `best`, `1080p`, or `720p`.

As with Chzzk Live Downloader, if a non-standard resolution is used, entering a value slightly higher than the expected resolution will automatically adjust to the nearest available one. (e.g., `1200p` → `1080p`)

### LINE Notification Level
You can check the download status in real time via LINE according to notification level.

* `None` - Notification will be quiet.
* `Brief information and critical errors` - Notifications of brief information and critical errors will be sent.
* `Brief information and all errors` - Notifications of brief information and all errors will be sent.
* `Verbose information and critical errors` - Notifications of verbose information and critical errors will be sent.
* `All information and all errors` - Notifications of all information and all errors will be sent.

## Removing the Channel
To remove a channel you no longer wish to manage, select the channel from the list, click the ☰ icon, and choose `Remove Channel`, then click `OK` to confirm to remove.

If the removed channel was in the middle of a download, the download will stop at the time of removal, and the final processing steps will be completed before saving.

## Skipping Current Stream
To skip the current live stream without downloading it, select the channel from the list, click the ☰ icon, and choose `Skip Current`.

## Browsing Channel Properties
To browse the properties of the channel, select the channel from the list, click the ☰ icon, and choose `Properties...`.

## Context Menu
When you select a channel from the list and right-click, a context menu of the channel will appear.

## Saving the Channel List
The currently managed channel list can be saved to a list file and loaded later when needed.

If the list contains one or more channels, click the ☰ icon and select `Save Channels...`. A dialog box will appear, allowing you to change the directory and file name where the list will be saved.

After specifying the directory and file name for the channel list, click the **Save** button to save the list.

## Loading the Channel List
Instead of adding channels manually each time, you can load a previously saved channel list.

Click the ☰ icon and select `Load Channels...`. A dialog box will appear, allowing you to choose a channel list file.

If a channel from the loaded list already exists in the current list, it will be automatically recognized and handled accordingly.

## Refreshing List
To refresh the list, click the ☰ icon, and choose `Refresh`.

## Loading the Channel List at Startup Automatically
If you frequently manage a fixed set of channels, manually loading the list each time can become tedious. By enabling the following setting, the specified channel list will be automatically loaded at startup.

* Click the ☰ icon, and choose `Settings...` to open the settings dialog box.
* In the `Features` tab, check `Load Channels at Startup`. Then, click the **...** button next to the `Path:` field and select the channel list file you want to load.
* From the next startup onward, the specified channel list will be automatically loaded.

## Managing Chzzk Live Downloader Running Externally
Since Chzzk Live Downloader can run independently without Chzzk Launcher, it may be executed without using Chzzk Launcher.

However, even in such cases, you can configure the following settings to automatically detect and add the running instance to the channel list for management at startup.

* Check `Scan Running Instances at Startup` in the `Features` tab.
* Set the range of IDs to scan in the `ID Ranges to Scan` field. The ID is the value specified with the `-i` or `--id` parameter when running Chzzk Live Downloader. For example, if it was run as shown below, specify `3` in the scan range.

```
ChzzkLiveDownloader -i 3
```

* You can specify an ID range from 0 to 31, and the IDs or ranges can be entered as follows:
```
~3, 6, 8-10, 13~15
```

* In the example above, the IDs scanned will be `0, 1, 2, 3, 6, 8, 9, 10, 13, 14, 15`.

* If both channel scanning and channel list loading are enabled, it will first scan for running channels and then load the channel list, filling in any gaps by adding new channels.

## Opening Chzzk Downloader Environment
To open Chzzk Downloader Environment, click the ☰ icon, and choose `Open Environment (Command Prompt)` or `Open Environment (PowerShell` under `Downloader`.

## Opening the Output Directory
To open the output directory for downloaded streams, click the ☰ icon, and choose `Open Output Directory` under `Downloader`.

## Viewing Downloader Configuration
To view configuration of Chzzk Live Downloader, click the ☰ icon, and choose `View Configuration...` under `Downloader`.

## Chzzk Live Downloader Shutdown Method on Exit
You can choose whether to allow Chzzk Live Downloader to continue downloading in the background or to shut down all instances along with Launcher when exiting.

If the confirm dialog appears upon exit, it means the following conditions are met:

* There are managed channels in the channel list.
* One or more instances of Chzzk Live Downloader are running externally.

To forcefully shutdown all instances, including those running externally:
* Choose the `Forcefully shutdown all instances (Administrator privileges may be required)`, then click **Yes**.
* This is the default shutdown method.

To quit only the channels currently managed by the list:
* Choose `Requests shutdown gracefully (for managed instances only)`, then click **Yes**.

To allow downloads to continue running in the background:
* Click **No**.

To continue using Launcher:
* Click **Cancel**.

You can preset this feature in the `Downloader` tab of the settings, instead of choosing it each time on exit.

## Other Settings

### Features

* **Update Interval (Seconds)** - Sets the screen refresh interval for the list. This only affects the display and is not related to the download detection interval. The download detection interval of Chzzk Live Downloader is set to 10 seconds by default and is designed to avoid being impacted by API rate limits, unlike other tools.

### Downloader

* **JSON-RPC Server: Host Address** - Sets the host address of the JSON-RPC server.
- **JSON-RPC Server: Port** - Sets the port number for the JSON-RPC server.

### Directory

* **Working Directory** - Specifies the directory where the configuration files of Chzzk Live Downloader are saved.
* **Output Directory** - Specifies the directory where downloaded stream files are saved.
- **Temporary Directory** - Specifies the directory where temporary files are created.

### About

* **Version Information** - Displays version information of Chzzk Launcher.

## How to Contact Author
Choonholic, choonholic at outlook dot com
