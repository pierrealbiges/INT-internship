#! /usr/bin/env python3
# -*- coding: utf8 -*-

import picamera

class video:
    
    def __init__(self):
        self.picam = picamera.PiCamera
        self.picam.resolution = (640,480) #Defining the camera resolution
        self.picam.start_recording(output='video_picam', format='h264', inline_headers=False) #Start recording in 'filename.filetype'
        self.picam.wait_recording(10) #Better integrated time.wait() that allow to continually check for errors
        self.picam.stop_recording() #Stop recording

        print('It went fine!') #Control line
        
capture = video()