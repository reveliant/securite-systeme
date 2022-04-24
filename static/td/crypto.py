"""Compute HMAC for received data"""

from socketserver import ForkingMixIn, UnixStreamServer, StreamRequestHandler
import os
import hmac

class ForkingUnixServer(ForkingMixIn, UnixStreamServer):
    """Forking UNIX Stream Server"""

def main():
    """Main function"""
    # Read key from file
    key = b''
    with open(os.environ['KEY_PATH'], mode='rb') as key_file:
        key = key_file.read()
        print("Read {0} bytes HMAC key".format(len(key)))

    # Handler class factory with HMAC Key
    class UnixHandler(StreamRequestHandler):
        """Keyed Handler for UNIX Socket Requests"""
        def __init__(self, *args, **kwargs):
            """Add key to handler"""
            self.hmac_key = key
            super(UnixHandler, self).__init__(*args, **kwargs)

        def handle(self):
            """Handle a request"""
            print("Received request")
            data_hmac = hmac.new(self.hmac_key, self.rfile.readline(), digestmod='sha256')
            self.wfile.write(data_hmac.digest())

    # Start UNIX socket server
    with ForkingUnixServer(os.environ['SOCKET_PATH'], UnixHandler) as server:
        print("Listen on {0}".format(os.environ['SOCKET_PATH']))
        server.serve_forever()

if __name__ == '__main__':
    main()
