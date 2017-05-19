"""
openRetina : a basic thalamic layer
See https://github.com/laurentperrinet/openRetina
"""
__author__ = "(c) Victor Boutin & Laurent Perrinet INT - CNRS"

import subprocess
p = subprocess.Popen(['./2017-05-19_using_eventRetina_testing_local_camera.py'])

from eventRetina import eventRetina
camera = eventRetina(model=dict(layer='camera', # label for this layer
                                 input=['stream'], # input: can be the camera, noise, a movie (TODO)
                                 output=['display'], # output: can be stream, display, capture,...
                                 T_SIM=5))
camera.run()