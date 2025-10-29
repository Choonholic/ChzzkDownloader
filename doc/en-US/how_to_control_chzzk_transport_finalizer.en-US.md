# How To Control Chzzk Transport Finalizer Externally Using JSON-RPC

## Chzzk Downloader Suite JSON-RPC Specifications
Chzzk Downloader Suite supports single request of [JSON-RPC 2.0 Specifications](https://www.jsonrpc.org/specification) to control externally.

## How To Activate Server
Execute Chzzk Transport Finalizer with `--rpc` option.

## How To Connect To Server
Internal JSON-RPC server accepts socket connections.

* **Host IP Address** - Default address is `localhost`.
* **Port Number** - Default port number is `65000`. Use `--rpcport` option to change. (available range: `49152`~`65300`)
* **RPC ID** - Default ID is `70`. Use `--rpcid` option to change.

## How To Request
To request action from Chzzk Transport Finalizer, send the object like below through the socket.

```json
{
    "jsonrpc": "2.0",
    "method": "get_status",
    "id": 30
}
```

### Method List
* `get_info` - Retrieves all information at once.
* `get_version` – Retrieves the application version.
* `get_settings` – Retrieves the application settings.
* `get_status` – Retrieves the current status.
* `remove_item` - Remove a file from the waiting queue.
* `skip_current` - Stops finalizing the current file and skips to the next one.
* `set_settings` – Changes the application settings.
* `reload_settings` – Reloads the application settings from configuration file.
* `quit_app` – Stops the current download (if in progress) and exits the application.

## Responses
Chzzk Transport Finalizer returns responses in the following format.

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

## Sample Codes
Please refer to [samples](https://github.com/Choonholic/ChzzkDownloader/blob/main/samples/) in GitHub repository.
