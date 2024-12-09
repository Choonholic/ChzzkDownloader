# Chzzk Clip Downloader
Downloader for Chzzk clips

<div style='text-align: center'>
<img src='../../img/screenshots/screenshot_chzzkclipdownloader.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

## Version
Version 1.3.0, December 10, 2024 08:00:00

## Usage
```powershell
ChzzkClipDownloader [-h] [--version] [-i INPUT] [-a] [--authaut AUTHAUT] [--authses AUTHSES]
                    [--adult [ADULT]] [-y] [-d [DISPLAY]] [--name [NAME]] [--work [WORK]]
                    [--out [OUT]] [--temp [TEMP]] [--category [CATEGORY]] [--exist [EXIST]]
                    [--threshold [THRESHOLD]] [--rpcid [RPCID]] [--rpcport [RPCPORT]]
                    [--snapshot SNAPSHOT] [--download [DOWNLOAD]] [--thumb [THUMB]]
                    [--startup [STARTUP]] [--settings [SETTINGS]] [--reset]
                    [clip]
```

### Positional Arguments
```
clip                    Clip UID or URL to download
```

### Options
```
-h, --help              Show this help message
--version               Show version information
-i, --input INPUT       Set the download list file
-a, --auth              Set Chzzk authorized credential with prompt
--authaut AUTHAUT       Set auth key of Chzzk authorized credential
--authses AUTHSES       Set session key of Chzzk authorized credential
--adult [ADULT]         Set the process method for adult contents when credentials are invalid (ask|skip)
-y, --yes               Set any confirmation values to 'yes' automatically
-d, --display [DISPLAY] Set download status display mode (quiet|simple|fluent|all)
--name [NAME]           Set output filename format
--work [WORK]           Set working directory
--out [OUT]             Set output directory
--temp [TEMP]           Set temporary directory
--category [CATEGORY]   Set output categorize method (none|streamer)
--exist [EXIST]         Set how to save when the target file already exists (rename|skip|overwrite)
--threshold [THRESHOLD] Set the threshold % for stopping downloads when disk space is low (disable: -, default: 10, 3-30)
--rpcid [RPCID]         Set ID of JSON-RPC server (default: 50)
--rpcport [RPCPORT]     Set port of JSON-RPC server (default: 64000, 49152-65300)
--snapshot SNAPSHOT     Save snapshot to a JSON file whenever changing status
--download [DOWNLOAD]   Set download method (default|atxc|alter)
--thumb [THUMB]         Save thumbnail image or skip (save|skip)
--startup [STARTUP]     Set startup method (normal|fast)
--settings [SETTINGS]   Set action when saving settings (default|skip|quit)
--reset                 Reset all settings
```

## Example
```powershell
ChzzkClipDownloader C46IcpG11p --thumb --work work --out out --temp temp
```

## Setup Clips to Download
The Clip UID or URL can be set directly to download a clip.

For example, Clip UID is **C46IcpG11p** if clip URL is https://chzzk.naver.com/clips/C46IcpG11p. To download this clip, use the following commands.

```powershell
ChzzkClipDownloader C46IcpG11p
ChzzkClipDownloader https://chzzk.naver.com/clips/C46IcpG11p
```

If you want to download several clips sequentially, you can create a list file as following, then save as a text file encoded as UTF-8. (e.g. `list.txt`)

```python
# List Samples
https://chzzk.naver.com/clips/YY9plBpybL
C46IcpG11p
https://chzzk.naver.com/clips/gTSq4c8HaQ
https://chzzk.naver.com/clips/nZbWU27D95
```

Then, use the following commands to download.

```powershell
ChzzkClipDownloader -i list.txt
ChzzkClipDownloader --input list.txt
```

## Resetting Authorized Credential
To download a clip that requires NAVER authorized credential, such as an adult-only clip, you must specify the following information.

* NAVER ID Authorization Key from Chzzk cookie (`NID_AUT`)
* NAVER ID Session Key from Chzzk cookie (`NID_SES`)

