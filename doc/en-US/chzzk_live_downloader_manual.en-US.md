# Chzzk Live Downloader
Downloader for Chzzk live streams

<div style='text-align: center'>
<img src='../../img/screenshots/screenshot_chzzklivedownloader.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

## Version
Version 1.39.0, February 12, 2026 00:00:00

## Prerequisites
- **[Mandatory]** Streamlink (Requires Streamlink 7.0.0 or higher)
- **[Mandatory]** The official major versions of FFmpeg (Requires FFmpeg 7.0 or higher)

## Usage
```
ChzzkLiveDownloader
  [-h] [--version] [-i ID] [-u [UID]] [-a [AUTH]] [--authaut AUTHAUT] [--authses AUTHSES]
  [--authcookie AUTHCOOKIE] [--adult [ADULT]] [-y] [-q [QUALITY]] [-d [DISPLAY]] [--once ONCE]
  [--stream [STREAM]] [--final [FINAL]] [--custom [CUSTOM]] [--ext [EXT]] [--offset OFFSET]
  [--duration DURATION] [--detect [DETECT]] [--name [NAME]] [--work [WORK]]
  [--work-user [WORK_USER]] [--work-pass [WORK_PASS]] [--out [OUT]] [--out-user [OUT_USER]]
  [--out-pass [OUT_PASS]] [--temp [TEMP]] [--temp-user [TEMP_USER]] [--temp-pass [TEMP_PASS]]
  [--category [CATEGORY]] [--exist [EXIST]] [--threshold [THRESHOLD]] [--rpc]
  [--rpcexpose [RPCEXPOSE]] [--rpcbaseport [RPCBASEPORT]] [--snapshot SNAPSHOT] [--thumb [THUMB]]
  [--metadata [METADATA]] [--startup [STARTUP]] [--pnpath [PNPATH]] [--pnlanguage [PNLANGUAGE]]
  [--pnparams [PNPARAMS]] [--pntexttype [PNTEXTTYPE]] [--settings [SETTINGS]] [--reset]
```

### Options
```
-h, --help                  Show this help message
--version                   Show version information
-i, --id ID                 Set streamer configuration id
-u, --uid [UID]             Set streamer unique identifier
-a, --auth [AUTH]           Set Chzzk authentication credential control method (reuse|reissue|ignore)
--authaut AUTHAUT           Set auth key of Chzzk authentication credential
--authses AUTHSES           Set session key of Chzzk authentication credential
--authcookie AUTHCOOKIE     Set Netscape cookie file of Chzzk authentication credential
--adult [ADULT]             Set the process method for adult contents when credentials are invalid (ask|skip)
-y, --yes                   Set any confirmation values to 'yes' automatically
-q, --quality [QUALITY]     Set target quality to download (e.g. 1080p)
-d, --display [DISPLAY]     Set display mode (quiet|simple|fluent|all)
--once ONCE                 Download a live stream only once
--stream [STREAM]           Set stream retrieving method (standard|request-timemachine|force-timemachine)
--final [FINAL]             Set finalization method (bypass|convert|cleanup|cconvert|ccleanup)
--custom [CUSTOM]           Set custom finalize options (applicable only with cconvert|ccleanup)
--ext [EXT]                 Set output file extension (applicable only with cconvert|ccleanup)
--offset OFFSET             Set amount of time to skip from the beginning of the stream
--duration DURATION         Set the maximum stream duration to download
--detect [DETECT]           Set detection interval (default: 60, 10-300)
--name [NAME]               Set output filename format
--work [WORK]               Set working directory
--work-user [WORK_USER]     Set username to use when working directory is on remote network
--work-pass [WORK_PASS]     Set password to use when working directory is on remote network
--out [OUT]                 Set output directory
--out-user [OUT_USER]       Set username to use when output directory is on remote network
--out-pass [OUT_PASS]       Set password to use when output directory is on remote network
--temp [TEMP]               Set temporary directory
--temp-user [TEMP_USER]     Set username to use when temporary directory is on remote network
--temp-pass [TEMP_PASS]     Set password to use when temporary directory is on remote network
--category [CATEGORY]       Set output categorize method (none|streamer)
--exist [EXIST]             Set how to save when the target file already exists (rename|skip|overwrite)
--threshold [THRESHOLD]     Set the threshold by size or percent for stopping downloads when disk space is low (disable: -, default: 5%, valid range: 1-50% of total disk space, even for size values)
--rpc                       Activate JSON-RPC server
--rpcexpose [RPCEXPOSE]     Set JSON-RPC server exposure method (close|open)
--rpcbaseport [RPCBASEPORT] Set base port of JSON-RPC server (default: 62000, 49152-65300)
--snapshot SNAPSHOT         Save snapshot to a JSON file whenever changing status
--thumb [THUMB]             Save thumbnail image or skip (save|skip)
--metadata [METADATA]       Save metadata or skip (save|skip)
--startup [STARTUP]         Set startup method (normal|fast)
--pnpath [PNPATH]           Set the path to the notification plugin
--pnlanguage [PNLANGUAGE]   Set the language used by the notification plugin
--pnparams [PNPARAMS]       Set the parameters for the notification plugin
--pntexttype [PNTEXTTYPE]   Set the text format used by the notification plugin (plain|markdown|html)
--settings [SETTINGS]       Set action when saving settings (default|update|show|skip|quit)
--reset                     Reset all settings
```

