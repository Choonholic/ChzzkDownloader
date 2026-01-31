# Chzzk Video Manager
Graphical Manager for Chzzk Video Downloader

<div style='text-align: center'>
<img src='../../img/screenshots/screenshot_chzzkvideomanager.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

## Version
Version 1.38.1, February 01, 2026 00:00:00

## Prerequisites
Since Chzzk Video Manager is the GUI frontend application for Chzzk Video Downloader, both of Chzzk Video Downloader and Chzzk Transport Finalizer must be installed as well.

If Chzzk Video Manager, Chzzk Video Downloader and Chzzk Transport Finalizer are in the same directory, Chzzk Video Manager will automatically recognize Chzzk Video Downloader and Chzzk Transport Finalizer upon execution. Otherwise, you will need to specify the location of Chzzk Video Downloader and Chzzk Transport Finalizer by referring to the **Verifying Prerequisites** section.

For portable versions, consider storing Chzzk Video Manager, Chzzk Video Downloader and Chzzk Transport Finalizer in the same directory for convenience. If installed using the `Setup`, all tools will be installed in the same directory.

## How To Execute
Click `Chzzk Video Manager` in Start menu, or execute `ChzzkVideoManager.exe` in `Chzzk Downloader Environment`.

## Verifying Prerequisites
Chzzk Video Manager requires Chzzk Video Downloader and Chzzk Transport Finalizer to be properly set up for full functionality. Additionally, Chzzk Video Downloader requires proper configurations of Streamlink (Version 7.0.0 or higher) and the official major versions of FFmpeg (Version 7.0 or higher). When Chzzk Video Manager starts, it checks whether this prerequisite is met, and if not, it will display the following dialog.

<div style='text-align: center'>
<img src='../../img/screenshots/vman_en-US/vman_prerequisites.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

You can click `Settings...` button to specify the location of Chzzk Video Downloader and Chzzk Transport Finalizer, or click `Download` button to install Streamlink or FFmpeg.

<div style='text-align: center'>
<img src='../../img/screenshots/vman_en-US/vman_downloader_locate_01.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

Click `...` button to choose `ChzzkVideoDownloader.exe` file in the correct path. When the correct Chzzk Video Downloader is specified, the version information will be displayed as shown in the following figure.

<div style='text-align: center'>
<img src='../../img/screenshots/vman_en-US/vman_downloader_locate_02.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

<div style='text-align: center'>
<img src='../../img/screenshots/vman_en-US/vman_finalizer_locate_01.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

Similarly, Click `...` button to choose `ChzzkTransportFinalizer.exe` file in the correct path. When the correct Chzzk Transport Finalizer is specified, the version information will be displayed as shown in the following figure.

<div style='text-align: center'>
<img src='../../img/screenshots/vman_en-US/vman_finalizer_locate_02.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

## Opening Main Menu
Clicking the ☰ icon located at the top-left corner of the window will open the Main Menu.

<div style='text-align: center'>
<img src='../../img/screenshots/vman_en-US/vman_main_menu.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

## Adding a Video
To add a video, click the ☰ icon, and choose `Add Video...`, then Add Video dialog box will appear. Enter the video number or URL of the video to be added, then click the `OK` button.

<div style='text-align: center'>
<img src='../../img/screenshots/vman_en-US/vman_add_video.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

### Video Number / Video URL
Video number will automatically recognize one of the following values when entered:

* Video URL - `https://chzzk.naver.com/video/Number`
* Video Number - `Number`

## Removing the Video
To remove a video, select the video from the list, click the ☰ icon, and choose `Remove Video`, then click `OK` to confirm to remove.

<div style='text-align: center'>
<img src='../../img/screenshots/vman_en-US/vman_remove_video.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

## Starting Download
To start download the videos of the list, click the ☰ icon, and choose `Start Download`.

## Stopping Download
To stop download the videos of the list, click the ☰ icon, and choose `Stop Download`, then click 'OK' to confirm to stop.

<div style='text-align: center'>
<img src='../../img/screenshots/vman_en-US/vman_stop_download.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

If a download was in progress when stopping, all remaining downloads will be aborted.

## Clearing Completed Downloads
To clear the completed downloads from the list, click the ☰ icon, and choose `Clear Completed`.

<div style='text-align: center'>
<img src='../../img/screenshots/vman_en-US/vman_clear_completed.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

This function is available only when the downloads are stopped midway or after it has been completed.

