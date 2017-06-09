#! /usr/bin/env python3
# -*- coding: utf8 -*-
from __future__ import division, print_function
"""
openRetina : a photoreceptor layer
See https://github.com/laurentperrinet/openRetina
"""
__author__ = "(c) Pierre Albiges, Victor Boutin & Laurent Perrinet INT - CNRS"

from openRetina import openRetina
phrs = openRetina(model=dict(layer='phrs', # label for this layer
                             input=['camera'], # input: can be the camera, noise, a movie (TODO)
                             output=['stream', 'capture'], # output: can be stream, display, ...
                             name_capture='openRetina_capture.png',
                             out_port=5555
                             ), verb=True)
phrs.run()