### Example
```powershell
ChzzkLiveDownloader -i 2 --thumb save --detect 30 --work work --out out --temp temp
```

## Initial Setup
For initial setup, the following items should be prepared.

- Streamer Channel UID

Execute without parameters for the first use.

```powershell
ChzzkLiveDownloader
```

For recommended initial setings, see [Recommended Initial Settings](#recommended-initial-settings) section in later.

## Downloading Multiple Channels Simultaneously
To download multiple channels at the same time, you can open a new Command Prompt or PowerShell console and run Chzzk Live Downloader. However, if you run without parameters, Chzzk Live Downloader will always download the first UID you registered, so if you want to specify a new UID, you can specify a new configuration with the following commands.

```powershell
ChzzkLiveDownloader -i n
ChzzkLiveDownloader --id n
```

The specific UID will be used again when you set the same parameters the next time, and automatically search for and download live streams with the UID.

## Managing UID Assignments

### Setting UID
To set the UID assigned to a specific ID, use the following commands.

```powershell
ChzzkLiveDownloader -i n -u uid or url
ChzzkLiveDownloader --id n --uid uid or url
```

If you want to change the UID assigned to the default ID, you can do so by specifying `0` for the `-i` (or `--id`) parameter, or by specifying only the `-u` (or `--uid`) parameter, as follows:

```powershell
ChzzkLiveDownloader -u uid or url
ChzzkLiveDownloader --uid uid or url
```

### Resetting UID
To reset the UID assigned to a specific ID, use the following commands. This will work even if you have not previously assigned a UID to the ID.

For default ID:

```powershell
ChzzkLiveDownloader -u
ChzzkLiveDownloader --uid
```

For a specific ID:

```powershell
ChzzkLiveDownloader -i n -u
ChzzkLiveDownloader --id n --uid
```

## Downloading A Live Stream Only Once Without Saving Information
If you want to download a live stream with URL only once, rather than specifying and saving the streamer information, use the following command.

```powershell
ChzzkLiveDownloader --once uid or url
```

## Resetting Authentication Credential
To download a live stream that requires NAVER authentication credential, such as an adult-only live stream, you must specify the following information.

- NAVER ID authentication key obtained from the Chzzk cookie (`NID_AUT`)
- NAVER ID session key obtained from the Chzzk cookie (`NID_SES`)

When the authentication credential is not found when downloading a clip that requires it, a prompt to enter your authorization will be activated.

If you enter these values, they will be set as defaults, and subsequent runs will use them without further input. For more information on how to get Chzzk authentication credential, please refer to `how_to_get_chzzk_credential.en-US.pdf`.

If your authentication credential has been changed, or if you need to reset them by logging in with a different ID, use the following commands.

```powershell
ChzzkLiveDownloader -a reset
ChzzkLiveDownloader --auth reset
```

If you need to temporarily ignore authentication credential, use the following commands.

```powershell
ChzzkLiveDownloader -a ignore
ChzzkLiveDownloader --auth ignore
```

With `-y` or `--yes` parameters, a prompt to enter the authorization will be activated automatically without any confirmation.

```powershell
ChzzkLiveDownloader -y
ChzzkLiveDownloader --yes
```

## Specifying Target Quality to Download
By default, all streams will be downloaded in the best quality possible. However, if you want to save them in a different quality for saving storage or other reasons, use the following commands. Also, if the stream is not using a standard resolution, the download will automatically choose the quality closest to the resolution you specify.

```powershell
ChzzkLiveDownloader -q 720p
ChzzkLiveDownloader --quality 720p
```

If you want to set this option to default, just use `-q` or `--quality` like below.

```powershell
ChzzkLiveDownloader -q
ChzzkLiveDownloader --quality
```

## Setting Output Filename Format
By default, the filename of videos and thumbnails to be saved will be `[{download_date}][{name}] {title}`. If you want to change this format, use the following command.

```powershell
ChzzkLiveDownloader --name "[{name}][{category}] {title}"
```

If you want to set this option to default, just use `--name` without format like below.

```powershell
ChzzkLiveDownloader --name
```

### Filename Format Tags
The following pre-defined tags can be used for filename format.

- `{name}` - Channel Name.
- `{verified}` - If channel is verified one, this tag will be `[✓]` or empty.
- `{channel_uid}` - Channel UID.
- `{title}` - Title of the stream.
- `{category_type}` - Category type of the stream if set.
- `{category}` - Category of the stream if set.
- `{category_value}` - Category value of the stream if set.
- `{live_date...}` - Date-related tags when the stream started.
- `{download_date...}` - Date-related tags when the downloading started.
- `{media...}` - Media information-related tags.

For the media-related tags, the following elements are available.

- `{media_quality}` - Media Quality. (e.g. `1080p`)
- `{media_encoding_track_id}` - Encoding track ID. (e.g. `1080p`)
- `{media_video_profile}` - Video profile. (e.g. `high`)
- `{media_audio_profile}` - Audio profile. (e.g. `LC`)
- `{media_video_codec}` - Video codec. (e.g. `H264`)
- `{media_video_bitrate}` - Video bitrate as bit-per-second. (e.g. `8000000`)
- `{media_audio_bitrate}` - Audio bitrate as bit-per-second. (e.g. `192000`)
- `{media_video_framerate}` - Video frame rate as frame-per-second. (e.g. `60.0`)
- `{media_video_width}` - Video width as pixels. (e.g. `1920`)
- `{media_video_height}` - Video height as pixels. (e.g. `1080`)
- `{media_audio_sampling_rate}` - Audio sampling rate as Hertz. (e.g. `48000`)
- `{media_audio_channel}` - Audio channels. (e.g. `2`)
- `{media_video_dynamic_range}` - Video dynamic range. (e.g. `SDR`)

For the date-related tags, the detailed elements can be expanded as below.

- `{..._date}` - Date with `%Y%m%d%H%M%S` format. (e.g. `20240607014327`)
- `{..._date_year}` or `{..._date_year_full}` - Year with century as a decimal number. (e.g. `2024`)
- `{..._date_year_short}` - Year without century as a zero-padded decimal number. (e.g. `24`)
- `{..._date_month}` - Month as a zero-padded decimal number. (`01`, `02`, ..., `12`)
- `{..._date_month_full}` - Month as full name. (`January`, `February`, ..., `December`)
- `{..._date_month_short}` - Month as abbreviated name. (`Jan`, `Feb`, ..., `Dec`)
- `{..._date_day}` - Day of the month as a zero-padded decimal number. (`01`, `02`, ..., `31`)
- `{..._date_hour}` - Hour (24-hour clock) as a zero-padded decimal number. (`00`, `01`, ..., `23`)
- `{..._date_minute}` - Minute as a zero-padded decimal number. (`00`, `01`, ..., `59`)
- `{..._date_second}` - Second as a zero-padded decimal number. (`00`, `01`, ..., `59`)

## Setting Live Stream Detection Interval
By default, the detection interval for live streams is set to 60 seconds. To change this, use the following command: `n` can be any value from `10` to `300`. Therefore, the detection interval can be set in seconds, from 10 second to 5 minutes.

```powershell
ChzzkLiveDownloader --detect n
```

If you want to set this option to default, just use `--detect` like below.

```powershell
ChzzkLiveDownloader --detect
```

## Saving Thumbnail Images
To save thumbnail images separately, use the following command.

```powershell
ChzzkLiveDownloader --thumb save
```

To turn off this feature, use the following command.

```powershell
ChzzkLiveDownloader --thumb skip
```

## Saving Metadata
To save metadata based on live stream information, use the following command.

```powershell
ChzzkLiveDownloader --metadata save
```

To turn off this feature, use the following command.

```powershell
ChzzkLiveDownloader --metadata skip
```

## Setting Display Mode
By default, fluent details will be displayed. However, if you don't need the details, you can use the following command to supress them.

```powershell
ChzzkLiveDownloader -d quiet
ChzzkLiveDownloader --display quiet
```

The following display methods can be set with options of `--display` parameter.

- `quiet` - Suppress all details.
- `simple` - Show simplified details only.
- `fluent` - Show fluent details.
- `all` - Show all details.

If you want to set this option to default, just use `-d` or `--display` like below.

```powershell
ChzzkLiveDownloader -d
ChzzkLiveDownloader --display
```

## Finalization
By default, Chzzk Live Downloader downloads in MPEGTS format with a `.ts` extension during the live download stage and converts it to MPEG4 format with a `.mp4` extension in the finalization stage when the download is complete. However, the finalization methods can be set with `--final` option like below.

```powershell
ChzzkLiveDownloader --final all
```

The following finalization methods can be set with options of `--final` parameter.

- `none` - Just downloads transport stream files (`.ts`) and bypass converting stage. The transport stream files must be converted with the external converters for playing properly.
- `convert` - Converts transport stream files (`.ts`) to video files (`.mp4`), but don't remove transport stream files.
- `cleanup` - Converts transport stream files (`.ts`) to video files (`.mp4`), and clean up transport stream files.
- `cconvert` - Converts transport stream files (`.ts`) to video files (`.mp4`) with custom options by `--custom`, but don't remove transport stream files.
- `ccleanup` - Converts transport stream files (`.ts`) to video files (`.mp4`) with custom options by `--custom`, and clean up transport stream files.

```powershell
ChzzkLiveDownloader --final convert
```

If you want to set this option to default, just use `--final` like below.

```powershell
ChzzkLiveDownloader --final
```

### Custom Encoding During Finalization
When `cconvert` or `ccleanup` is specified for the `--final` parameter, you can use the `--custom` parameter to specify the encoding options for finalization. Since the encoding options themselves take the form of command-line arguments, you must wrap them using the `=` operator and double quotes (`"`), to prevent errors. For example, the following setting configures encoding with the `HEVC` codec:

```powershell
ChzzkLiveDownloader --final cconvert --custom="-c:v libx265 -crf 25 -c:a aac -b:a 128k"
```

You can also save the settings as a custom option set file and load it at runtime to apply the configurations.

```text
-c:v libx265 -crf 25 -c:a aac -b:a 128k
```

For example, if the file `hevc_sw_128k.set` contains the above settings, you can specify the file name as follows:

```powershell
ChzzkLiveDownloader --final cconvert --custom=hevc_sw_128k.set
```

If you want to set this option to default, just use `--custom` without options like below.

```powershell
ChzzkLiveDownloader --custom
```

You can also use the `--ext` parameter to specify a different file extension when the custom options require it.

```powershell
ChzzkLiveDownloader --final cconvert --custom=av1_nvenc_128k.set --ext=.av1
```

Please note that custom encoding is not recommended due to its suboptimal performance. For better results, consider using a dedicated external professional encoders.

## Setting Start Offset
You can use the following command to set amount of time to skip from the beginning of the stream.

```powershell
ChzzkLiveDownloader --offset 30
```

By default, the unit of time is seconds. However, you can also set through hours, minutes, seconds and milliseconds as follows.


```powershell
ChzzkLiveDownloader --offset 1:23:45.67
ChzzkLiveDownloader --offset 1h30m45.67s
```

## Setting Duration and Split Downloading
You can use the following command to set the stream duration to download. If the `--once` parameter is not specified, the downloaded stream will be split into the specified duration.

```powershell
ChzzkLiveDownloader --duration 3600
```

By default, the unit of time is seconds. However, you can also set through hours, minutes, seconds and milliseconds as follows.


```powershell
ChzzkLiveDownloader --duration 1:23:45.67
ChzzkLiveDownloader --duration 1h30m45.67s
```

## Setting Stream Retrieving Method
By default, ChzzkLiveDownloader retrieves stream information from the Chzzk Time Machine API to download the stream at the earliest possible time. However, you can set stream retrieving method based of your preferences with the following command.

```powershell
ChzzkLiveDownloader --stream standard
```

The following stream methods can be set with options of `--stream` parameter.

- `standard` - Retrieves the stream information from the Chzzk default API.
- `request-timemachine` - Retrieves the stream information from the Chzzk Time Machine API if possible.
- `force-timemachine` - Retrieves forcibly the stream information from the Chzzk Time Machine API even if the Time Machine is not enabled.

If you want to set this option to default, just use `--stream` like below.

```powershell
ChzzkLiveDownloader --stream
```

## Setting Working Directory
You can use the following command to specify the directory where required files are stored to work properly.

```powershell
ChzzkLiveDownloader --work work
```

If you want to set this option to default, just use `--work` without directory like below.

```powershell
ChzzkLiveDownloader --work
```

## Setting Output Directory
You can use the following command to specify the directory where downloaded files are finally saved.

```powershell
ChzzkLiveDownloader --out out
```

By default, all files are categorized and saved in subdirectories by streamer. If you want to save files without categorizing them by streamer, use the following command.

```powershell
ChzzkLiveDownloader --category none
```

If you want to set this option to default, just use `--out` and `--category` without options like below.

```powershell
ChzzkLiveDownloader --out --category
```

## Setting Temporary Directory
You can use the following command to specify the temporary directory where the files being downloaded are saved.

```powershell
ChzzkLiveDownloader --temp temp
```

If you want to set this option to default, just use `--temp` without directory like below.

```powershell
ChzzkLiveDownloader --temp
```

## Directory Specification
You can specify directories in several ways as follows.

```powershell
ChzzkLiveDownloader --temp temp
```

Specifies the `temp` directory under the current directory where the executable is located as the temporary directory. If the directory does not exist, it will be created.

```powershell
ChzzkLiveDownloader --work \Users\Username\Documents\chzzk_work
```

Specifies the `\Users\Username\Documents\chzzk_work` directory on the current drive as the working directory. If the directory does not exist, it will be created.

```powershell
ChzzkLiveDownloader --work C:\Users\Username\Documents\chzzk_work
```

Of course, you can specify the drive (e.g. `C:`) directly as shown above.

```powershell
ChzzkLiveDownloader --out \\192.168.0.1\chzzk\out
```

Specifies the `\\192.168.0.1\chzzk\out` directory on a network storage based on a UNC path as the output directory. If the directory does not exist, it will be created.

When saving files to network storage, you may need to enter a username and password to connect to the network storage. This information can be specified as follows.

```powershell
ChzzkLiveDownloader --work-user username --work-pass password
ChzzkLiveDownloader --out-user username --out-pass password
ChzzkLiveDownloader --temp-user username --temp-pass password
```

## Setting how to save when the target file already exists
By default, when a file with the same name already exists, the file is saved with `(n)` appended to its name. However, you can use the following command to overwrite the file or skip download itself instead.

```powershell
ChzzkLiveDownloader --exist overwrite
ChzzkLiveDownloader --exist skip
```

If you want to set this option to default, just use `--exist` like below.

```powershell
ChzzkLiveDownloader --exist
```

## Setting the threshold for stopping downloads when disk space is low
By default, downloads stop when the free space in the output directory and the temporary directory drops to 5% or less. To set a different free-space threshold, use the following command. The threshold can be specified as an absolute size or as a percentage (%), and the valid range is 1% to 50% of the total disk capacity.

```powershell
ChzzkLiveDownloader --threshold 20%
ChzzkLiveDownloader --threshold 1GB
ChzzkLiveDownloader --threshold 100M
ChzzkLiveDownloader --threshold 800MiB
```

When specifying the threshold as an absolute size, you can use SI units (KB, MB, GB...) or IEC units (KiB, MiB, GiB...). You may also specify prefixes only (K, Ki, M, Mi, G, Gi...). Of course, you can also specify the value in bytes without any unit.

To disable the feature that stops downloads based on free disk space, use the following command.

```powershell
ChzzkLiveDownloader --threshold -
```

If you want to set this option to default, just use `--threshold` like below.

```powershell
ChzzkLiveDownloader --threshold
```

## Setting Action When Saving Settings
All options are automatically saved to the configuration file by default.

However, by specifying an option after the `--settings` parameter, you can control whether to save the settings or view the current settings.

```powershell
ChzzkLiveDownloader --settings skip
```

- `default` – Saves the selected options to the configuration file and proceeds with the downloads.
- `skip` – Applies the selected options only to the current session without saving, and then proceeds with the downloads.
- `update` – Saves the selected options to the configuration file, displays the updated settings, and then quits.
- `show` – Ignores all selected options, displays the existing settings, and then quits.
- `quit` – Saves the selected options to the configuration file and then quits.

The following information is managed separately and is always saved regardless of the `--settings` parameter:

- All settings of saved streamer channel UIDs
- All settings of per-streamer target quality to download
- NAVER ID authentication key obtained from the Chzzk cookie (`NID_AUT`)
- NAVER ID session key obtained from the Chzzk cookie (`NID_SES`)

## Setting Action When Saving Settings
All options are always saved to configuration files by default. If you want to apply settings to current session only without saving, use the following command.

```powershell
ChzzkLiveDownloader --settings skip
```

However, the following information is always saved.


If you want to save the settings without downloading and exit, use the following command.

```powershell
ChzzkLiveDownloader --settings quit
```

## Plugins
Chzzk Live Downloader provides additional features tailored to the user's personal preferences and environment through plugins.

### Notification Plugins
By registering a notification plugin, you can easily monitor the operational status of Chzzk Live Downloader through an external solution. The following notification plugin is provided by default:

- `pn_slack` - Slack notification plugin
- `pn_telegram` - Telegram notification plugin

You can register a notification plugin using `--pnpath` parameter as shown below. Since only one plugin can be active at a time, if multiple registrations are made, only the last one will be active. After the plugin is registered, it applies to all future runs of Chzzk Live Downloader.

```powershell
ChzzkLiveDownloader --pnpath=pn_...
```

You can specify the language for the notification messages using `--pnlanguage` parameter as shown below.

```powershell
ChzzkLiveDownloader --pnpath=pn_... --pnlanguage=ko-KR
```

If the notification plugin supports Markdown or HTML formats, you can specify the text format of the notification messages using `--pntexttype` parameter as shown below.

```powershell
ChzzkLiveDownloader --pnpath=pn_... --pntexttype=html
```

You can also specify custom plugins as notification plugins. If additional parameters need to be passed to the plugin, use `--pnparams` parameter. In this case, `%M` should be used to indicate where the message should be inserted.

```powershell
ChzzkLiveDownloader --pnpath=userpn_... --pnparams="--user --message %M"
```

To unregister a notification plugin, just use `--pnpath` without specifying a plugin like below.

```powershell
ChzzkLiveDownloader --pnpath
```

## Resetting All Configurations
Over time, you may find that you've mixed things up and want to reset your settings. To reset all configurations, use the following command.

```powershell
ChzzkLiveDownloader --reset
```

This will reset the following information.

- All settings of saved streamer channel UIDs
- All settings of per-streamer target quality to download
- NAVER ID authentication key obtained from the Chzzk cookie (`NID_AUT`)
- NAVER ID session key obtained from the Chzzk cookie (`NID_SES`)
- Settings for live stream detection interval
- Settings for Saving thumbnail image
- Settings for displaying download details
- Settings for the finalization
- Settings for output and temporary directories

## Displaying Version Information
You can check the version information by using the following command.

```powershell
ChzzkLiveDownloader --version
```

## Getting help
You can use the following command to get simple parameter help.

```powershell
ChzzkLiveDownloader -h
ChzzkLiveDownloader --help
```

## Parameter precedence
Except `--reset`, `-h` and `--version`, the parameters can be used in any order as shown below. However, multiple copies of the same parameter cannot be assigned.

```powershell
ChzzkLiveDownloader -i 1 -u --detect 30 --bypass -s
```

The `-h` and `--version` parameters are processed only with the first one used, and then terminated immediately afterward. Therefore, the following command will output only the version information.

```powershell
ChzzkLiveDownloader --version -h
```

The `--reset` parameter resets the settings, ignoring any previously set values, then exits. Therefore, the `--detect` parameter will be ignored in the following command.

```powershell
ChzzkLiveDownloader --detect 30 --reset
```

## Recommended Initial Settings
The following settings are recommeneded for the first use. The following command will set working directory (`--work`), output directory (`--out`), temporary directory (`--temp`) at once to making it easy to organize the downloaded video files.

```powershell
ChzzkLiveDownloader --work work --out out --temp temp
```

## Controlling Externally Using JSON-RPC
Please read `how_to_control_chzzk_live_downloader.en-US.pdf` for detailed information.

## Contact Us
If you have any questions, bug reports, or improvement requests regarding the Chzzk Downloader Suite, please submit them through [GitHub](https://github.com/Choonholic/ChzzkDownloader/)‘s [Issues](https://github.com/Choonholic/ChzzkDownloader/issues/new) feature. We can respond to all languages; however, the languages we directly support are Korean, English, Japanese, and Chinese. For other languages, responses may not be fully accurate due to the use of machine translation.
