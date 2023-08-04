import os
import subprocess
from flask import Flask, request
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

def wake_on_lan():
    mac_address = os.getenv("MAC_ADDRESS")
    if mac_address:
        subprocess.run(['wakeonlan', mac_address])
    else:
        print("Error: No se encontró la dirección MAC en el archivo .env")

@app.route('/webhook', methods=['GET', 'POST'])
def webhook_handler():

    wake_on_lan()
    return 'Ordenador encendido mediante Wake On LAN.', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5454)
