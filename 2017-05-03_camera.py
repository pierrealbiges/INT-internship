#!/usr/bin/python
from __future__ import division, print_function

'''
File name : camera.py
Authors : Pierre Albiges, Victor Boutin and Laurent Perrinet
Date created : 2017-04-25
Date last modified : 2017-05-05
Object : Apprehend the OpenRetina project through the manipulation of the PhotoReceptor class

See https://github.com/laurentperrinet/openRetina/blob/master/src/openRetina.py as source for the program
See https://github.com/pierrealbiges/INT-internship/ for associated documents

Warning : Raspbian parts are not working for now
'''

import numpy as np
import cv2
import time

import io #Allows to work with streams on python
import socket
import struct #Allows the convertion between binary data (here from connection network) and python strings 

from PIL import Image

from distutils.version import LooseVersion

np.set_printoptions(precision=2, suppress=True)

class PhotoReceptor :

    def __init__(self, w, h, cam_id=0, DOWNSCALE=1, verbose=True, rpi=False) :

        self.h, self.w = h, w
        self.rpi = rpi
        self.verbose = verbose

        try:
            if self.rpi:
                if self.verbose: print(''' Raspbian system ''')
                self.server_socket = socket.socket()       #Create a new socket
                self.server_socket.bind(('0.0.0.0', 8000)) #Bind the socket to the adress
                self.server_socket.listen(0)               #Listen the connection made to the socket
                time.sleep(1)
                self.connection = self.server_socket.accept()[0].makefile('rb') #Accept the connection. Socket must be binded and listened
            else:
                if self.verbose: print(''' Unix systems ''')
                self.cap = cv2.VideoCapture(cam_id)

                if self.verbose: print ("Before a downscale of {}, dim1 : {}, dim2 : {}".format(DOWNSCALE, self.h, self.w))

                if LooseVersion(cv2.__version__).version[0] == 2:
                    self.cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, self.w)
                    self.cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, self.h) 

                    self.DOWNSCALE = DOWNSCALE
                    if DOWNSCALE > 1 :
                        W = self.cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
                        H = self.cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
                        self.cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, int(W/self.DOWNSCALE))
                        self.cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, int(H/self.DOWNSCALE))
                    self.h, self.w = self.cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT), self.cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
                    if self.verbose: print ('Using OpenCV')

                else:

                    self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.w)
                    self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.h)

                    self.DOWNSCALE = DOWNSCALE
                    if DOWNSCALE > 1:
                        W = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
                        H = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
                        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(W/self.DOWNSCALE))
                        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(H/self.DOWNSCALE))
                    self.h, self.w = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT), self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
                    if self.verbose: print('Using OpenCV3')

                if self.verbose: print ("After a downscale of {}, dim1 : {}, dim2 : {}".format(self.DOWNSCALE, self.h, self.w))

        except:
            print('Unable to capture video')


    def grab(self):
        try:
            #if self.verbose: print(''' Raspbian system ''')
            while True :
                self.image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0] #Unpack the string
                if not self.image_len: #If the string is empty (length = 0) or is missing, break the connection
                    print('Image length missing or zero')
                    break

                self.image_stream = io.BytesIO()
                self.image_stream.write(connection.read(image_len))
                self.image_stream.seek(0)
            self.image = Image.open(self.image_stream)
            # self.image = self.image.rotate(270)
            # self.image.show()
            print('Image is %d%d pixels' % self.image.size)
            frame = self.image
            self.image.verify()
            print('Image is verified \n')
        except:
            #if self.verbose: print(''' Unix systems''')
            ret, frame_bgr = self.cap.read()
            #frame = frame_bgr[:, :, ::-1] #BGR to RBG.
            frame = frame_bgr
        return frame

    def close(self):
        try:
            if self.verbose: print(''' Raspbian system ''')
            self.connection.close()    #Close the connection
            self.server_socket.close() # Close the socket
            print('Connection closed')
        except:
            if self.verbose: print(''' Unix systems''')
            self.cap.release()
            del self.cap