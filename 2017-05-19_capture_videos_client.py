""" Pi side """

import zmq
CHUNK_SIZE = 250000

try:
    context = zmq.Context()
    router = context.socket(zmq.ROUTER)
    
    router.sndhwm = router.rcvhwm = CHUNK_SIZE
    router.hwm = CHUNK_SIZE
    router.bind("tcp://*:5555")
    print("Connected to computer")
    
    file = open("video_picam2","rb")
    print('File opened')
    while True:
        identity, command = router.recv_multipart()
        
        assert command == b"fetch"
        print('Command received')
        
        while True:
            data = file.read(CHUNK_SIZE)
            router.send_multipart([identity, data])
            print('Sending data...')
            if not data:
                print('\nNo more data')
                break
        if not data: break

finally:
    router.close()
    context.term()
    print("\nConnection closed")