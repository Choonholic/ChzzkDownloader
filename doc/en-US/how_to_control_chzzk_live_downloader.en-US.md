# How To Control Chzzk Live Downloader Externally Using JSON-RPC

## Chzzk Downloader Suite JSON-RPC Specifications
Chzzk Downloader Suite supports single request of [JSON-RPC 2.0 Specifications](https://www.jsonrpc.org/specification) to control externally.

## How To Activate Server
Execute Chzzk Live Downloader with `--rpc` option.

## How To Connect To Server
Internal JSON-RPC server accepts socket connections.

- **Host IP Address** - Default address is `localhost`. If you want to allow connections from outside the local PC, set the `--rpcexpose` option to `open` to expose the server externally. In this case, you may need to modify the Windows Defender Firewall settings as shown in the following image.
- **Port Number** - Base port number (default: `62000`) + the channel ID. Use `--rpcbaseport` option to change. (available range: `49152`~`65300`)
- **RPC ID** - Using the channel ID automatically. Use `-i` option to change. (default: `0`)

If the base port is `62000` and the the channel ID is `3`, the actual port number is set to `62003`.

<div style='text-align: center'>
<img src='../../img/screenshots/cld_firewall.png' />
<p><i>(This image may vary depending on the operating system or system environment.)</i></p>
</div>

## How To Request
To request action from Chzzk Live Downloader, send the object like below through the TCP socket.

```json
{
    "jsonrpc": "2.0",
    "method": "get_status",
    "id": 0
}
```

### Method List
- `get_channel` – Retrieves channel information.
- `get_info` - Retrieves all information at once.
- `get_live` – Retrieves live stream information if a live stream is currently being downloaded.
- `get_settings` – Retrieves the application settings.
- `get_status` – Retrieves the current status.
- `get_version` – Retrieves the application version.
- `quit_app` – Stops the current download (if in progress) and exits the application.
- `reload_settings` – Reloads the application settings from configuration file.
- `resume_download` - Resumed downloading the forcibly stopped stream.
- `set_settings` – Changes the application settings.
- `skip_current` - Skips the current stream and waiting the next one.
- `stop_current` - Stops downloading the current stream and waiting the next one.

## Responses
Chzzk Live Downloader returns responses in the following format.

```json
{
    "jsonrpc": "2.0",
    "result": {
        "timestamp": "2026-01-01T00:00:00.000Z",
        "...": "...",
    },
    "id": 0
}
```

### When The Request was Processed Successfully
- `result` - The results of the requested method.
- `timestamp` - The response time based on UTC.

### When The Request was not Processed Properly
- `error` - Indicates response is error.
- `code` - The error code.
- `message` - The error message.

## Sample Codes
Please refer to [samples](https://github.com/Choonholic/ChzzkDownloader/blob/main/samples/) in GitHub repository.
