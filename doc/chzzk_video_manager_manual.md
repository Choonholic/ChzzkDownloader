# Chzzk Video Manager
Graphical Manager for Chzzk Video Downloader

<div style='text-align: center'>
<img src='../img/screenshots/screenshot_chzzkvideomanager.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

## Version
Version 0.92, November 04, 2024 00:00:00

## Prerequisites
Since Chzzk Video Manager is the GUI frontend application for Chzzk Video Downloader, Chzzk Video Downloader must be installed as well.

If the Chzzk Video Downloader and Chzzk Video Manager are in the same directory, Chzzk Video Manager will automatically recognize Chzzk Video Downloader upon execution. Otherwise, you will need to specify the location of Chzzk Video Downloader by referring to the **Verifying Prerequisites** section.

For portable versions, consider storing both Chzzk Video Downloader and Chzzk Video Manager in the same directory for convenience. If installed using the `Setup`, both will be installed in the same directory.

## How To Execute
Click `Chzzk Video Manager` in Start menu, or execute `ChzzkVideoManager.exe` in `Chzzk Downloader Environment`.

## Verifying Prerequisites
Chzzk Video Manager requires Chzzk Video Downloader to be properly set up for full functionality Additionally. When Chzzk Video Manager starts, it checks whether this prerequisite is met, and if not, it will display the following dialog.

<div style='text-align: center'>
<img src='../img/screenshots/vman/vman_prerequisites.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

You can click `Settings...` button to specify the location of Chzzk Video Downloader.

<div style='text-align: center'>
<img src='../img/screenshots/vman/vman_downloader_locate_01.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

Click `...` button to choose `ChzzkVideoDownloader.exe` file in the correct path.

<div style='text-align: center'>
<img src='../img/screenshots/vman/vman_downloader_locate_02.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

When the correct Chzzk Video Downloader is specified, the version information will be displayed as shown in the following figure.

<div style='text-align: center'>
<img src='../img/screenshots/vman/vman_downloader_locate_03.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

## Opening Main Menu
Clicking the ☰ icon located at the top-left corner of the window will open the Main Menu.

<div style='text-align: center'>
<img src='../img/screenshots/vman/vman_main_menu_01.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

<div style='text-align: center'>
<img src='../img/screenshots/vman/vman_main_menu_02.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

## Adding a Video
When selecting `Add Video...` from the Main Menu, the Add Video dialog box will appear. Enter the video number or URL of the video to be added, then click the `OK` button to add the video.

<div style='text-align: center'>
<img src='../img/screenshots/vman/vman_add_video.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

### Video Number / Video URL
Video number will automatically recognize one of the following values when entered:

* Video URL - `https://chzzk.naver.com/video/Number`
* Video Number - `Number`

## Removing the Video
To remove a video, select the video from the list, click the ☰ icon, and choose `Remove Video`, then click `OK` to confirm to remove.

<div style='text-align: center'>
<img src='../img/screenshots/vman/vman_remove_video.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

## Starting Download
To start download the videos of the list, click the ☰ icon, and choose `Start Download`.

## Stopping Download
To stop download the videos of the list, click the ☰ icon, and choose `Stop Download`, then click 'OK' to confirm to stop.

<div style='text-align: center'>
<img src='../img/screenshots/vman/vman_stop_download.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

If a download was in progress when stopping, all remaining downloads will be aborted.

## Browsing Video Properties
To browse the properties of the video, select the video from the list, click the ☰ icon, and choose `Properties...`.

<div style='text-align: center'>
<img src='../img/screenshots/vman/vman_properties.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

## Context Menu
When you select a video from the list and right-click, a context menu of the video will appear.

<div style='text-align: center'>
<img src='../img/screenshots/vman/vman_context_menu.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

## Saving the Video List
The video list can be saved to a list file and loaded later when needed.

If the list contains one or more videos, click the ☰ icon and select `Save Video List...`. A dialog box will appear, allowing you to change the directory and file name where the list will be saved.

<div style='text-align: center'>
<img src='../img/screenshots/vman/vman_save_list.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

After specifying the directory and file name for the video list, click the **Save** button to save the list.

## Loading the Video List
Instead of adding videos manually each time, you can load a previously saved video list.

Click the ☰ icon and select `Load Video List...`. A dialog box will appear, allowing you to choose a video list file.

<div style='text-align: center'>
<img src='../img/screenshots/vman/vman_load_list.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

If a video from the loaded list already exists in the current list, it will be automatically recognized and handled accordingly.

## Refreshing List
To refresh the list immediately, click the ☰ icon, and choose `Refresh`.

## Opening Chzzk Downloader Environment
To open Chzzk Downloader Environment, click the ☰ icon, and choose `Open Environment (Command Prompt)` or `Open Environment (PowerShell)` under `Downloader`.

