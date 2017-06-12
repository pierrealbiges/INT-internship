"""
openRetina : a basic thalamic layer
See https://github.com/laurentperrinet/openRetina
"""
__author__ = "(c) Victor Boutin & Laurent Perrinet INT - CNRS"

#import subprocess
#p = subprocess.Popen(['ssh pi@10.164.7.213 "cd ~/INT-internship ; python3 2017-05-16_using_openretina.py "'])

from openRetina import openRetina
thalamus = openRetina(model=dict(layer='thalamus', title='A simple interaction with the pi retina', # label for this layer
                                 ip='10.164.7.213',
                                 input=['stream'], # input: can be the camera, noise, a movie (TODO)
                                 output=['display'], # output: can be stream, display, capture,...
                                 T_SIM=20))
thalamus.run()