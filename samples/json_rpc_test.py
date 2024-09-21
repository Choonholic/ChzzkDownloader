# json_rpc_test.py
# Test code for JSON-RPC features of Chzzk Downloader Suite
# Written by Choonholic, September 21, 2024

# Minimal Requirements: Chzzk Downloader Suite Version 0.85 or higher

import json
import socket
import time
import select

def send_request(host, port, request):
    response = b''

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            client_socket.setblocking(False)

            try:
                client_socket.connect_ex((host, port))
            except BlockingIOError:
                while True:
                    try:
                        client_socket.connect((host, port))
                        break
                    except BlockingIOError:
                        time.sleep(0.1)
                    except socket.error as e:
                        print(f"Error connecting to server: {e}")
                        return None

            request_data = json.dumps(request) + '\n'

            try:
                client_socket.sendall(request_data.encode())
            except socket.error as e:
                print(f"Error sending request: {e}")
                return None

            data_received = False
            attempts = 0

            while True:
                try:
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
                except socket.error as e:
                    print(f"Error receiving data: {e}")
                    break
                except BlockingIOError:
                    time.sleep(0.1)
    except Exception as e:
        print(f"Unexpected error: {e}")

    try:
        return response.decode(errors='replace')
    except UnicodeDecodeError as e:
        print(f"Error decoding response: {e}")
        return None

if __name__ == "__main__":
    exit_flag = False
    request = {}
    rpc_host = 'localhost'
    rpc_port = 62000

    while not exit_flag:
        port = input('port (default: 62000): ')
        port = int(port) if port else 62000
        id = input('id: ')
        id = int(id) if id else 0
        bind_port = input('Bind id to port? [y/N] ')
        rpc_port = port + id if bind_port.startswith('y') else port

        while True:
            command = input('Command? [get_version/get_settings/get_channel/get_status/get_live/get_video/get_clip/skip_current/quit_app/restart/exit] ')

            if command in ['get_version', 'get_settings', 'get_channel', 'get_status', 'get_live', 'get_video', 'get_clip', 'skip_current', 'quit_app']:
                request = {
                    "jsonrpc": "2.0",
                    "method": command,
                    "id": id
                }

                response = send_request(rpc_host, rpc_port, request)

                print(response)
            elif command == 'restart':
                break
            elif command == 'exit':
                exit_flag = True
                break
            else:
                print(f'Invalid command: {command}')
