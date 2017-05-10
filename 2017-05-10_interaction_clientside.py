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


while True:
	message = socket.recv() #Wait for next request from client
	print("Received request: %s" % message)

	if message == 'END':
		break

	stream = io.BytesIO()
	camera.start_preview()
	start = time.time()

	for capture in camera.capture_continuous (stream, format='jpeg'):
		print('dbkey n1', len(capture.getvalue()))

		if time.time() - start > 5:
			break

	socket.send(capture)
	#socket.send(struct.pack('<L', stream.tell()))

	time.sleep(1)


socket.close()
context.term()
print('Socket and context closed')
