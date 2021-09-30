
#!/usr/bin/python3

import sys, time
from socket import *
import threading

BUFSIZE = 1024000
testdata = 'h' * (BUFSIZE-1)


def listen():
    st_socket.listen(1)
    while 1:
        conn, (host, remoteport) = st_socket.accept()
        while 1:
            data = conn.recv(BUFSIZE)
            if not data:
                break
            del data
        conn.send(bytearray(testdata,"utf-8"))

        conn.close()
        print ('Tested upload with', host)


st_socket = socket(AF_INET, SOCK_STREAM)
st_socket.bind(('', 8879))
print ('Server ready...')


listen()
