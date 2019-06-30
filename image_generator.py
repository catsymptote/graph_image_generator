import math
import numpy as np


x_min = -2
x_max = 2
y_min = -2
y_max = 2

x_pix = 100
y_pix = 100


def get_x(x_in):
    x_range = x_max - x_min
    x_out = x_in / x_pix * x_range + x_min
    return x_out

def get_y(y_in):
    y_range = y_max - y_min
    y_out = y_in / y_pix * y_range + y_min
    return y_out


def gen_plane(func, w, h):
    global x_pix
    x_pix = w
    global y_pix
    y_pix = h
    
    channels = 3
    
    plane = np.zeros((h, w, channels), dtype=np.uint8)
    #plane = [] #[[(100, 100, 100)]*x_pix]*y_pix
    
    for y in range(w):
        #row = ()
        for x in range(h):
            #r = func(get_x(x), get_y(y)) #math.sqrt(get_x(x)**2 + get_y(y)**2)
            #if r > 1.5:
            #    plane[y][x][0] = 255
            #    plane[y][x][1] = 255
            #    plane[y][x][2] = 255
            #else:
            #    plane[y][x][0] = 100
            #    plane[y][x][1] = 100
            #    plane[y][x][2] = 100
            
            rgb = func(get_x(x), get_y(y))
            plane[y][x] = rgb
            
            
        #plane.append(row)
    
    return plane
