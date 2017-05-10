''' Pi side'''

import time
import zmq
import picamera
import struct
import io

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
print('Server connected')

try:
    message = socket.recv() #Wait for next request from client
    print("Received request: %s" % message)

    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.start_preview()
    time.sleep(2)

    stream = io.BytesIO()

    socket.send(stream.read())
    #socket.send(struct.pack('<L', stream.tell()))

finally:
    socket.close()
    context.term()
    print('Socket and context closed')
