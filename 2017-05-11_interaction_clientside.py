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

camera = picamera.PiCamera()
camera.resolution = (640, 480)

try:
    while True:
        message = socket.recv()
        print("Received request: n.%s" % message)

        if message == 'END':
            break

        stream = io.BytesIO()
        camera.start_preview()
        time.sleep(0.2)
        
        camera.capture(stream, format='jpeg')

        socket.send(stream.getvalue())

except:
    socket.close()
    context.term()
    print('Connection closed')
