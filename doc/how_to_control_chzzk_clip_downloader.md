# How To Control Chzzk Clip Downloader Externally Using JSON-RPC

## Chzzk Downloader Suite JSON-RPC Specifications
Chzzk Downloader Suite supports local single request of [JSON-RPC 2.0 Specifications](https://www.jsonrpc.org/specification) to control externally.

## How To Connect To Server
Internal JSON-RPC server accepts socket connections.

* **Host IP Address** - Default address is `localhost`.
* **Port Number** - Default port number is `64000`. Use `--rpcport` option to change. (available range: `49152`~`65300`)
* **RPC ID** - Default ID is `50`. Use `--rpcid` option to change.

## How To Request
To request action from Chzzk Clip Downloader, send the object like below through the socket.

```json
{
    "jsonrpc": "2.0",
    "method": "get_status",
    "id": 50
}
```

### Method List
* `get_version` – Retrieves the application version.
* `get_settings` – Retrieves the application settings.
* `get_channel` – Retrieves channel information.
* `get_channelex` – Retrieves extended channel information.
* `get_clip` – Retrieves clip information if a clip is currently being downloaded.
* `get_status` – Retrieves the current status.
* `get_statusex` – Retrieves the current status. If a clip is being downloaded, also returns the clip information.
* `quit_app` – Stops the current download (if in progress) and exits the application.

## Responses
Chzzk Clip Downloader returns responses in the following format.

```json
{
    "jsonrpc": "2.0",
    "result": "Success",
    "id": 50
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
        "name": "Chzzk Clip Downloader",
        "version": "0.88",
        "description": "Downloader for Chzzk clips",
        "developer": "Choonholic",
        "build_date": "October 11, 2024 00:00:00"
    },
    "id": 50
}

/* get_settings */
{
    "jsonrpc": "2.0",
    "result": {
        "save_thumbnail": false,
        "display_method": 2,
        "output_filename": "[{download_date}][{name}] {title}",
        "working_directory": "...", /* omitted */
        "output_directory": "...", /* omitted */
        "temp_directory": "...", /* omitted */
        "json_rpc_id": 50,
        "json_rpc_port": 64000
    },
    "id": 50
}

/* get_channel */
{
    "jsonrpc": "2.0",
    "result": {
        "name": "\ub9c8\ub808\ud50c\ub85c\uc2a4",
        "verified": false,
        "image": "...", /* omitted */
        "description": "...", /* omitted */
        "followers": 32040
    },
    "id": 50
}

/* get_channelex */
{
    "jsonrpc": "2.0",
    "result": {
        "name": "\ub9c8\ub808\ud50c\ub85c\uc2a4",
        "verified": false,
        "image": "...", /* omitted */
        "description": "...", /* omitted */
        "followers": 32040,
        "status": "Downloading",
        "details": "93%, 4.6MiB, 4.9MiB, 118KiB, 00:00:02",
        "index": 2,
        "title": "\"Adele - Skyfall\"",
        "thumbnail_url": "...", /* omitted */
        "duration": 60,
        "created_date": "2024-09-05 00:19:05",
        "adult": false,
        "actual_quality": "720p",
        "width": 720,
        "height": 1280,
        "video_bitrate": 497.0,
        "audio_bitrate": 192.0,
        "video_codec": "AVC",
        "file_size": 5209025
    },
    "id": 50
}

/* get_clip */
{
    "jsonrpc": "2.0",
    "result": {
        "index": 3,
        "title": "\uc5b4\uc774\ucfe0",
        "thumbnail_url": "...", /* omitted */
        "duration": 60,
        "created_date": "2024-08-26 10:14:46",
        "adult": false,
        "actual_quality": "720p",
        "width": 720,
        "height": 1280,
        "video_bitrate": 1283.0,
        "audio_bitrate": 192.0,
        "video_codec": "AVC",
        "file_size": 11101280
    },
    "id": 50
}

/* get_status */
{
    "jsonrpc": "2.0",
    "result": {
        "status": "Downloading",
        "details": "37%, 3.9MiB, 10MiB, 1.2MiB, 00:00:05"
    },
    "id": 50
}

/* get_statusex */
{
    "jsonrpc": "2.0",
    "result": {
        "status": "Downloading",
        "details": "51%, 5.4MiB, 10MiB, 605KiB, 00:00:08",
        "index": 3,
        "title": "\uc5b4\uc774\ucfe0",
        "thumbnail_url": "...", /* omitted */
        "duration": 60,
        "created_date": "2024-08-26 10:14:46",
        "adult": false,
        "actual_quality": "720p",
        "width": 720,
        "height": 1280,
        "video_bitrate": 1283.0,
        "audio_bitrate":192.0,
        "video_codec": "AVC",
        "file_size": 11101280
    },
    "id": 50
}

/* quit_app */
{
    "jsonrpc": "2.0",
    "result": "Success",
    "id": 50
}
```

## Sample Codes
Please refer to [samples](https://github.com/Choonholic/ChzzkDownloader/blob/main/samples/) in GitHub repository.
