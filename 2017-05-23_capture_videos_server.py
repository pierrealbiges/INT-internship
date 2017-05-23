""" Computer side """

import zmq

try: 
    context = zmq.Context()                   #Creating a zmq context containing all the above
    print('Connecting to Pi...')
    dealer = context.socket(zmq.DEALER)       #Opening a socket using the zmq DEALER protocol (see zmq doc)
    dealer.connect('tcp://10.164.7.213:5555') #Connecting to the RaspBerry Pi IP adress:port
    print('Connected')
    
    print('Sending request...')
    dealer.send(b'fetch')                     #Sending the request 'if possible, send the video file'
    
    total = 0                                 #Number of bytes received
    chunks = 0                                #Number of video chunks received
    
    video = open("video_picam", "r+b")        #Opening (creating if first use) a file under "read+write in bytes' protocol
    
    while True:                               #While received chunks arn't empty, continue receiving
        chunk = dealer.recv()                 #Receiving a video chunk
        chunks += 1
        size = len(chunk)                     #Checking the chunk length (in bytes) 
        total += size
        
        print('Chunk %i received, %i bytes' % (chunks, size))
        video.write(chunk)                    #Add the last received chunk to the local file 
    
        if size == 0:               #If last received chunk is empty (whole file received), stop listening the to socket
            break
            
    print('%i chunks received, %i bytes' % (chunks, total))

finally:                                      #Close the file/connections 
    video.close()
    dealer.close()
    context.term()
    print('\nConnection closed')