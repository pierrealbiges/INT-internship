#! /usr/bin/env python3
# -*- coding: utf8 -*-

import picamera

picam = picamera.PiCamera
picam.resolution = (640,480) #Defining the camera resolution
picam.start_recording(self,output='video_picam', format='h264') #Start recording in 'filename.filetype'
picam.wait_recording(10) #Better integrated time.wait() that allow to continually check for errors
picam.stop_recording() #Stop recording

print('It went fine!') #Control line