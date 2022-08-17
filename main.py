from website import *
import socket
import os

if __name__ == '__main__':
    app = create_app(os.path.dirname(os.path.realpath(__file__)))
    app.run(debug=True,
            port=80,
            host=socket.gethostbyname(socket.gethostname()))
