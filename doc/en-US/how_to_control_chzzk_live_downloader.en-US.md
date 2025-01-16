# How To Control Chzzk Live Downloader Externally Using JSON-RPC

## Chzzk Downloader Suite JSON-RPC Specifications
Chzzk Downloader Suite supports single request of [JSON-RPC 2.0 Specifications](https://www.jsonrpc.org/specification) to control externally.

## How To Activate Server
Execute Chzzk Live Downloader with `--rpc` option.

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
* `get_info` - Retrieves all information at once.
* `get_version` – Retrieves the application version.
* `get_settings` – Retrieves the application settings.
* `get_channel` – Retrieves channel information.
* `get_live` – Retrieves live stream information if a live stream is currently being downloaded.
* `get_status` – Retrieves the current status.
* `set_settings` – Changes the application settings.
* `reload_settings` – Reloads the application settings from configuration file.
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

## Sample Codes
Please refer to [samples](https://github.com/Choonholic/ChzzkDownloader/blob/main/samples/) in GitHub repository.
