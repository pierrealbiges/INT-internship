"""
openRetina : a basic thalamic layer
See https://github.com/laurentperrinet/openRetina
"""
__author__ = "(c) Victor Boutin & Laurent Perrinet INT - CNRS"

import subprocess
p = subprocess.Popen(['./2017-05-19_using_eventRetina_stacked_camera.py'])
GCs = subprocess.Popen(['./2017-05-19_using_eventRetina_stacked_GCs.py'])

from eventRetina import eventRetina
camera = eventRetina(model=dict(layer='output', title='A three layered network: retina - GCs - display', # label for this layer
                                 input=['stream'], # input: can be the camera, noise, a movie (TODO)
                                 in_port=5556,
                                 output=['display', 'capture'], # output: can be stream, display, capture,...
                                 name_capture='eventRetina_capture.png',
                                 T_SIM=5, sparseness=0.01), verb=True)
camera.run()