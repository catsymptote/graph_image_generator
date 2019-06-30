"""
TO DO
- Make into a single file?
    Make it easy to just put in a dir and use
    the graphing functions.
- Allow for different ways of generating?
    Pixel-based vs layer-based?
    Different functions. E.g. Mandelbrot vs Buddahbrot.
- Black/white vs other functionality? (In function file.)
- Info about generation time?
    Maybe store this in a csv, with depth, etc etc.
    As well as version number?


"""


import grapher
import image_generator

import math


def Z(a_z, b_z, a_c, b_c):
    Re = a_z**2 + a_c - b_z**2
    Im = b_c + 2*a_z*b_z
    return Re, Im


def rad(x, y):
    return math.sqrt(x**2 + y**2)


def func(x, y):
    # c
    a_c = x
    b_c = y
    
    # z
    a_z = a_c
    b_z = b_c
    
    start = 100
    inkr = 6
    
    for i in range(100): # Break off point
        if rad(a_z, b_z) > 2:
            rgb = [inkr*i, inkr*i, inkr*i+start]
            for j in range(len(rgb)):
                if rgb[j] > 255:
                    rgb[j] = 255
            return rgb
        a_z, b_z = Z(a_z, b_z, a_c, b_c)
    return [0, 0, 0]


w = 200
h = 200

rgb = image_generator.gen_plane(func, w, h)

pic = grapher.Grapher(rgb, w, h)
pic.gen_frame()
pic.gen_axes()
pic.create()
