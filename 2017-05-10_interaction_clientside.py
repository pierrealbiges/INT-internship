import time
import zmq
import picamera
import struct
import io

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
print('Client connected')

try:
	while True:
		message = socket.recv() #Wait for next request from client
		print("Received request: %s" % message)

		if message == 'END':
			break

		camera = picamera.PiCamera()
		camera.resolution = (640, 480)
		camera.start_preview()
		time.sleep(2)

		start = time.time()
		stream = io.BytesIO()
		for capture in camera.capture_continuous(stream, 'jpeg'):

			socket.send(stream.read())
			#socket.send(struct.pack('<L', stream.tell()))

			if time.time() - start > 5:
				socket.close()
				break

finally:
	socket.close()
	context.term()
	print('Socket and context closed')
