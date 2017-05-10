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
        message = socket.recv() #Wait for next request from client
        print("Received request: %s" % message)

        
        if message == 'END':
            break

        stream = io.BytesIO()
        camera.start_preview()
        time.sleep(1)
        
        camera.capture(stream)
        print(stream.getvalue())

        socket.send(stream.read())
        #socket.send(struct.pack('<L', stream.tell()))

except:
    socket.close()
    context.term()
    print('Socket and context closed')
