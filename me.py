import os
#os.popen('pip install pywhatkit')
#os.popen('pip install pyautogui')
#os.popen('pip install flask')
from cProfile import run
import pywhatkit
import flask
import pyautogui
import time
import datetime
import socket
import sys
from requests import get

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

ip = get('https://api.ipify.org').text
hostname = socket. gethostname()
local_ip = socket.gethostbyname(hostname)

print("Your computer name is: " + hostname, "Your local IP is: " + get_ip(), "Your public IP is: ", ip, sep="\n")
print(datetime.datetime.now(), "Server started at", get_ip(), ":8000")
print("\n")
print("Press Ctrl+C to stop the server")


#ipv4 = os.popen('ip addr show eth0 | grep "\<inet\>" | awk \'{ print $2 }\' | awk -F "/" \'{ print $1 }\'').read().strip()
#print(ipv4)


class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

with HiddenPrints():
  pywhatkit.start_server()