## Browsing Video Properties
To browse the properties of the video, select the video from the list, click the ☰ icon, and choose `Properties...`.

<div style='text-align: center'>
<img src='../../img/screenshots/vman_en-US/vman_properties.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

## Context Menu
When you select a video from the list and right-click, a context menu of the video will appear.

<div style='text-align: center'>
<img src='../../img/screenshots/vman_en-US/vman_context_menu.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

## Saving the Video List
The video list can be saved to a list file and loaded later when needed.

If the list contains one or more videos, click the ☰ icon and select `Save Video List...`, then a file dialog box will appear, allowing you to change the directory and file name where the list will be saved.

## Loading the Video List
Instead of adding videos manually each time, you can load a previously saved video list.

Click the ☰ icon and select `Load Video List...`. A dialog box will appear, allowing you to choose a video list file.

If a video from the loaded list already exists in the current list, it will be automatically recognized and handled accordingly.

## Refreshing List
To refresh the list immediately, click the ☰ icon, and choose `Refresh`.

## Opening Chzzk Downloader Environment
To open Chzzk Downloader Environment, click the ☰ icon, and choose `Open Environment (Command Prompt)` or `Open Environment (PowerShell)` under `Tools`.

## Opening the Output Directory
To open the output directory for downloaded videos, click the ☰ icon, and choose `Open Output Directory` under `Tools`.

## Purging Broken Files
If an abnormal situation occurs—such as a network disconnection or system shutdown during download—broken files may remain in the temporary directory.
To remove any remaining broken files, click the ☰ icon, and choose `Purge Broken Files` under `Tools`.

<div style='text-align: center'>
<img src='../../img/screenshots/vman_en-US/vman_purge_broken.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

## Viewing Downloader Configuration
To view configuration of Chzzk Video Downloader, click the ☰ icon, and choose `View Configuration...` under `Tools`.

<div style='text-align: center'>
<img src='../../img/screenshots/vman_en-US/vman_configuration.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

## Restarting Chzzk Transport Finalizer
If you enable `Send to Chzzk Transport Finalizer` in the `Finalize` settings, Chzzk Transport Finalizer will be launched automatically and handle the finalization. However, depending on the situation, Chzzk Transport Finalizer may be forced to terminate or may not function as expected. In such cases, restarting Chzzk Transport Finalizer may be necessary.

To restart Chzzk Transport Finalizer, click the ☰ icon, and choose `Restart Chzzk Transport Finalizer` under `Tools`.

If there was a file being finalized at the time of restart, it may become corrupted.
In this case, deleting the affected file will automatically restart the finalization.

<div style='text-align: center'>
<img src='../../img/screenshots/vman_en-US/vman_restart_finalizer.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

## Moving to Tray on Minimize
If the `Move to tray on minimize` option is enabled in `Features` settings, Chzzk Video Manager will move to the system tray when minimized.

<div style='text-align: center'>
<img src='../../img/screenshots/vman_en-US/vman_tray_icon.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

Double-clicking tray icon will restore the window to its original state, and right-clicking on the tray icon will display a menu, as shown in the following image.

<div style='text-align: center'>
<img src='../../img/screenshots/vman_en-US/vman_tray_menu.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

## Set Custom Finalize Options
If VOD status of the file being downloaded is `UPLOAD` and extra options are set in the `Custom Options` parameter in the `Finalize` settings, those options will be passed to `FFmpeg` during the finalization process. For example, the following options enable `FFmpeg` to encode using the `HEVC` codec:

```powershell
-c:v libx265 -crf 25 -c:a aac -b:a 128k
```

Please note that custom encoding is not recommended due to its suboptimal performance. For tter results, consider using external professional encoders.

## Other Settings

### Startup

<div style='text-align: center'>
<img src='../../img/screenshots/vman_en-US/vman_settings_startup.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

* **Remember window size and position on startup** - Saves the window size and position on exit and restores them on the next launch.
* **Check latest updates of Chzzk Video Manager at startup** - Decides whether check latest updates of Chzzk Video Manager at startup or not. Otherwise, Click `Check Updates` button to check updates manually.

### Features

<div style='text-align: center'>
<img src='../../img/screenshots/vman_en-US/vman_settings_features.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

