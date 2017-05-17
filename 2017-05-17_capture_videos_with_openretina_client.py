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
    print('Received request : %s', % message)
    
    vid = open('video_picam','rb')
    socket.send(vid)

finally:
    socket.close()
    context.term()
    print('Connection closed')