<div style='text-align: center'>
<img src='../img/screenshots/vman/vman_environment.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

## Opening the Output Directory
To open the output directory for downloaded videos, click the ☰ icon, and choose `Open Output Directory` under `Downloader`.

## Viewing Downloader Configuration
To view configuration of Chzzk Video Downloader, click the ☰ icon, and choose `View Configuration...` under `Downloader`.

<div style='text-align: center'>
<img src='../img/screenshots/vman/vman_configuration.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

## Moving to Tray on Minimize
If the `Move to tray on minimize` option is enabled in `Features` settings, Chzzk Video Manager will move to the system tray when minimized.

<div style='text-align: center'>
<img src='../img/screenshots/vman/vman_tray_icon.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

Double-clicking tray icon will restore the window to its original state, and right-clicking on the tray icon will display a menu, as shown in the following image.

<div style='text-align: center'>
<img src='../img/screenshots/vman/vman_tray_menu.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

## Other Settings

### Startup

<div style='text-align: center'>
<img src='../img/screenshots/vman/vman_settings_startup.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

* **Remember window size and position on startup** - Saves the window size and position on exit and restores them on the next launch.
* **Check latest updates of Chzzk Video Manager at startup** - Decides whether check latest updates of Chzzk Video Manager at startup or not. Otherwise, Click `Check Updates` button to check updates manually.

### Features

<div style='text-align: center'>
<img src='../img/screenshots/vman/vman_settings_features.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

* **Update Interval (Seconds)** - Sets the screen refresh interval for the list.
* **Performance Level** - Specify the performance of the system where Chzzk Video Manager is currently running. If you encounter errors due to timeouts when adding or refreshing videos, try lowering the performance level by one step and attempt again.

### Downloader

<div style='text-align: center'>
<img src='../img/screenshots/vman/vman_settings_downloader.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

* **JSON-RPC Server: Host Address** - Sets the host address of the JSON-RPC server.
* **JSON-RPC Server: Port** - Sets the port number for the JSON-RPC server.
* **JSON-RPC Server: ID** - Sets the ID for the JSON-RPC server.
* **Save thumbnail image** - Checks to save thumbnail images separately.
* **Target Quality** - Sets target quality to download.

### Directory

<div style='text-align: center'>
<img src='../img/screenshots/vman/vman_settings_directory.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

* **Working Directory** - Specifies the directory where the configuration files of Chzzk Video Downloader are saved.
* **Output Directory** - Specifies the directory where downloaded video files are saved.
* **Temporary Directory** - Specifies the directory where temporary files are created.

### About

<div style='text-align: center'>
<img src='../img/screenshots/vman/vman_settings_about.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

* **Version Information** - Displays version information of Chzzk Video Manager.
* **Contact Links** - Links to contact to authors.

## Contact Us
If you have any questions, bug reports, or improvement requests regarding the Chzzk Downloader Suite, please submit them through [GitHub](https://github.com/Choonholic/ChzzkDownloader/)‘s [Issues](https://github.com/Choonholic/ChzzkDownloader/issues/new) feature. We can respond to all languages; however, the languages we directly support are Korean, English, Japanese, and Chinese. For other languages, responses may not be fully accurate due to the use of machine translation.

치지직 다운로드 도구에 대해 궁금한 사항, 제보할 오류, 개선 요청 사항 등이 있을 때는 [GitHub](https://github.com/Choonholic/ChzzkDownloader/)의 [Issues](https://github.com/Choonholic/ChzzkDownloader/issues/new) 기능을 통해 제보해 주세요. 모든 언어에 대응 가능하나, 직접 대응 가능한 언어는 한국어, 영어, 일본어, 중국어이며, 다른 언어는 기계 번역을 통하기 때문에 100% 대응이 불가능할 수 있습니다.

Chzzk Downloader Suiteに関するご質問、バグ報告、または改善要望がございましたら、[GitHub](https://github.com/Choonholic/ChzzkDownloader/)の[Issues](https://github.com/Choonholic/ChzzkDownloader/issues/new)機能を通じてお知らせください。全ての言語に対応可能ですが、直接対応可能な言語は韓国語、英語、日本語、中国語です。他の言語については、機械翻訳を通じて対応するため、100%正確に対応できない場合があります。

如果您对Chzzk Downloader Suite有任何疑问、错误报告或改进建议，请通过[GitHub](https://github.com/Choonholic/ChzzkDownloader/)的[Issues](https://github.com/Choonholic/ChzzkDownloader/issues/new)功能提交反馈。我们可以应对所有语言，但我们直接支持的语言是韩语、英语、日语和中文。对于其他语言，由于通过机器翻译处理，可能无法做到百分之百的准确响应。
