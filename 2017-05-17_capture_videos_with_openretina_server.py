""" Computer side """

import zmq

try: 
    context = zmq.Context()
    print('Connecting to Pi...')
    dealer = context.socket(zmq.DEALER)
    dealer.connect('tcp://10.164.7.213:5555')
    print('Connected')
    
    CHUNCK_SIZE = 250000
    print('Sending request')
    dealer.send(b'fetch')
    
    total = 0
    chuncks = 0
    
    while True:
        chunck = dealer.recv()
        chuncks += 1
        size = len(chunck)
        total += size
    
        if size == 0:
            break #Whole file received
            
    print('%i chuncks received, %i bytes' % (chuncks, total))

finally: 
    dealer.close()
    context.term()
    print('\nConnection closed')