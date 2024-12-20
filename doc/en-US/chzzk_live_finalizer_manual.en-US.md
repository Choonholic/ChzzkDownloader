# Chzzk Live Finalizer
Finalizer for Chzzk live streams

<div style='text-align: center'>
<img src='../../img/screenshots/screenshot_chzzklivefinalizer.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

## Version
Version 1.4.1, December 20, 2024 10:00:00

## Usage
```powershell
ChzzkLiveFinalizer [-h] [--version] [-d [DISPLAY]] [--work [WORK]] [--work-user [WORK_USER]]
                   [--work-pass [WORK_PASS]] [--watch [WATCH]] [--watch-user [WATCH_USER]]
                   [--watch-pass [WATCH_PASS]] [--convert [CONVERT]] [--exist [EXIST]]
                   [--threshold [THRESHOLD]] [--rpcid [RPCID]] [--rpcport [RPCPORT]]
                   [--snapshot SNAPSHOT] [--startup [STARTUP]] [--settings [SETTINGS]] [--reset]
```

## Options
```
-h, --help                Show this help message
--version                 Show version information
-d, --display [DISPLAY]   Set process status display mode (quiet|simple|fluent|all)
--work [WORK]             Set working directory
--work-user [WORK_USER]   Set username to use when working directory is on remote network
--work-pass [WORK_PASS]   Set password to use when working directory is on remote network
--watch [WATCH]           Set watching directory
--watch-user [WATCH_USER] Set username to use when watching directory is on remote network
--watch-pass [WATCH_PASS] Set password to use when watching directory is on remote network
--convert [CONVERT]       Set convert parameters
--exist [EXIST]           Set how to save when the target file already exists (rename|skip|overwrite)
--threshold [THRESHOLD]   Set the threshold % for stopping downloads when disk space is low (disable: -, default: 10, 3-30)
--rpcid [RPCID]           Set ID of JSON-RPC server (default: 70)
--rpcport [RPCPORT]       Set port of JSON-RPC server (default: 65000, 49152-65300)
--snapshot SNAPSHOT       Save snapshot to a JSON file whenever changing status
--startup [STARTUP]       Set startup method (normal|fast)
--settings [SETTINGS]     Set action when saving settings (default|skip|quit)
--reset                   Reset all settings
```

## Example
```powershell
ChzzkLiveFinalizer --watch out
```

## Description
Chzzk Live Finalizer is a tool designed to handle final processing sequentially in a separate process, instead of Chzzk Live Downloader directly performing the final processing. Using Chzzk Live Finalizer ensures that live streams can be downloaded without interruption, even when they are broadcast in short intervals.

## Set Working Directory
You can use the following command to specify the directory where required files are stored to work properly.

```powershell
ChzzkLiveFinalizer --work work
```

If you want to set this option to default, just use `--work` without directory like below.

```powershell
ChzzkLiveFinalizer --work
```

## Set Watching Directory
Chzzk Live Finalizer watches the directory where stream files are saved and automatically performs the final conversion when new files are added. Use the following command to specify the directory to watch.

```powershell
ChzzkLiveFinalizer --watch out
```

If you want to set this option to default, just use `--watch` without directory like below.

```powershell
ChzzkLiveFinalizer --watch
```

## Directory Specification
You can specify directories in several ways as follows.

```powershell
ChzzkLiveFinalizer --work work
```

Specifies the `work` directory under the current directory where the executable is located as the working directory. If the directory does not exist, it will be created.

```powershell
ChzzkLiveFinalizer --watch \Users\Username\Documents\chzzk
```

Specifies the `\Users\Username\Documents\chzzk` directory on the current drive as the watching directory. If the directory does not exist, it will be created.

```powershell
ChzzkLiveFinalizer --watch C:\Users\Username\Documents\chzzk
```

Of course, you can specify the drive (e.g. `C:`) directly as shown above.

```powershell
ChzzkLiveFinalizer --watch \\192.168.0.1\chzzk
```

Specifies the `\\192.168.0.1\chzzk` directory on a network storage based on a UNC path as the watching directory. If the directory does not exist, it will be created.

When saving files to network storage, you may need to enter a username and password to connect to the network storage. This information can be specified as follows.

