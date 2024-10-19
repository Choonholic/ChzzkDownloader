# How To Control Chzzk Live Downloader Externally Using JSON-RPC

## Chzzk Downloader Suite JSON-RPC Specifications
Chzzk Downloader Suite supports local single request of [JSON-RPC 2.0 Specifications](https://www.jsonrpc.org/specification) to control externally.

## How To Connect To Server
Internal JSON-RPC server accepts socket connections.

* **Host IP Address** - Default address is `localhost`.
* **Port Number** - Base port number (default: `62000`) + streamer ID. Use `--rpcbaseport` option to change. (available range: `49152`~`65300`)
* **RPC ID** - Using streamer ID automatically. Use `-i` option to change. (default: `0`)

If the streamer ID is `3`, port number is `62003` by default.

## How To Request
To request action from Chzzk Live Downloader, send the object like below through the socket.

```json
{
    "jsonrpc": "2.0",
    "method": "get_status",
    "id": 1
}
```

### Method List
* `get_version` – Retrieves the application version.
* `get_settings` – Retrieves the application settings.
* `get_channel` – Retrieves channel information.
* `get_channelex` – Retrieves extended channel information.
* `get_live` – Retrieves live stream information if a live stream is currently being downloaded.
* `get_status` – Retrieves the current status.
* `get_statusex` – Retrieves the current status. If a live stream is being downloaded, also returns the live stream information.
* `quit_app` – Stops the current download (if in progress) and exits the application.

## Responses
Chzzk Live Downloader returns responses in the following format.

```json
{
    "jsonrpc": "2.0",
    "result": "Success",
    "id": 1
}
```

### When The Request was Processed Successfully
* `result` - Results of the requested method.

### When The Request was not Processed Properly
* `error` - Indicates response is error.
* `code` - Error code.
* `message` - Error message.

## Examples
```json
/* get_version */
{
    "jsonrpc": "2.0",
    "result": {
        "name": "Chzzk Live Downloader",
        "version": "0.88",
        "description": "Downloader for Chzzk live streams",
        "developer": "Choonholic",
        "build_date": "October 12, 2024 00:00:00"
    },
    "id": 5
}

/* get_settings */
{
    "jsonrpc": "2.0",
    "result": {
        "detect": 60,
        "save_thumbnail": true,
        "display_method": 2,
        "stream_method": 1,
        "finalize_method": 2,
        "custom_options": null,
        "output_filename": "[{download_date}][{name}] {title}",
        "working_directory": "...", /* omitted */
        "output_directory": "...", /* omitted */
        "temp_directory": "...", /* omitted */
        "json_rpc_baseport": 62000
    },
    "id": 5
}

/* get_channel */
{
    "jsonrpc": "2.0",
    "result": {
        "uid": "458f6ec20b034f49e0fc6d03921646d2",
        "name": "\uc11c\uc0c8\ubd04\ub0e5 SEBOM",
        "verified": true,
        "image": "...", /* omitted */
        "description": "...", /* omitted */
        "followers": 161009,
        "target_quality": "best",
        "notification": 0,
        "local_path": "...", /* omitted */
        "local_image": "...", /* omitted */
    },
    "id": 5
}

/* get_channelex */
{
    "jsonrpc": "2.0",
    "result": {
        "uid": "458f6ec20b034f49e0fc6d03921646d2",
        "name": "\uc11c\uc0c8\ubd04\ub0e5 SEBOM",
        "verified": true,
        "image": "...", /* omitted */
        "description": "...", /* omitted */
        "followers": 161009,
        "target_quality": "best",
        "notification": 0,
        "local_path": "...", /* omitted */
        "local_image": "...", /* omitted */
        "status": "Downloading",
        "details": "713.77 MiB, 0:01:29, 1021.24 KiB/s",
        "title": "LOL \ube0c\ub860\uc988 \uac00\uc790",
        "category_type": "GAME",
        "category": "League_of_Legends",
        "category_value": "\ub9ac\uadf8 \uc624\ube0c \ub808\uc804\ub4dc",
        "open_date": "2024-10-11 00:44:13",
        "image_url": "...", /* omitted */
        "adult": false,
        "actual_quality": "1080p",
        "video_profile": "high",
        "audio_profile": "LC",
        "video_codec": "H264",
        "video_bitrate": 8704000,
        "audio_bitrate": 192000,
        "video_framerate": "60.0",
        "width": 1920,
        "height": 1080,
        "audio_sampling_rate": 48000,
        "audio_channel": 2,
        "video_dynamic_range": "SDR"
    },
    "id": 5
}

/* get_live */
{
    "jsonrpc": "2.0",
    "result": {
        "title": "LOL \ube0c\ub860\uc988 \uac00\uc790",
        "category_type": "GAME",
        "category": "League_of_Legends",
        "category_value": "\ub9ac\uadf8 \uc624\ube0c \ub808\uc804\ub4dc",
        "open_date": "2024-10-11 00:44:13",
        "image_url": "...", /* omitted */
        "adult": false,
        "actual_quality": "1080p",
        "video_profile": "high",
        "audio_profile": "LC",
        "video_codec": "H264",
        "video_bitrate": 8704000,
        "audio_bitrate": 192000,
        "video_framerate": "60.0",
        "width": 1920,
        "height": 1080,
        "audio_sampling_rate": 48000,
        "audio_channel": 2,
        "video_dynamic_range": "SDR"
    },
    "id": 5
}

/* get_status */
{
    "jsonrpc": "2.0",
    "result": {
        "status": "Downloading",
        "details": "726.22 MiB, 0:01:41, 1021.46 KiB/s"
    },
    "id": 5
}

/* get_statusex */
{
    "jsonrpc": "2.0",
    "result": {
        "status": "Downloading",
        "details": "726.22 MiB, 0:01:41, 1021.46 KiB/s",
        "title": "LOL \ube0c\ub860\uc988 \uac00\uc790",
        "category_type": "GAME",
        "category": "League_of_Legends",
        "category_value": "\ub9ac\uadf8 \uc624\ube0c \ub808\uc804\ub4dc",
        "open_date": "2024-10-11 00:44:13",
        "image_url": "...", /* omitted */
        "adult": false,
        "actual_quality": "1080p",
        "video_profile": "high",
        "audio_profile": "LC",
        "video_codec": "H264",
        "video_bitrate": 8704000,
        "audio_bitrate": 192000,
        "video_framerate": "60.0",
        "width": 1920,
        "height": 1080,
        "audio_sampling_rate": 48000,
        "audio_channel": 2,
        "video_dynamic_range": "SDR"
    },
    "id": 5
}

/* skip_current */
{
    "jsonrpc": "2.0",
    "result": "Success",
    "id": 5
}

/* quit_app */
{
    "jsonrpc": "2.0",
    "result": "Success",
    "id": 5
}
```

## Sample Codes
Please refer to [samples](https://github.com/Choonholic/ChzzkDownloader/blob/main/samples/) in GitHub repository.