When the authorized credential is not found when downloading a clip that requires it, a prompt to enter your authorization will be activated.

If you enter these values, they will be set as defaults, and subsequent runs will use them without further input. For more information on how to get Chzzk authorized credential, please refer to `how_to_get_chzzk_credential.en-US.pdf`.

If your authorized credential has been changed, or if you need to reset them by logging in with a different ID, use the following commands.

```powershell
ChzzkClipDownloader clip_uid or url -a
ChzzkClipDownloader clip_uid or url --auth
```

With `-y` or `--yes` parameters, a prompt to enter the authorization will be activated automatically without any confirmation.

```powershell
ChzzkClipDownloader clip_uid or url -y
ChzzkClipDownloader clip_uid or url --yes
```

## Setting Output Filename Format
By default, the filename of clips and thumbnails to be saved will be `[{download_date}][{name}] {title}`. If you want to change this format, use the following command.

```powershell
ChzzkClipDownloader clip_uid or url --name "[{name}][{category}] {title}"
```

If you want to set this option to default, just use `--name` without format like below.

```powershell
ChzzkClipDownloader clip_uid or url --name
```

### Filename Format Tags
The following pre-defined tags can be used for filename format.

* `{name}` - Channel Name.
* `{verified}` - If channel is verified one, this tag will be `[✓]` or empty.
* `{clip_uid}` - Clip UID.
* `{title}` - Title of the clip.
* `{download_date...}` - Date-related tags when the stream started.
* `{media...}` - Media information-related tags.

For the media-related tags, the following elements are available.