```powershell
ChzzkLiveFinalizer --work-user username --work-pass password
ChzzkLiveFinalizer --watch-user username --watch-pass password
```

### Set Finalize Encoding Parameters
You can set encoding parameters of finalization using the `--convert` option. For example, the following options enable `FFmpeg` to encode using the `H.265` codec:

```powershell
ChzzkLiveFinalizer --convert "-c:v libx265 -preset medium -crf 23 -c:a aac -b:a 128k"
```

If you want to set this option to default, just use `--convert` without options like below.

```powershell
ChzzkLiveFinalizer --convert
```

## Set How to Display Process Details
By default, fluent details will be displayed. However, if you don't need the details, you can use the following command to prevent them from being displayed.

```powershell
ChzzkLiveFinalizer -d quiet
ChzzkLiveFinalizer --display quiet
```

The following display methods can be set with options of `--display` parameter.

* `quiet` - Suppress all details.
* `fluent` - Show all fluent details.
* `default` - This option is the same as `fluent`.

If you want to set this option to default, just use `-d` or `--display` like below.

```powershell
ChzzkLiveFinalizer -d
ChzzkLiveFinalizer --display
```

## Set how to save when the target file already exists
By default, when a file with the same name already exists, the file is saved with `(n)` appended to its name. However, you can use the following command to overwrite the file or skip converting itself instead.

```powershell
ChzzkLiveFinalizer --exist overwrite
ChzzkLiveFinalizer --exist skip
```

If you want to set this option to default, just use `--exist` without like below.

```powershell
ChzzkLiveFinalizer --exist
```

## Set the threshold % for stopping finalization when disk space is low
By default, finalization will stop if the free space in the watching directory drops below 10%. To set the free disk space threshold, use the following command. The acceptable range is `3` to `30`.

```powershell
ChzzkLiveFinalizer --threshold 20
```

To disable the feature that stops finalization based on free disk space, use the following command.

```powershell
ChzzkLiveFinalizer --threshold -
```

If you want to set this option to default, just use `--threshold` without like below.

```powershell
ChzzkLiveFinalizer --threshold
```

## Set Action When Saving Settings
All options are always saved to configuration files by default. If you want to apply settings to current session only without saving, use the following command.

```powershell
ChzzkLiveFinalizer --settings skip
```

If you want to save the settings without finalization and exit, use the following command.

```powershell
ChzzkLiveFinalizer --settings quit
```

## Resetting All Configurations
Over time, you may find that you've mixed things up and want to reset your settings. To reset all configurations, use the following command.

```powershell
ChzzkLiveFinalizer --reset
```

This will reset the following information.

* Settings for displaying process details
* Settings for watching directory
* Settings for converting parameters

## Display Version Information
You can check the version information by using the following command.

```powershell
ChzzkLiveFinalizer --version
```

## Getting help
You can use the following command to get simple parameter help.

```powershell
ChzzkLiveFinalizer -h
ChzzkLiveFinalizer --help
```

## Parameter precedence
Except `--reset`, `-h` and `--version`, the parameters can be used in any order as shown below. However, multiple copies of the same parameter cannot be assigned.

```powershell
ChzzkLiveFinalizer -d quiet --watch out
```

The `-h` and `--version` parameters are processed only with the first one used, and then terminated immediately afterward. Therefore, the following command will output only the version information.

```powershell
ChzzkLiveFinalizer --version -h
```

The `--reset` parameter resets the settings, ignoring any previously set values, then exits. Therefore, the clip UID will be ignored in the following command.

```powershell
ChzzkLiveFinalizer --watch out --reset
```

## Controlling Externally Using JSON-RPC
Please read `how_to_control_chzzk_live_finalizer.en-US.pdf` for detailed information.

## Contact Us
If you have any questions, bug reports, or improvement requests regarding the Chzzk Downloader Suite, please submit them through [GitHub](https://github.com/Choonholic/ChzzkDownloader/)‘s [Issues](https://github.com/Choonholic/ChzzkDownloader/issues/new) feature. We can respond to all languages; however, the languages we directly support are Korean, English, Japanese, and Chinese. For other languages, responses may not be fully accurate due to the use of machine translation.
