# How To Control Chzzk Video Downloader Externally Using JSON-RPC

## Chzzk Downloader Suite JSON-RPC Specifications
Chzzk Downloader Suite supports local single request of [JSON-RPC 2.0 Specifications](https://www.jsonrpc.org/specification) to control externally.

## How To Connect To Server
Internal JSON-RPC server accepts socket connections.

* **Host IP Address** - Default address is `localhost`.
* **Port Number** - Default port number is `63000`. Use `--rpcport` option to change. (available range: `49152`~`65300`)
* **RPC ID** - Default ID is `30`. Use `--rpcid` option to change.

## How To Request
To request action from Chzzk Video Downloader, send the object like below through the socket.

```json
{
    "jsonrpc": "2.0",
    "method": "get_status",
    "id": 30
}
```

### Method List
* `get_version` – Retrieves the application version.
* `get_settings` – Retrieves the application settings.
* `get_channel` – Retrieves channel information.
* `get_channelex` – Retrieves extended channel information.
* `get_video` – Retrieves replay video information if a replay video is currently being downloaded.
* `get_status` – Retrieves the current status.
* `get_statusex` – Retrieves the current status. If a replay video is being downloaded, also returns the replay video information.
* `quit_app` – Stops the current download (if in progress) and exits the application.

## Responses
Chzzk Video Downloader returns responses in the following format.

```json
{
    "jsonrpc": "2.0",
    "result": "Success",
    "id": 30
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
        "name": "Chzzk Video Downloader",
        "version": "0.88",
        "description": "Downloader for Chzzk replay videos",
        "developer": "Choonholic",
        "build_date": "October 11, 2024 00:00:00"
    },
    "id": 30
}

/* get_settings */
{
    "jsonrpc": "2.0",
    "result": {
        "quality": null,
        "save_thumbnail": true,
        "display_method": 2,
        "output_filename": "[{live_date}][{name}] {title}",
        "working_directory": "...", /* omitted */
        "output_directory": "...", /* omitted */
        "temp_directory": "...", /* omitted */
        "json_rpc_id": 30,
        "json_rpc_port": 63000
    },
    "id": 30
}

/* get_channel */
{
    "jsonrpc": "2.0",
    "result": {
        "name": "\uc694\ub8f0\ub808\ud788",
        "verified": true,
        "image": "..." /* omitted */
    },
    "id": 30
}

/* get_channelex */
{
    "jsonrpc": "2.0",
    "result": {
        "name": "\uc694\ub8f0\ub808\ud788",
        "verified": true,
        "image": "...", /* omitted */
        "status": "Downloading",
        "details": "12%, 5.0GiB, 39GiB, 52MiB, 00:11:04",
        "index": 0,
        "title": "\ud6c8\uc218\ub300\ud658\uc601",
        "thumbnail_url": "...", /* omitted */
        "duration": 40951,
        "publish_date": "2024-10-06 02:33:24",
        "category": "Alien_Isolation",
        "category_type": "GAME",
        "category_value": "\uc5d0\uc774\ub9ac\uc5b8",
        "adult": false,
        "actual_quality": "1080p",
        "width": 1920,
        "height": 1080,
        "video_framerate": "60",
        "bitrate": 8388608,
        "video_codec": "avc1.640028,mp4a.40.2",
        "filesize": 41973095131
    },
    "id": 30
}

/* get_video */
{
    "jsonrpc": "2.0",
    "result": {
        "index": 0,
        "title": "\ud6c8\uc218\ub300\ud658\uc601",
        "thumbnail_url": "...", /* omitted */
        "duration": 40951,
        "publish_date": "2024-10-06 02:33:24",
        "category": "Alien_Isolation",
        "category_type": "GAME",
        "category_value": "\uc5d0\uc774\ub9ac\uc5b8",
        "adult": false,
        "actual_quality": "1080p",
        "width": 1920,
        "height": 1080,
        "video_framerate": "60",
        "bitrate": 8388608,
        "video_codec": "avc1.640028,mp4a.40.2",
        "filesize": 41973095131
    },
    "id": 30
}

/* get_status */
{
    "jsonrpc": "2.0",
    "result": {
        "status": "Downloading",
        "details": "14%, 5.7GiB, 39GiB, 76MiB, 00:07:23"
    },
    "id": 30
}

/* get_statusex */
{
    "jsonrpc": "2.0",
    "result": {
        "status": "Downloading",
        "details": "0%, 210MiB, 39GiB, 4.9MiB, 02:14:59",
        "index": 0,
        "title": "\ud6c8\uc218\ub300\ud658\uc601",
        "thumbnail_url": "...", /* omitted */
        "duration": 40951,
        "publish_date": "2024-10-06 02:33:24",
        "category": "Alien_Isolation",
        "category_type": "GAME",
        "category_value": "\uc5d0\uc774\ub9ac\uc5b8",
        "adult": false,
        "actual_quality": "1080p",
        "width": 1920,
        "height": 1080,
        "video_framerate": "60",
        "bitrate": 8388608,
        "video_codec": "avc1.640028,mp4a.40.2",
        "filesize": 41973095131
    },
    "id": 30
}

/* quit_app */
{
    "jsonrpc": "2.0",
    "result": "Success",
    "id": 30
}
```

## Sample Codes
Please refer to [samples](https://github.com/Choonholic/ChzzkDownloader/blob/main/samples/) in GitHub repository.
