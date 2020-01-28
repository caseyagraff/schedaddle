"""
server.py
"""

import sys
import multiprocessing
import threading
from queue import Queue
import socket
import signal

from job import Job

KILL_SOCKET = 'KILL_SOCKET'

class Server:
    def __init__(self, num_workers=1, host='127.0.0.1', port=8087):
        self.num_workers = num_workers
        self.host = host
        self.port = port

        self.jobs = Queue()

        original_sigint_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)

        self.pool = multiprocessing.Pool(self.num_workers)

        signal.signal(signal.SIGINT, original_sigint_handler)

    def start(self):
        print(f'Server started with {self.num_workers} workers.')

        listener = threading.Thread(target=self.listen)
        listener.start()

        try:
            while True:
                job = self.jobs.get()

                # Will block when worker pool is empty
                self.pool.apply_async(job.run)
        except KeyboardInterrupt:
            print('\nSIGINT, terminating pool.')
            self.pool.terminate()
        else:
            print('Exiting normally')
            self.pool.close()

        self.pool.join()

        self.terminate_listener()
        listener.join()

        print('Server stopping.')

    def listen(self):
        print('Listening...')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()

            while True:
                conn, addr = s.accept()
                with conn:
                    message = conn.recv(1024).decode()

                    if message == KILL_SOCKET:
                        break

                    self.add_job(message)

        print('Done listening.')

    def terminate_listener(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(KILL_SOCKET.encode())


    def add_job(self, job):
        split = job.rstrip().split(",")

        if len(split) > 1:
            job, save_file = split
        else:
            job, save_file = split[0], None

        self.jobs.put(Job(job, save_file))

        print(f'Added job "{job}" with save "{save_file}".')


if __name__ == '__main__':
    s = Server(int(sys.argv[1]))
    s.start()
