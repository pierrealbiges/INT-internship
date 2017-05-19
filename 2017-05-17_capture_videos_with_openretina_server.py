""" Computer side """

import zmq

try: 
    context = zmq.Context()
    print('Connecting to Pi...')
    dealer = context.socket(zmq.DEALER)
    dealer.connect('tcp://10.164.7.213:5555')
    print('Connected')
    
    CHUNK_SIZE = 250000
    print('Sending request')
    dealer.send(b'fetch')
    
    total = 0
    chunks = 0
    
    while True:
        chunk = dealer.recv()
        chunks += 1
        size = len(chunk)
        total += size
        
        print('Chunk %i received, %i bytes' % (chunks, size))
        video = open("video_picam", "wb+")
    
        if size == 0:
            break #Whole file received
            
    print('%i chunks received, %i bytes' % (chunks, total))

finally: 
    video.close()
    dealer.close()
    context.term()
    print('\nConnection closed')