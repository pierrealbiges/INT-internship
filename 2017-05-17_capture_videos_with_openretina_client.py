""" Pi side """

import zmq

context = zmq.Context()
router = context.socket(zmq.ROUTER)
socket_set_hwm(router, 0)
router.bind("tcp://*:5555")
print("Connected to computer")

try:
    file = open("video_picam","r")
    print('File opened')
    while True:
        identity, command = router.recv_multipart()
        
        except zmq.ZMQError as e:
            if e.errno == zmq.ETERM:
                return
            else:
                raise
        
        assert command == b"fetch"
        print('Command received')
        
        while True:
            data = file.read(CHUNCK_SIZE)
            router.send_multipart([identity, data])
            print('Sending data...')
            if not data:
                print('\nNo more data')
                break

finally:
    socket.close()
    context.term()
    print("Connection closed")