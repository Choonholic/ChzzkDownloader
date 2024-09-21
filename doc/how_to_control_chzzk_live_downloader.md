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
* `get_version` - Get application version of Chzzk Live Downloader.
* `get_status` - Get current status.
* `get_channel` - Get channel information.
* `get_live` - Get live stream information if available.
* `skip_current` - If a stream is currently being downloaded, the download will be canceled, and Chzzk Live Downloader will wait for the next stream.
* `quit_app` - If a stream is currently being downloaded, the task will be stopped, and Chzzk Live Downloader will exit.


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
        "version": "0.84",
        "description": "Downloader for Chzzk live streams",
        "developer": "Choonholic",
        "build_date": "September 18, 2024 00:00:00"
    },
    "id": 5
}

/* get_channel */
{
    "jsonrpc": "2.0",
    "result": {
        "name": "\ub9b4\uce74",
        "verified": true,
        "image": "https://nng-phinf.pstatic.net/...",
        "description": "",
        "followers": 133855
    },
    "id": 5
}

/* get_status */
{
    "jsonrpc": "2.0",
    "result": {
        "status": "Downloading",
        "info": "610.19 MiB, 0:00:24, 17.04 MiB/s"
    },
    "id": 5
}

/* get_live */
{
    "jsonrpc": "2.0",
    "result": {
        "title": "\ucd94\uc11d\ud2b9\uc9d1...",
        "category_type": "ETC",
        "category": "talk",
        "category_value": "talk",
        "open_date": "2024-09-17 12:59:36",
        "image_url": "https://livecloud-thumb.akamaized.net/...",
        "adult": false,
        "video_profile": "high",
        "audio_profile": "LC",
        "video_codec": "H264",
        "video_bitrate": 8192000,
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

/* quit_app */
{
    "jsonrpc": "2.0",
    "result": "Success",
    "id": 5
}
```

## Sample Codes
Please refer to [samples](https://github.com/Choonholic/ChzzkDownloader/blob/main/samples/) in GitHub repository.
