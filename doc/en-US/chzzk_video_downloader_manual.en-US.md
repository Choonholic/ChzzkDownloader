# Chzzk Video Downloader
Downloader for Chzzk replay videos

<div style='text-align: center'>
<img src='../../img/screenshots/screenshot_chzzkvideodownloader.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

## Version
Version 1.0.0, November 25, 2024 23:00:00

## Usage
```powershell
ChzzkVideoDownloader [-h] [-i INPUT] [-a] [-q [QUALITY]] [-d [DISPLAY]] [-y] [--version]
                     [--adult [ADULT]] [--authaut AUTHAUT] [--authses AUTHSES]
                     [--name [NAME]] [--work [WORK]] [--out [OUT]] [--temp [TEMP]]
                     [--category [CATEGORY]] [--exist [EXIST]] [--rpcid [RPCID]]
                     [--rpcport [RPCPORT]] [--snapshot SNAPSHOT] [--download [DOWNLOAD]]
                     [--thumb [THUMB]] [--startup [STARTUP]] [--settings [SETTINGS]]
                     [--reset]
                     [video]
```

### Positional Arguments
```
video                   Video number or URL to download
```

### Options
```
-h, --help              Show this help message
-i, --input INPUT       Set the download list file
-a, --auth              Set Chzzk authorized credential
-q, --quality [QUALITY] Set target quality to download (e.g. 1080p)
-d, --display [DISPLAY] Set download status display mode (quiet|simple|fluent|all)
-y, --yes               Set any confirmation values to 'yes' automatically
--version               Show version information
--adult [ADULT]         Set the process method for adult contents when credentials are invalid (ask|skip)
--authaut AUTHAUT       Set auth key of Chzzk authorized credential
--authses AUTHSES       Set session key of Chzzk authorized credential
--name [NAME]           Set output filename format
--work [WORK]           Set working directory
--out [OUT]             Set output directory
--temp [TEMP]           Set temporary directory
--category [CATEGORY]   Set output categorize method (none|streamer)
--exist [EXIST]         Set whether to overwrite or rename the file if it already exists (overwrite|rename)
--rpcid [RPCID]         Set ID of JSON-RPC server (default: 30)
--rpcport [RPCPORT]     Set port of JSON-RPC server (default: 63000, 49152-65300)
--snapshot SNAPSHOT     Save snapshot to a JSON file whenever changing status
--download [DOWNLOAD]   Set download method (default|atxc|alter)
--thumb [THUMB]         Save thumbnail image or skip (save|skip|keep)
--startup [STARTUP]     Set startup method (normal|fast)
--settings [SETTINGS]   Set action when saving settings (default|skip|quit)
--reset                 Reset all settings
```

## Example
```powershell
ChzzkVideoDownloader 1602969 --thumb --work work --out out --temp temp
```

## Setup Videos to Download
The video number or URL can be set directly to download a replay video.

For example, video number is **1602969** if video URL is https://chzzk.naver.com/video/1602969. To download this video, use the following commands.

```powershell
ChzzkVideoDownloader 1602969
ChzzkVideoDownloader https://chzzk.naver.com/video/1602969
```

If you want to download several videos sequentially, you can create a list file as following, then save as a text file encoded as UTF-8. (e.g. `list.txt`)

```python
# List Samples
https://chzzk.naver.com/video/2676946
2555164
https://chzzk.naver.com/video/2631744
https://chzzk.naver.com/video/2620211
https://chzzk.naver.com/video/2590216
2453109
```

Then, use the following commands to download.

```powershell
ChzzkVideoDownloader -i list.txt
ChzzkVideoDownloader --input list.txt
```

## Resetting Authorized Credential
To download a video that requires NAVER authorized credential, such as an adult-only video, you must specify the following information.

* NAVER ID Authorization Key from Chzzk cookie (`NID_AUT`)
* NAVER ID Session Key from Chzzk cookie (`NID_SES`)

When the authorized credential is not found when downloading a clip that requires it, a prompt to enter your authorization will be activated.

If you enter these values, they will be set as defaults, and subsequent runs will use them without further input. For more information on how to get Chzzk authorized credential, please refer to `how_to_get_chzzk_credential.en-US.pdf`.

If your authorized credential has been changed, or if you need to reset them by logging in with a different ID, use the following commands.

```powershell
ChzzkVideoDownloader video_no or url -a
ChzzkVideoDownloader video_no or url --auth
```

