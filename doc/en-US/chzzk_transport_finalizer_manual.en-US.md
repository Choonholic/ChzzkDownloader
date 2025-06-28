# Chzzk Transport Finalizer
Finalizer for Chzzk transport streams

<div style='text-align: center'>
<img src='../../img/screenshots/screenshot_chzzktransportfinalizer.png' />
<p><i>(This image may not reflect the latest information.)</i></p>
</div>

## Version
Version 1.24.0, June 28, 2025 00:00:00

## Prerequisites
* **[Mandatory]** Latest version of FFmpeg. (Requires FFmpeg 7.0 or higher)

## Usage
```powershell
ChzzkTransportFinalizer [-h] [--version] [-d [DISPLAY]] [--work [WORK]] [--work-user [WORK_USER]]
                        [--work-pass [WORK_PASS]] [--watch [WATCH]] [--watch-user [WATCH_USER]]
                        [--watch-pass [WATCH_PASS]] [--convert [CONVERT]] [--exist [EXIST]]
                        [--threshold [THRESHOLD]] [--rpc] [--rpcid [RPCID]] [--rpcport [RPCPORT]]
                        [--snapshot SNAPSHOT] [--metadata [METADATA]] [--startup [STARTUP]]
                        [--pnpath [PNPATH]] [--pnlanguage [PNLANGUAGE]] [--pnparams [PNPARAMS]]
                        [--pntexttype [PNTEXTTYPE]] [--settings [SETTINGS]] [--reset]
```

## Options
```
-h, --help                Show this help message
--version                 Show version information
-d, --display [DISPLAY]   Set display mode (quiet|simple|fluent|all)
--work [WORK]             Set working directory
--work-user [WORK_USER]   Set username to use when working directory is on remote network
--work-pass [WORK_PASS]   Set password to use when working directory is on remote network
--watch [WATCH]           Set watching directory
--watch-user [WATCH_USER] Set username to use when watching directory is on remote network
--watch-pass [WATCH_PASS] Set password to use when watching directory is on remote network
--convert [CONVERT]       Set convert parameters
--exist [EXIST]           Set how to save when the target file already exists (rename|skip|overwrite)
--threshold [THRESHOLD]   Set the threshold % for stopping downloads when disk space is low (disable: -, default: 10, 3-50)
--rpc                     Activate JSON-RPC server
--rpcid [RPCID]           Set ID of JSON-RPC server (default: 70)
--rpcport [RPCPORT]       Set port of JSON-RPC server (default: 65000, 49152-65300)
--snapshot SNAPSHOT       Save snapshot to a JSON file whenever changing status
--metadata [METADATA]     Save metadata or skip (save|skip)
--startup [STARTUP]       Set startup method (normal|fast)
--pnpath [PNPATH]         Set the path to the notification plugin
--pnlanguage [PNLANGUAGE] Set the language used by the notification plugin
--pnparams [PNPARAMS]     Set the parameters for the notification plugin
--pntexttype [PNTEXTTYPE] Set the text format used by the notification plugin (plain|markdown|html)
--settings [SETTINGS]     Set action when saving settings (default|skip|quit)
--reset                   Reset all settings
```

## Example
```powershell
ChzzkTransportFinalizer --work work --watch out
```

## Description
Chzzk Transport Finalizer is a tool designed to handle final processing sequentially in a separate process, instead of Chzzk Live Downloader and Chzzk Video Downloader directly performing the final processing. Using Chzzk Transport Finalizer ensures that live streams can be downloaded without interruption, even when they are broadcast in short intervals.

## Setting Working Directory
You can use the following command to specify the directory where required files are stored to work properly.

```powershell
ChzzkTransportFinalizer --work work
```

If you want to set this option to default, just use `--work` without directory like below.

```powershell
ChzzkTransportFinalizer --work
```

## Setting Watching Directory
Chzzk Transport Finalizer watches the directory where stream files are saved and automatically performs the final conversion when new files are added. Use the following command to specify the directory to watch.

```powershell
ChzzkTransportFinalizer --watch out
```

If you want to set this option to default, just use `--watch` without directory like below.

```powershell
ChzzkTransportFinalizer --watch
```

## Directory Specification
You can specify directories in several ways as follows.

```powershell
ChzzkTransportFinalizer --work work
```

Specifies the `work` directory under the current directory where the executable is located as the working directory. If the directory does not exist, it will be created.

```powershell
ChzzkTransportFinalizer --watch \Users\Username\Documents\chzzk
```

Specifies the `\Users\Username\Documents\chzzk` directory on the current drive as the watching directory. If the directory does not exist, it will be created.

```powershell
ChzzkTransportFinalizer --watch C:\Users\Username\Documents\chzzk
```

Of course, you can specify the drive (e.g. `C:`) directly as shown above.

```powershell
ChzzkTransportFinalizer --watch \\192.168.0.1\chzzk
```

Specifies the `\\192.168.0.1\chzzk` directory on a network storage based on a UNC path as the watching directory. If the directory does not exist, it will be created.

When saving files to network storage, you may need to enter a username and password to connect to the network storage. This information can be specified as follows.

```powershell
ChzzkTransportFinalizer --work-user username --work-pass password
ChzzkTransportFinalizer --watch-user username --watch-pass password
```

### Setting Finalize Encoding Parameters
You can set encoding parameters of finalization using the `--convert` option. When specifying options for the `--convert` parameter, since the option itself takes the form of a parameter, to avoid errors, please specify the option directly using the `=` operator and `"` quotes as shown below. For example, the following options enable `FFmpeg` to encode using the `H.265` codec:

```powershell
ChzzkTransportFinalizer --convert="-c:v libx265 -preset medium -crf 23 -c:a aac -b:a 128k"
```

