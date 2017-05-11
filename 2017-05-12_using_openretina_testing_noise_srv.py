"""
openRetina : a basic thalamic layer
See https://github.com/laurentperrinet/openRetina
"""
__author__ = "(c) Victor Boutin & Laurent Perrinet INT - CNRS"

import subprocess
p = subprocess.Popen(['./2017-05-12_using_openretina_testing_noise.py'])

from openRetina import openRetina
noise = openRetina(model=dict(layer='noise', # label for this layer
                                 input=['stream'], # input: can be the camera, noise, a movie (TODO)
                                 output=['display'], # output: can be stream, display, capture,...
                                 T_SIM=20))
noise.run()