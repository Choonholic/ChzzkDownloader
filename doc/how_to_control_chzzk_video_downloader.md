# How To Control Chzzk Video Downloader Externally Using JSON-RPC

## Chzzk Downloader Suite JSON-RPC Specifications
Chzzk Downloader Suite supports local single request of [JSON-RPC 2.0 Specifications](https://www.jsonrpc.org/specification) to control externally.

## How To Connect To Server
Internal JSON-RPC server accepts socket connections.

* **Host IP Address** - Default address is `localhost`.
* **Port Number** - Default port number is `63000`. Use `--rpcport` option to change. (available range: `49152`~`65300`)
* **RPC ID** - Default ID is `30`. Use `--rpcid` option to change.

## How To Request
To request action from Chzzk Live Downloader, send the object like below through the socket.

```json
{
    "jsonrpc": "2.0",
    "method": "get_status",
    "id": 30
}
```

### Method List
* `get_version` - Get application version.
* `get_settings` - Get application settings.
* `get_status` - Get current status.
* `get_channel` - Get channel information.
* `get_video` - Get video information which is currently downloading.
* `set_setings` - Set application settings.
* `quit_app` - Stop downloading if a clip is currently being downloaded, and exit.

## Responses
Chzzk Live Downloader returns responses in the following format.

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
        "version": "0.84",
        "description": "Downloader for Chzzk replay videos",
        "developer": "Choonholic",
        "build_date": "September 18, 2024 00:00:00"
    },
    "id": 30
}

/* get_channel */
{
    "jsonrpc": "2.0",
    "result": {
        "name": "\uc720\uc789\uc5b4",
        "verified": false,
        "image": "https://nng-phinf.pstatic.net/...",
        "description": "\ubaa9\uc18c\ub9ac...",
        "followers": 1091
    },
    "id": 30
}

/* get_status */
{
    "jsonrpc": "2.0",
    "result": {
        "status": "Downloading",
        "info": " 48%, 267MiB, 551MiB, 65MiB, 00:00:04"
    },
    "id": 30
}

/* get_video */
{
    "jsonrpc": "2.0",
    "result": {
        "index": 2,
        "title": "09/22...",
        "thumbnail_url": "https://nng-phinf.pstatic.net/...",
        "duration": 561,
        "publish_date": "2024-07-22 12:03:22",
        "category": "Minecraft",
        "category_type": "GAME",
        "category_value": "\ub9c8\uc778\ud06c\ub798\ud504\ud2b8",
        "adult": false,
        "quality": "1080p",
        "width": 1920,
        "height": 1080,
        "video_framerate": "60",
        "bitrate": 8420352,
        "video_codec": "avc1.640028,mp4a.40.2",
        "filesize": 578098953
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
