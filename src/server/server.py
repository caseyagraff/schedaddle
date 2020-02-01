"""
server.py
"""

import sys
import signal

from sanic import Sanic

from routes import Jobs

DEFAULT_SERVER_NAME = 'schedaddle'
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8087

app = Sanic(name=DEFAULT_SERVER_NAME)
app.add_route(Jobs.as_view(), '/jobs')

def start(host=DEFAULT_HOST, port=DEFAULT_PORT, num_workers=1):
    app.run(host=host, port=port)

if __name__ == '__main__':
    start()
