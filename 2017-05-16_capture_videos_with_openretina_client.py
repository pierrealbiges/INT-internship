""" Client side """

import zmq
import struct
import io

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
print('Server connected')

try:
    message = socket.recv()
    print('Received request : %s' message)
    
    Vid = open('video_picam','r')
    socket.send(Vid)

finally:
    socket.close()
    context.term()
    print('Connection closed')