With `-y` or `--yes` parameters, a prompt to enter the authorization will be activated automatically without any confirmation.

```powershell
ChzzkVideoDownloader video_no or url -y
ChzzkVideoDownloader video_no or url --yes
```

## Specifying Target Quality to Download
By default, all videos will be downloaded in the best quality possible. However, if you want to save them in a different quality for saving storage or other reasons, use the following commands. Also, if the video is not using a standard resolution, the download will automatically choose the quality closest to the resolution you specify.

```powershell
ChzzkVideoDownloader video_no or url -q 720p
ChzzkVideoDownloader video_no or url --quality 720p
```

If you want to set this option to default, just use `-q` or `--quality` like below.

```powershell
ChzzkVideoDownloader video_no or url -q
ChzzkVideoDownloader video_no or url --quality
```

## Setting Output Filename Format
By default, the filename of videos and thumbnails to be saved will be `[{live_date}][{name}] {title}`. If you want to change this format, use the following command.

```powershell
ChzzkVideoDownloader video_no or url --name "[{name}][{category}] {title}"
```

If you want to set this option to default, just use `--name` without format like below.

```powershell
ChzzkVideoDownloader video_no or url --name
```

### Filename Format Tags
The following pre-defined tags can be used for filename format.

* `{name}` - Channel Name.
* `{verified}` - If channel is verified one, this tag will be `[✓]` or empty.
* `{video_no}` - Video Number.
* `{title}` - Title of the video.
* `{category_type}` - Category type of the video if set.
* `{category}` - Category of the video if set.
* `{category_value}` - Category value of the video if set.
* `{live_date...}` - Date-related tags when the stream started.
* `{publish_date...}` - Date-related tags when the video published.
* `{media...}` - Media information-related tags.

For the media-related tags, the following elements are available.

* `{media_quality}` - Media Quality. (e.g. `1080p`)
* `{media_video_width}` - Video width as pixels. (e.g. `1920`)
* `{media_video_height}` - Video height as pixels. (e.g. `1080`)
* `{media_video_framerate}` - Video frame rate as frame-per-second. (e.g. `60.0`)
* `{media_bitrate}` - Bitrate as bit-per-second. (e.g. `81920000`)
* `{media_video_codec}` - Video codec. (e.g. `H264`)

For the date-related tags, the detailed elements can be expanded as below.

* `{..._date}` - Date with `%Y%m%d%H%M%S` format. (e.g. `20240607014327`)
* `{..._date_year}` or `{..._date_year_full}` - Year with century as a decimal number. (e.g. `2024`)
* `{..._date_year_short}` - Year without century as a zero-padded decimal number. (e.g. `24`)
* `{..._date_month}` - Month as a zero-padded decimal number. (`01`, `02`, ..., `12`)
* `{..._date_month_full}` - Month as full name. (`January`, `February`, ..., `December`)
* `{..._date_month_short}` - Month as abbreviated name. (`Jan`, `Feb`, ..., `Dec`)
* `{..._date_day}` - Day of the month as a zero-padded decimal number. (`01`, `02`, ..., `31`)
* `{..._date_hour}` - Hour (24-hour clock) as a zero-padded decimal number. (`00`, `01`, ..., `23`)
* `{..._date_minute}` - Minute as a zero-padded decimal number. (`00`, `01`, ..., `59`)
* `{..._date_second}` - Second as a zero-padded decimal number. (`00`, `01`, ..., `59`)

## Handling Thumbnail Images
To save thumbnail images separately, use the following command.

```powershell
ChzzkVideoDownloader video_no or url --thumb save
```

To turn off this feature, use the following command.

```powershell
ChzzkVideoDownloader video_no or url --thumb skip
```

## Set How to Display Download Details
By default, fluent download details will be displayed. However, if you don't need the details, you can use the following command to prevent them from being displayed.

```powershell
ChzzkVideoDownloader video_no or url -d quiet
ChzzkVideoDownloader video_no or url --display quiet
```

The following display methods can be set with options of `--display` parameter.

* `quiet` - Suppress all download details.
* `fluent` - Show all fluent download details.
* `default` - This option is the same as `fluent`.

If you want to set this option to default, just use `-d` or `--display` like below.

```powershell
ChzzkVideoDownloader video_no or url -d
ChzzkVideoDownloader video_no or url --display
```

