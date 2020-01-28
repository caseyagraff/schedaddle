import sys
import socket

class Sender:
    def __init__(self, host='127.0.0.1', port=8087):
        self.host = host
        self.port = port

    def send(self, job):
        print(f'Sending "{job}".')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(job.encode())

def main(jobs_file):
    sender = Sender()
    with open(jobs_file, 'r') as f_in:
        for line in f_in:
            sender.send(line.rstrip())

if __name__ == '__main__':
    main(sys.argv[1])

