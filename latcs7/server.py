
#!/usr/bin/python3

import sys, time
from socket import *
import threading

BUFSIZE = 1024000
def server():
    st_socket = socket(AF_INET, SOCK_STREAM)
    st_socket.bind(('', 8875))
    st_socket.listen(1)
    print ('Server ready...')
    while 1:
        conn, (host, remoteport) = st_socket.accept()
        while 1:
            data = conn.recv(BUFSIZE)
            if not data:
                break
            del data
        conn.close()
        print ('Tested upload with', host)
server()
