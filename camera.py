#!/usr/bin/python
from __future__ import division, print_function

'''
File name : 2017-05-02_grabing_frames_with_opencv.ipynb
Authors : Pierre Albiges, Victor Boutin and Laurent Perrinet
Date created : 2017-04-25
Date last modified : 2017-05-04
Object : Apprehend the OpenRetina project through the manipulation of the PhotoReceptor class

See https://github.com/laurentperrinet/openRetina/blob/master/src/openRetina.py as source for the program
See https://github.com/pierrealbiges/INT-internship/ for associated documents
'''

import numpy as np
import cv2
from distutils.version import LooseVersion

np.set_printoptions(precision=2, suppress=True)

class PhotoReceptor :
    
    def __init__(self, w, h, cam_id=0, DOWNSCALE=1, verbose=True) :

        self.h, self.w = h, w
        self.rpi = False
        self.cap = cv2.VideoCapture(cam_id)
        
        if verbose: print ("Before a downscale of {}, dim1 : {}, dim2 : {}".format(DOWNSCALE, self.h, self.w))

        if LooseVersion(cv2.__version__).version[0] == 2:
            self.cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, self.w)
            self.cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, self.h) 

            self.DOWNSCALE = DOWNSCALE
            if DOWNSCALE > 1 :
                W = self.cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
                H = self.cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT) #Why not working direcy on w, h?
                self.cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, int(W/self.DOWNSCALE))
                self.cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, int(H/self.DOWNSCALE))
            self.h, self.w = self.cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT), self.cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
            if verbose: print ('Using OpenCV')
        
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
            if verbose: print('Using OpenCV3')

        if verbose: print ("After a downscale of {}, dim1 : {}, dim2 : {}".format(self.DOWNSCALE, self.h, self.w))


    def grab(self) :
        ret, frame_bgr = self.cap.read()
        #frame = frame_bgr[:, :, ::-1] #BGR to RBG.
        frame = frame_bgr
        return frame
    
    def close(self) :
        self.cap.release()
        del self.cap