# json_rpc_test.py
# Test code for JSON-RPC features of Chzzk Downloader Suite
# Written by Choonholic, January 12, 2025

# Minimal Requirements: Chzzk Downloader Suite Version 1.36.0 or higher

import errno
import ipaddress
import json
import socket
import time
import select

def connect_nonblocking(sock, host, port, timeout=5.0):
    sock.setblocking(False)
    err = sock.connect_ex((host, port))

    if err not in (0, errno.EINPROGRESS, errno.EWOULDBLOCK, errno.EALREADY, 10035):
        raise OSError(err, f"connect_ex failed with {err}")

    _, writable, _ = select.select([], [sock], [], timeout)

    if not writable:
        raise TimeoutError("connect timeout")

    so_error = sock.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)

    if so_error != 0:
        raise OSError(so_error, f"connect failed with SO_ERROR={so_error}")

def send_request(host, port, request):
    print(f"Sending request to {host}:{port}")

    response = b''

    request_data = json.dumps(request).encode()

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            connect_nonblocking(client_socket, host, port, timeout=5.0)

            client_socket.sendall(request_data)

            data_received = False
            attempts = 0

            while True:
                readable, _, _ = select.select([client_socket], [], [], 0.1)
                if readable:
                    data = client_socket.recv(4096)
                    if data:
                        response += data
                        data_received = True
                        attempts = 0
                    else:
                        break
                else:
                    if data_received:
                        attempts += 1
                        if attempts >= 10:
                            break
                    else:
                        time.sleep(0.1)

        return response.decode(errors="replace")

    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    commands = [
        'get_channel',
        'get_clip',
        'get_info',
        'get_live',
        'get_settings',
        'get_status',
        'get_version',
        'get_video',
        'reload_settings',
        'skip_current',
        'stop_current',
        'resume_download',
        'quit_app',
        'quit_empty'
    ]
    exit_flag = False
    request = {}
    rpc_host = 'localhost'
    rpc_port = 62000

    while not exit_flag:
        host = input('host (default: localhost): ')

        if host == '' or host.lower() == 'localhost':
            host = 'localhost'
        elif ipaddress.ip_address(host):
            pass
        else:
            host = 'localhost'

        port = input('port (default: 62000): ')
        port = int(port) if port else 62000
        id = input('id: (default: 0): ')
        id = int(id) if id else 0
        bind_port = input('Bind id to port? [y/N] ')
        port = port + id if bind_port.startswith('y') else port

        while True:
            command = input("Command? ('help' to list commands) ")

            if command in commands:
                request = {
                    "jsonrpc": "2.0",
                    "method": command,
                    "id": id
                }

                response = send_request(host, port, request)

                print(response)
            elif command == 'help':
                print('Available commands:')

                for cmd in commands:
                    print(f' - {cmd}')

                print(' - restart')
                print(' - exit')
            elif command == 'restart':
                break
            elif command == 'exit':
                exit_flag = True
                break
            else:
                print(f'Invalid command: {command}')