If you want to set this option to default, just use `--convert` without options like below.

```powershell
ChzzkTransportFinalizer --convert
```

## Saving Metadata
To save metadata based on transport stream information, use the following command. Chzzk Transport Finalizer uses stream information exported as a `JSON` file along with the transport files from Chzzk Live Downloader or Chzzk Video Downloader. If this file is not created or has been deleted, the metadata will not be saved.

```powershell
ChzzkTransportFinalizer --metadata save
```

To turn off this feature, use the following command.

```powershell
ChzzkTransportFinalizer --metadata skip
```

## Setting Display Mode
By default, fluent details will be displayed. However, if you don't need the details, you can use the following command to supress them.

```powershell
ChzzkTransportFinalizer -d quiet
ChzzkTransportFinalizer --display quiet
```

The following display methods can be set with options of `--display` parameter.

* `quiet` - Suppress all details.
* `simple` - Show simplified details only.
* `fluent` - Show fluent details.
* `all` - Show all details.

If you want to set this option to default, just use `-d` or `--display` like below.

```powershell
ChzzkTransportFinalizer -d
ChzzkTransportFinalizer --display
```

## Setting how to save when the target file already exists
By default, when a file with the same name already exists, the file is saved with `(n)` appended to its name. However, you can use the following command to overwrite the file or skip converting itself instead.

```powershell
ChzzkTransportFinalizer --exist overwrite
ChzzkTransportFinalizer --exist skip
```

If you want to set this option to default, just use `--exist` without like below.

```powershell
ChzzkTransportFinalizer --exist
```

## Setting the threshold % for stopping finalization when disk space is low
By default, finalization will stop if the free space in the watching directory drops below 10%. To set the free disk space threshold, use the following command. The acceptable range is `3` to `30`.

```powershell
ChzzkTransportFinalizer --threshold 20
```

To disable the feature that stops finalization based on free disk space, use the following command.

```powershell
ChzzkTransportFinalizer --threshold -
```

If you want to set this option to default, just use `--threshold` without like below.

```powershell
ChzzkTransportFinalizer --threshold
```

## Setting Action When Saving Settings
All options are always saved to configuration files by default. If you want to apply settings to current session only without saving, use the following command.

```powershell
ChzzkTransportFinalizer --settings skip
```

If you want to save the settings without finalization and exit, use the following command.

```powershell
ChzzkTransportFinalizer --settings quit
```

## Plugins
Chzzk Transport Finalizer provides additional features tailored to the user's personal preferences and environment through plugins.

### Notification Plugins
By registering a notification plugin, you can easily monitor the operational status of Chzzk Transport Finalizer through an external solution. The following notification plugin is provided by default:

* `pn_slack` - Slack notification plugin
* `pn_telegram` - Telegram notification plugin

You can register a notification plugin using `--pnpath` parameter as shown below. Since only one plugin can be active at a time, if multiple registrations are made, only the last one will be active. After the plugin is registered, it applies to all future runs of Chzzk Transport Finalizer.

```powershell
ChzzkTransportFinalizer --pnpath=pn_...
```

You can specify the language for the notification messages using `--pnlanguage` parameter as shown below.

```powershell
ChzzkTransportFinalizer --pnpath=pn_... --pnlanguage=ko-KR
```

If the notification plugin supports Markdown or HTML formats, you can specify the text format of the notification messages using `--pntexttype` parameter as shown below.

```powershell
ChzzkTransportFinalizer --pnpath=pn_... --pntexttype=html
```

You can also specify custom plugins as notification plugins. If additional parameters need to be passed to the plugin, use `--pnparams` parameter. In this case, `%M` should be used to indicate where the message should be inserted.

```powershell
ChzzkTransportFinalizer --pnpath=userpn_... --pnparams="--user --message %M"
```

To unregister a notification plugin, just use `--pnpath` without specifying a plugin like below.

```powershell
ChzzkTransportFinalizer --pnpath
```

## Resetting All Configurations
Over time, you may find that you've mixed things up and want to reset your settings. To reset all configurations, use the following command.

```powershell
ChzzkTransportFinalizer --reset
```

This will reset the following information.

* Settings for displaying process details
* Settings for watching directory
* Settings for converting parameters

## Displaying Version Information
You can check the version information by using the following command.

```powershell
ChzzkTransportFinalizer --version
```

## Getting help
You can use the following command to get simple parameter help.

```powershell
ChzzkTransportFinalizer -h
ChzzkTransportFinalizer --help
```

## Parameter precedence
Except `--reset`, `-h` and `--version`, the parameters can be used in any order as shown below. However, multiple copies of the same parameter cannot be assigned.

```powershell
ChzzkTransportFinalizer -d quiet --watch out
```

The `-h` and `--version` parameters are processed only with the first one used, and then terminated immediately afterward. Therefore, the following command will output only the version information.

```powershell
ChzzkTransportFinalizer --version -h
```

The `--reset` parameter resets the settings, ignoring any previously set values, then exits. Therefore, the clip UID will be ignored in the following command.

```powershell
ChzzkTransportFinalizer --watch out --reset
```

## Controlling Externally Using JSON-RPC
Please read `how_to_control_chzzk_transport_finalizer.en-US.pdf` for detailed information.

## Contact Us
If you have any questions, bug reports, or improvement requests regarding the Chzzk Downloader Suite, please submit them through [GitHub](https://github.com/Choonholic/ChzzkDownloader/)‘s [Issues](https://github.com/Choonholic/ChzzkDownloader/issues/new) feature. We can respond to all languages; however, the languages we directly support are Korean, English, Japanese, and Chinese. For other languages, responses may not be fully accurate due to the use of machine translation.
