#! /usr/bin/env python3
# -*- coding: utf8 -*-

import picamera

class Rec_video():
    def __init__(self):
        cam = picamera.PiCamera()
        cam.resolution = (640,480) #Defining the camera resolution
        
        print('Recording start') #Control line
        
        cam.start_recording(output='video_picam2', format='h264') #Start recording in 'filename.filetype'
        cam.wait_recording(5) #Better integrated time.wait() that allow to continually check for errors
        cam.stop_recording() #Stop recording

        print('\nRecording end') #Control line
        
rec = Rec_video() #Calling the Rec_video class