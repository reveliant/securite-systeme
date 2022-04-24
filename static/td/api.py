"""Pass JSON 'data' to HMAC service"""

from binascii import hexlify
import socket
from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def home_page():
    """Useless home page"""
    return "<p>Crypto</p>"

@app.route("/hmac", methods=['POST'])
def build_mac():
    """Handle HMAC requests"""
    data = request.get_json()

    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect(os.environ['SOCKET_PATH'])
        sock.sendall(bytes(data['data'] + '\n', 'utf-8'))

        # Receive data from the server and shut down
        return {
            "hmac": hexlify(sock.recv(1024))
        }