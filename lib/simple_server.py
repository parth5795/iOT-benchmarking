
#!/usr/bin/python3

import sys, time
import threading
from latsocket import LTUSocket
BUFSIZE = 1024000


def listen():

        data = st_socket.receive()
        st_socket.send()
        print ('Tested upload with', host)


st_socket = LTUSocket()
st_socket.bind( 8879)
print ('Server ready...')


listen()
