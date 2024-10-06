# chzzklauncher.py
# Chzzk Live Downloader Launcher Sample
# Written by Choonholic, September 21, 2024

# Minimal Requirements: Chzzk Live Downloader Version 0.85

import json
import select
import socket
import subprocess
import time

class ChzzkLaucherApplication:
    # Set to True when the verbose information of requests and responses is required
    SHOW_VERBOSE = False

    # Range for finding channels based on ports
    FIND_RANGE = 20

    # Add execute path to PATH environment or add executable path to this
    DOWNLOADER_PATH = 'ChzzkLiveDownloader.exe'
    RPC_HOST = 'localhost'
    RPC_BASE_PORT = 62000

    # JSON-RPC methods
    GET_VERSION = 'get_version'
    GET_SETTINGS = 'get_settings'
    GET_STATUS = 'get_status'
    GET_CHANNEL = 'get_channel'
    GET_LIVE = 'get_live'
    SKIP_CURRENT = 'skip_current'
    QUIT_APP = 'quit_app'

    def __init__(self):
        '''Initializing channels'''
        self._channels = []

    def send_request(self, host, port, request, ignore_errors=False):
        '''Send JSON-RPC request'''
        response = b''

        if self.SHOW_VERBOSE:
            print(f'RPC Server: {host}:{port}')

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
                            if not ignore_errors:
                                print(f"Error connecting to server: {e}")
                            return None

                request_data = json.dumps(request) + '\n'

                try:
                    client_socket.sendall(request_data.encode())
                except socket.error as e:
                    if not ignore_errors:
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
                        if not ignore_errors:
                            print(f"Error receiving data: {e}")
                        break
                    except BlockingIOError:
                        time.sleep(0.1)
        except Exception as e:
            if not ignore_errors:
                print(f"Unexpected error: {e}")

        try:
            return response.decode(errors='replace')
        except UnicodeDecodeError as e:
            if not ignore_errors:
                print(f"Error decoding response: {e}")
            return None

    def send_command(self, command, id, ignore_errors=False):
        '''Send a command to Chzzk Live Downloader instances'''
        request = {
            "jsonrpc": "2.0",
            "method": command,
            "id": id
        }

        if self.SHOW_VERBOSE:
            print(f'Request:  {request}')

        for _ in range(3):
            try:
                response = self.send_request(self.RPC_HOST, self.RPC_BASE_PORT + id, request, ignore_errors=ignore_errors)

                if self.SHOW_VERBOSE:
                    print(f'Response: {response}')

                return json.loads(response)
            except Exception:
                continue

        if not ignore_errors:
            raise Exception('All attempts to send command were failed.')

    def register_channels(self):
        '''Register all active channels to watch list'''
        try:
            print(f'Registering...')

            for id in range(self.FIND_RANGE):
                try:
                    response = self.get_channel(id, ignore_errors=True)

                    if response['result']:
                        channel = {
                            'id': id,
                            'name': response['result']['name'],
                            'status': None
                        }

                        self._channels.append(channel)
                except Exception:
                    continue

            self.get_all_channel_status()
        except Exception as e:
            print(f'An error occurred while finding channels: {e}')

    def find_available_id(self):
        '''Find an available id to add'''
        used_ids = { channel['id'] for channel in self._channels }

        id = 0

        while id in used_ids:
            id += 1

        return id

    def add_channel(self, id, uid):
        '''Add a channel to watch list'''
        try:
            response = self.run_instance(id, uid)

            channel = {
                'id': id,
                'name': response['result']['name'],
                'status': None
            }

            self._channels.append(channel)
            self.get_all_channel_status()
        except Exception as e:
            print(f'An error occurred while adding channel {id}: {e}')

    def remove_channel(self, id):
        '''Remove a channel from watch list'''
        passed_channels = [channel for channel in self._channels if channel['id'] != id]

        if len(passed_channels) != len(self._channels):
            self._channels = passed_channels

            self.send_command(self.QUIT_APP, id)

        self.get_all_channel_status()

    def get_channel(self, id, ignore_errors=False):
        '''Get information of the channel'''
        try:
            response = self.send_command(self.GET_CHANNEL, id, ignore_errors=ignore_errors)

            return response if response else None
        except Exception as e:
            if not ignore_errors:
                print(f'An error occurred while retrieving channel: {e}')

            return None

    def get_configurations(self, id):
        '''Get current configuration of Chzzk Live Downloader'''
        try:
            response = self.send_command(self.GET_SETTINGS, id)

            print(f'Configurations [{id}]: {response}')
        except Exception as e:
            print(f'An error occurred while retrieving configurations: {e}')

    def get_channel_status(self, id, channel_obj=None):
        '''Get current status of a channel'''
        try:
            if not object: # When not invoked by get_all_channel_status()
                for channel in self._channels:
                    if channel['id'] == id:
                        channel_obj = channel
                        break

            response = self.send_command(self.GET_STATUS, id)

            match response['result']['status']:
                case 'Waiting':
                    channel_obj['status'] = 'Waiting'
                case 'Downloading':
                    channel_obj['status'] = f'Downloading: {response['result']['info']}'
                case 'Finalizing':
                    channel_obj['status'] = f'Finalizing: {response['result']['info']}'

            print(f'[{channel_obj['id']}] {channel_obj['name']}: {channel_obj['status']}')
        except Exception as e:
            print(f'An error occurred while retrieving channel status: {e}')

    def get_all_channel_status(self):
        '''Get current status of all downloaders'''
        for channel in self._channels:
            self.get_channel_status(channel['id'], channel)

        print()

    def run_instance(self, id, uid):
        '''Run Chzzk Live Downloader and bind to Launcher'''
        print(f'Initiating a downloader [{id}]...')
        print()

        command = [
            self.DOWNLOADER_PATH,
            '-i', str(id),
            '-u', str(uid),
            '--rpcbaseport', str(self.RPC_BASE_PORT)
        ]

        try:
            subprocess.Popen(command, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP|subprocess.CREATE_NO_WINDOW)
            time.sleep(5) # Waiting for initialization for 5 seconds

            for _ in range(3): # Retrying 3 times for slower environments
                try:
                    response = self.send_command(self.GET_CHANNEL, id)

                    return response
                except Exception:
                    time.sleep(1)
                    continue
        except Exception as e:
            print(f'An error occurred while running downloader: {e}')

    def shutdown_all_downloader(self):
        '''Shutdown all instances'''
        print(f'Shutting down all downloaders...')

        for channel in self._channels:
            self.send_command(self.QUIT_APP, channel['id'])

    def main(self):
        '''Main loop'''
        print('Quick and Dirty Sample Launcher for Chzzk Live Downloader')
        print('Written by Choonholic, September 18, 2004.')
        print()

        self.register_channels() # Register all of currently active channels

        while True:
            command = input('Command? [l for list/a for add/d for delete/h for channel/c for configurations/s for status/t for shutdown all/x for exit] ').lower()

            match command:
                case str() if command.startswith('l'): # List all channels currently watching
                    print('Channels:')
                    print(self._channels)
                case str() if command.startswith('a'): # Add a channel and run a downloader instance
                    uid = input('Streamer UID or Live URL: ')

                    self.add_channel(self.find_available_id(), uid)
                case str() if command.startswith('r'): # Remove a channel
                    id = int(input('Streamer ID To Remove: '))

                    self.remove_channel(id)
                case str() if command.startswith('h'): # Get the channel information
                    id = int(input('Streamer ID To Get Channel Information: '))

                    self.get_channel(id)
                case str() if command.startswith('c'): # Get the configurations
                    id = int(input('Streamer ID To Get Configurations: '))

                    self.get_configurations(id)
                case str() if command.startswith('s'): # Get current status of all downloaders
                    self.get_all_channel_status()
                case str() if command.startswith('t'): # Shutdown all downloaders
                    self.shutdown_all_downloader()
                case str() if command.startswith('x'): # Exit Launcher
                    break

if __name__ == "__main__":
    # Entry Point
    app = ChzzkLaucherApplication()

    app.main()
