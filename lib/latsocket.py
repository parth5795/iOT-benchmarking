

import socket
class LTUSocket:


    def __init__(self, bufsize = 1024000, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
        self.BUFSIZE = bufsize
    def bind(self, port):
        self.sock.bind(('', port))
    def connect(self, host, port):
        self.connection = self.sock.connect((host, port))
        return self.connection

    def send(self):
        totalsent = 0
        msg = 'h'* (self.BUFSIZE)
        while totalsent < self.BUFSIZE:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def receive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < self.BUFSIZE:
            chunk = self.sock.recv(min(self.BUFSIZE - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)