* `{media_quality}` - Media Quality. (e.g. `1080p`)
* `{media_video_width}` - Video width as pixels. (e.g. `1920`)
* `{media_video_height}` - Video height as pixels. (e.g. `1080`)
* `{media_video_bitrate}` - Video bitrate as bit-per-second. (e.g. `8000000`)
* `{media_audio_bitrate}` - Audio bitrate as bit-per-second. (e.g. `192000`)
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
ChzzkClipDownloader clip_uid or url --thumb save
```

To turn off this feature, use the following command.

```powershell
ChzzkClipDownloader clip_uid or url --thumb skip
```

## Set How to Display Download Details
By default, fluent download details will be displayed. However, if you don't need the details, you can use the following command to prevent them from being displayed.

```powershell
ChzzkClipDownloader clip_uid or url -d quiet
ChzzkClipDownloader clip_uid or url --display quiet
```

The following display methods can be set with options of `--display` parameter.

* `quiet` - Suppress all download details.
* `fluent` - Show all fluent download details.
* `default` - This option is the same as `fluent`.

If you want to set this option to default, just use `-d` or `--display` like below.

```powershell
ChzzkClipDownloader clip_uid or url -d
ChzzkClipDownloader clip_uid or url --display
```

## Set Working Directory
You can use the following command to specify the directory where required files are stored to work properly.

```powershell
ChzzkClipDownloader clip_uid or url --work work
```

If you want to set this option to default, just use `--work` without directory like below.

```powershell
ChzzkClipDownloader clip_uid or url --work
```

## Set Output Directory
You can use the following command to specify the directory where downloaded files are saved.

```powershell
ChzzkClipDownloader clip_uid or url --out out
```

By default, all files are categorized and saved in subdirectories by streamer. If you want to save files without categorizing them by streamer, use the following command.

```powershell
ChzzkClipDownloader clip_uid or url --category none
```

If you want to set this option to default, just use `--out` and `--category` without options like below.

```powershell
ChzzkClipDownloader clip_uid or url --out --category
```

## Set Temporary Directory
You can use the following command to specify the temporary directory where the files being downloaded are saved.

```powershell
ChzzkClipDownloader clip_uid or url --temp temp
```

If you want to set this option to default, just use `--temp` without like below.

```powershell
ChzzkClipDownloader clip_uid or url --temp
```

## Set how to save when the target file already exists
By default, when a file with the same name already exists, the file is saved with `(n)` appended to its name. However, you can use the following command to overwrite the file or skip download itself instead.

```powershell
ChzzkClipDownloader clip_uid or url --exist overwrite
ChzzkClipDownloader clip_uid or url --exist skip
```

If you want to set this option to default, just use `--exist` without like below.

```powershell
ChzzkClipDownloader clip_uid or url --exist
```

## Set the threshold % for stopping downloads when disk space is low
By default, downloading will stop if the free space in the storage directory or temporary directory drops below 10%. To set the free disk space threshold, use the following command. The acceptable range is `3` to `30`.

```powershell
ChzzkClipDownloader clip_uid or url --threshold 20
```

To disable the feature that stops downloads based on free disk space, use the following command.

```powershell
ChzzkClipDownloader clip_uid or url --threshold -
```

If you want to set this option to default, just use `--threshold` without like below.

```powershell
ChzzkClipDownloader clip_uid or url --threshold
```

## Set Download Method
A lightweight download module was included as an alternative. To try out the alternative module, use the following command.

```powershell
ChzzkClipDownloader clip_uid or url --download alter
```

## Set Action When Saving Settings
All options are always saved to configuration files by default. If you want to apply settings to current session only without saving, use the following command.

```powershell
ChzzkClipDownloader --settings skip
```

However, the following information is always saved.

* NAVER ID Authorization key from Chzzk cookie (`NID_AUT`)
* NAVER ID Session key from Chzzk cookie (`NID_SES`)

If you want to save the settings without downloading and exit, use the following command.

```powershell
ChzzkClipDownloader --settings quit
```

## Resetting All Configurations
Over time, you may find that you've mixed things up and want to reset your settings. To reset all configurations, use the following command.

```powershell
ChzzkClipDownloader --reset
```

This will reset the following information.

* NAVER ID Authorization key from Chzzk cookie (`NID_AUT`)
* NAVER ID Session key from Chzzk cookie (`NID_SES`)
* Settings for Saving thumbnail image
* Settings for displaying download details
* Settings for output and temporary directories

## Display Version Information
You can check the version information by using the following command.

```powershell
ChzzkClipDownloader --version
```

## Getting help
You can use the following command to get simple parameter help.

```powershell
ChzzkClipDownloader -h
ChzzkClipDownloader --help
```

## Parameter precedence
Except `--reset`, `-h` and `--version`, the parameters can be used in any order as shown below. However, multiple copies of the same parameter cannot be assigned.

```powershell
ChzzkClipDownloader C46IcpG11p --out out
```

The `-h` and `--version` parameters are processed only with the first one used, and then terminated immediately afterward. Therefore, the following command will output only the version information.

```powershell
ChzzkClipDownloader --version -h
```

The `--reset` parameter resets the settings, ignoring any previously set values, then exits. Therefore, the clip UID will be ignored in the following command.

```powershell
ChzzkClipDownloader C46IcpG11p --reset
```

## Recommended Initial Settings
The following settings are recommeneded for the first use. The following command will set working directory (`--work`), output directory (`--out`), temporary directory (`--temp`) at once to making it easy to organize the downloaded clip files.

```powershell
ChzzkClipDownloader clip_uid or url --work work --out out --temp temp
```

## Controlling Externally Using JSON-RPC
Please read `how_to_control_chzzk_clip_downloader.en-US.pdf` for detailed information.

## Contact Us
If you have any questions, bug reports, or improvement requests regarding the Chzzk Downloader Suite, please submit them through [GitHub](https://github.com/Choonholic/ChzzkDownloader/)‘s [Issues](https://github.com/Choonholic/ChzzkDownloader/issues/new) feature. We can respond to all languages; however, the languages we directly support are Korean, English, Japanese, and Chinese. For other languages, responses may not be fully accurate due to the use of machine translation.
