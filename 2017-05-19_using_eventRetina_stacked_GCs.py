#! /usr/bin/env python3
# -*- coding: utf8 -*-
from __future__ import division, print_function
"""
openRetina : a photoreceptor layer
See https://github.com/laurentperrinet/openRetina
"""
__author__ = "(c) Pierre Albiges, Victor Boutin & Laurent Perrinet INT - CNRS"

from eventRetina import eventRetina
phrs = eventRetina(model=dict(layer='GCs', # label for this layer
                             input=['stream'], # input: can be the camera, noise, a movie (TODO)
                             in_port=5555,
                             output=['stream'], # output: can be stream, display, ...
                             name_capture = 'retina_capture',
                             out_port=5556
                             ))
print
phrs.run()