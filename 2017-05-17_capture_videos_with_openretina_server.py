""" Server side """

import zmq
import struct
import io

context = zmq.Context()
print('Connecting to Pi...')
socket = context.socket(zmq.REQ)
socket.connect('tcp://10.164.7.213:5555')
print('Connected')

print('Sending request')
socket.send(b'Camera request')

message = socket.recv()
print('Received reply [ %s ]' % (len(message)))

socket.close()
context.term()
print('Connection closed')