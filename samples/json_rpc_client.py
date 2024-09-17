import json
import socket
import time
import select

class JsonRpcClient:
    def __init__(self):
        self._host = 'localhost'
        self._port = 62000

    def send_request(self, request):
        response = b''

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                client_socket.setblocking(False)

                try:
                    client_socket.connect_ex((self._host, self._port))
                except BlockingIOError:
                    while True:
                        try:
                            client_socket.connect((self._host, self._port))
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
                            data = client_socket.recv(4096)  # Increased buffer size

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

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @host.setter
    def host(self, host):
        self._host = host

    @port.setter
    def port(self, port):
        self._port = port

if __name__ == "__main__":
    exit_flag = False
    client = JsonRpcClient()
    request = {}

    while not exit_flag:
        port = input('port (default: 62000): ')
        port = int(port) if port else 62000
        id = input('id: ')
        id = int(id) if id else 0
        bind_port = input('Bind id to port? [y/N] ')
        client.port = port + id if bind_port.startswith('y') else port

        print(f'Connected {client.host}:{client.port} with ID {id}...')

        while True:
            command = input('Command? [get_version/get_status/get_channel/get_live/get_video/get_clip/skip_current/quit_app/restart/exit] ')

            if command in ['get_version', 'get_status', 'get_channel', 'get_live', 'get_video', 'get_clip', 'skip_current', 'quit_app']:
                request = {
                    "jsonrpc": "2.0",
                    "method": command,
                    "id": id
                }

                response = client.send_request(request)

                print(response)
            elif command == 'restart':
                break
            elif command == 'exit':
                exit_flag = True
                break
            else:
                print(f'Invalid command: {command}')
