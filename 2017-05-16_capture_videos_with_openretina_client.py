""" Client side """

import zmq
import struct
import io

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")
print('Server connected')

message = socket.recv()
print('Received request : %s', message)

Vid = open('video_picam','r')
socket.send(Vid)


socket.close()
context.term()
print('Connection closed')