# json_rpc_test.py
# Test code for JSON-RPC features of Chzzk Downloader Suite
# Written by Choonholic, January 18, 2025
#
# Minimal Requirements: Chzzk Downloader Suite Version 1.37.0 or higher

import errno
import ipaddress
import json
import socket
import select

MAX_RESPONSE_BYTES = 4 * 1024 * 1024

def connect_nonblocking(sock, host, port, timeout=5.0):
    sock.setblocking(False)

    err = sock.connect_ex((host, port))

    if err not in (0, errno.EINPROGRESS, errno.EWOULDBLOCK, errno.EALREADY, 10035):
        raise OSError(err, f"connect_ex failed with {err}")

    _, writable, _ = select.select([], [sock], [], timeout)

    if not writable:
        so_error = sock.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)

        raise TimeoutError(f"connect timeout (SO_ERROR={so_error})")

    so_error = sock.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)

    if so_error != 0:
        raise OSError(so_error, f"connect failed with SO_ERROR={so_error}")


def _scan_complete_json_prefix(s: str) -> int:
    n = len(s)
    i = 0

    while i < n and s[i].isspace():
        i += 1

    if i >= n:
        return 0

    first = s[i]
    if first not in "{[":
        return 0

    depth = 0
    in_string = False
    escape = False

    while i < n:
        ch = s[i]

        if escape:
            escape = False
            i += 1
            continue

        if ch == "\\":
            escape = True
            i += 1
            continue

        if ch == '"':
            in_string = not in_string
            i += 1
            continue

        if in_string:
            i += 1
            continue

        if ch in "{[":
            depth += 1
        elif ch in "}]":
            depth -= 1

            if depth == 0:
                return i + 1

            if depth < 0:
                return 0

        i += 1

    return 0

def send_request(host, port, request_obj, connect_timeout=5.0, recv_timeout=5.0):
    print(f"Sending request to {host}:{port}")

    request_data = json.dumps(request_obj).encode("utf-8")
    buffer = b""

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            connect_nonblocking(client_socket, host, port, timeout=connect_timeout)
            client_socket.setblocking(True)
            client_socket.settimeout(recv_timeout)
            client_socket.sendall(request_data)

            while True:
                chunk = client_socket.recv(8192)

                if not chunk:
                    break

                buffer += chunk

                if len(buffer) > MAX_RESPONSE_BYTES:
                    raise ValueError("Response too large")

                text = buffer.decode("utf-8", errors="replace")
                end = _scan_complete_json_prefix(text)

                if end > 0:
                    return text[:end].strip()

        return buffer.decode("utf-8", errors="replace") if buffer else None
    except socket.timeout:
        print("Error: recv timeout")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def print_pretty_response(response_text: str):
    try:
        obj = json.loads(response_text)

        print(json.dumps(obj, indent=2, ensure_ascii=False))
    except Exception:
        print(response_text)

if __name__ == "__main__":
    commands = [
        "get_channel",
        "get_clip",
        "get_info",
        "get_live",
        "get_settings",
        "get_status",
        "get_version",
        "get_video",
        "reload_settings",
        "skip_current",
        "stop_current",
        "resume_download",
        "quit_app",
        "quit_empty",
    ]

    exit_flag = False
    rpc_host = "localhost"
    rpc_port = 62000

    while not exit_flag:
        host = input("host (default: localhost): ").strip()

        if host == "" or host.lower() == "localhost":
            host = "localhost"
        else:
            try:
                ipaddress.ip_address(host)
            except ValueError:
                host = "localhost"

        port_str = input("port (default: 62000): ").strip()
        port = int(port_str) if port_str else rpc_port

        id_str = input("id (default: 0): ").strip()
        req_id = int(id_str) if id_str else 0

        bind_port = input("Bind id to port? [y/N] ").strip().lower()

        if bind_port.startswith("y"):
            port = port + req_id

        while True:
            command = input("Command? ('help' to list commands) ").strip()

            if command in commands:
                request_obj = {
                    "jsonrpc": "2.0",
                    "method": command,
                    "id": req_id,
                }

                response = send_request(host, port, request_obj)

                if response is None:
                    print("(no response)")
                else:
                    print_pretty_response(response)

            elif command == "help":
                print("Available commands:")

                for cmd in commands:
                    print(f" - {cmd}")

                print(" - restart")
                print(" - exit")

            elif command == "restart":
                break

            elif command == "exit":
                exit_flag = True
                break

            else:
                print(f"Invalid command: {command}")
