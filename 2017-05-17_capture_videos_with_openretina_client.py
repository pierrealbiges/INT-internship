""" Pi side """

import zmq

context = zmq.Context()
router = context.socket(zmq.ROUTER)
socket_set_hwm(router, 0)
router.bind("tcp://*:5555")
print("Connected to computer")

try:
    file = open("video_picam","r")
    while True:
        identity, command = router.recv_multipart()
        assert command == b"fetch"
        
        while True:
            data = file.read(CHUNCK_SIZE)
            router.send_multipart([identity, data])
            if not data:
                break

finally:
    socket.close()
    context.term()
    print("Connection closed")