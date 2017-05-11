"""
openRetina : a basic thalamic layer
See https://github.com/laurentperrinet/openRetina
"""
__author__ = "(c) Victor Boutin & Laurent Perrinet INT - CNRS"

from openRetina import openRetina
thalamus = openRetina(model=dict(layer='thalamus', # label for this layer
                                 ip='10.164.7.213',
                                 input=['stream'], # input: can be the camera, noise, a movie (TODO)
                                 output=['display'], # output: can be stream, display, capture,...
                                 T_SIM=20))
thalamus.run()