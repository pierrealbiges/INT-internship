import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv() #Wait for next request from client
    print("Received request: %s" % message)

    time.sleep(2)
    socket.send(b"World") #Send reply back to client
