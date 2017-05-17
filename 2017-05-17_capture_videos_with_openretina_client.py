""" Pi side """

import zmq

try:
    context = zmq.Context()
    router = context.socket(zmq.ROUTER)
    
    router.sndhwm = socket.rcvhwm = 250000
    router.hwm = 250000
    router.bind("tcp://*:5555")
    print("Connected to computer")
    
    file = open("video_picam","r")
    print('File opened')
    while True:
        identity, command = router.recv_multipart()
        
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
    router.close()
    context.term()
    print("Connection closed")