* **Update Interval (Seconds)** - Sets the screen refresh interval for the list.
* **Stop downloading if free space is less than** - Sets the stop threshold when disk space is low, using either a percentage (%) or a size value. When using a size value, you can specify SI units (KB, MB, GB...) or IEC units (KiB, MiB, GiB...). You may also specify prefixes only (K, Ki, M, Mi, G, Gi...). Of course, you can also specify the value in bytes without any unit.
* **Sleep Mode** - Sets the system's sleep mode while the Chzzk Video Manager is running.
* **System Performance** - Specify the performance of the system where Chzzk Video Manager is currently running. If you encounter errors due to timeouts when adding or refreshing videos, try lowering the performance level by one step and attempt again.
* **Save metadata based on replay information** - Checks to save metadata based on replay information.

### Downloader

<div style='text-align: center'>
<img src='../../img/screenshots/vman_en-US/vman_settings_downloader.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

* **JSON-RPC Server: Allow External Remote Access** - Allows remote access to the JSON-RPC server from outside the PC running the downloader.
* **JSON-RPC Server: Port** - Sets the port number for the JSON-RPC server.
* **JSON-RPC Server: ID** - Sets the ID for the JSON-RPC server.
* **Save Thumbnail Image** - Checks to save thumbnail images separately.
* **Enable Download Speed Limit** - Limits the download speed to control network bandwidth. (e.g., 500K, 10M, 1G)
* **Save Method When The Target File Already Exists** - Sets how to save when the target file already exists.
* **Output Filename Format** - Set output filename format. Please refer to `chzzk_video_downloader_manual.en-US.pdf` for detailed information on format specifiers.
* **Target Quality** - Sets target quality to download.

### Finalize

<div style='text-align: center'>
<img src='../../img/screenshots/vman_en-US/vman_settings_finalize.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

* **JSON-RPC Server: Allow External Remote Access** - Allows remote access to the JSON-RPC server from outside the PC running the finalizer.
* **JSON-RPC Server: Port** - Sets the port number for the JSON-RPC server.
* **JSON-RPC Server: ID** - Sets the ID for the JSON-RPC server.
* **Finalize Method** - Specifies the finalization method.
* **Send To Chzzk Transport Finalizer** - Delegate finalizing stage to Chzzk Transport Finalizer.
* **Shutdown Chzzk Transport Finalizer When Exit** - Specifies whether to also shutdown Chzzk Transport Finalizer when exiting.
* **Custom Options** - Specifies custom options for the finalization. You can also click the `...` button to load and specify a custom option set file.
* **Extension for Custom Finalization** - Specifies file extension when the custom options require it.

### Plugin

<div style='text-align: center'>
<img src='../../img/screenshots/vman_en-US/vman_settings_plugin.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

* **Notifications: Path** - Sets the path to the notification plugin.
* **Notifications: Parameters** - Sets the parameters for the notification plugin.
* **Notifications: Text Type** - Sets the text format used by the notification plugin.

### Auth

<div style='text-align: center'>
<img src='../../img/screenshots/vman_en-US/vman_settings_auth.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

* **Auth Key (NID_AUT)** - Specifies the authorization key of NAVER ID.
* **Session Key (NID_SES)** - Specifies the session key of NAVER ID.
* **Ignore authentication credential temporarily** - Sets whether ignore authentication credential temporarily or not.

For more information on how to get Chzzk authentication credential, please refer to `how_to_get_chzzk_credential.en-US.pdf`.

### Directories

<div style='text-align: center'>
<img src='../../img/screenshots/vman_en-US/vman_settings_directories.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

* **Working Directory** - Specifies the directory where the configuration files of Chzzk Video Downloader are saved.
* **Output Directory** - Specifies the directory where downloaded video files are saved.
* **Temporary Directory** - Specifies the directory where temporary files are created.
* **Categorize Method** - Sets the categorization method for directories where downloaded video files are saved.

<div style='text-align: center'>
<img src='../../img/screenshots/vman_en-US/vman_settings_network.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

You can click the `Network...` button to enter the information required to access the network storage.

### About

<div style='text-align: center'>
<img src='../../img/screenshots/vman_en-US/vman_settings_about.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

* **Version Information** - Displays version information of Chzzk Video Manager.
* **Contact Links** - Links to contact to authors.

## Contact Us
If you have any questions, bug reports, or improvement requests regarding the Chzzk Downloader Suite, please submit them through [GitHub](https://github.com/Choonholic/ChzzkDownloader/)‘s [Issues](https://github.com/Choonholic/ChzzkDownloader/issues/new) feature. We can respond to all languages; however, the languages we directly support are Korean, English, Japanese, and Chinese. For other languages, responses may not be fully accurate due to the use of machine translation.