## Set Working Directory
You can use the following command to specify the directory where required files are stored to work properly.

```powershell
ChzzkVideoDownloader video_no or url --work work
```

If you want to set this option to default, just use `--work` without directory like below.

```powershell
ChzzkVideoDownloader video_no or url --work
```

## Set Output Directory
You can use the following command to specify the directory where downloaded files are saved.

```powershell
ChzzkVideoDownloader video_no or url --out out
```

By default, all files are categorized and saved in subdirectories by streamer. If you want to save files without categorizing them by streamer, use the following command.

```powershell
ChzzkVideoDownloader video_no or url --category none
```

If you want to set this option to default, just use `--out` and `--category` without options like below.

```powershell
ChzzkVideoDownloader video_no or url --out --category
```

## Set Temporary Directory
You can use the following command to specify the temporary directory where the files being downloaded are saved.

```powershell
ChzzkVideoDownloader video_no or url --temp temp
```

If you want to set this option to default, just use `--temp` without like below.

```powershell
ChzzkVideoDownloader video_no or url --temp
```

## Set Whether to Overwrite or Rename the File If It Already Exists
By default, when a file with the same name already exists, the file is saved with `(n)` appended to its name. However, you can use the following command to overwrite the file instead.

```powershell
ChzzkVideoDownloader video_no or url --exist overwrite
```

If you want to set this option to default, just use `--exist` without like below.

```powershell
ChzzkVideoDownloader video_no or url --exist
```

## Set Download Method
A lightweight download module was included as an alternative. To try out the alternative module, use the following command.

```powershell
ChzzkVideoDownloader video_no or url --download alter
```

## Set Action When Saving Settings
All options are always saved to configuration files by default. If you want to apply settings to current session only without saving, use the following command.

```powershell
ChzzkVideoDownloader video_no or url --settings skip
```

However, the following information is always saved.

* NAVER ID Authorization key from Chzzk cookie (`NID_AUT`)
* NAVER ID Session key from Chzzk cookie (`NID_SES`)

If you want to save the settings without downloading and exit, use the following command.

```powershell
ChzzkVideoDownloader --settings quit
```

## Resetting All Configurations
Over time, you may find that you've mixed things up and want to reset your settings. To reset all configurations, use the following command.

```powershell
ChzzkVideoDownloader --reset
```

This will reset the following information.

* NAVER ID Authorization key from Chzzk cookie (`NID_AUT`)
* NAVER ID Session key from Chzzk cookie (`NID_SES`)
* Settings for target quality to download
* Settings for Saving thumbnail image
* Settings for displaying download details
* Settings for output and temporary directories

## Display Version Information
You can check the version information by using the following command.

```powershell
ChzzkVideoDownloader --version
```

## Getting help
You can use the following command to get simple parameter help.

```powershell
ChzzkVideoDownloader -h
ChzzkVideoDownloader --help
```

## Parameter precedence
Except `--reset`, `-h` and `--version`, the parameters can be used in any order as shown below. However, multiple copies of the same parameter cannot be assigned.

```powershell
ChzzkVideoDownloader 1602969 --out out
```

The `-h` and `--version` parameters are processed only with the first one used, and then terminated immediately afterward. Therefore, the following command will output only the version information.

```powershell
ChzzkVideoDownloader --version -h
```

The `--reset` parameter resets the settings, ignoring any previously set values, then exits. Therefore, the video number will be ignored in the following command.

```powershell
ChzzkVideoDownloader 1602969 --reset
```

## Recommended Initial Settings
The following settings are recommeneded for the first use. The following command will set working directory (`--work`), output directory (`--out`), temporary directory (`--temp`) at once to making it easy to organize the downloaded video files.

```powershell
ChzzkVideoDownloader video_no or url --work work --out out --temp temp
```

## Controlling Externally Using JSON-RPC
Please read `how_to_control_chzzk_video_downloader.en-US.pdf` for detailed information.

## Contact Us
If you have any questions, bug reports, or improvement requests regarding the Chzzk Downloader Suite, please submit them through [GitHub](https://github.com/Choonholic/ChzzkDownloader/)‘s [Issues](https://github.com/Choonholic/ChzzkDownloader/issues/new) feature. We can respond to all languages; however, the languages we directly support are Korean, English, Japanese, and Chinese. For other languages, responses may not be fully accurate due to the use of machine translation.