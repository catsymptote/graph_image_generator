#import png
from PIL import Image
import scipy.misc
import numpy as np
import os


class Grapher:
    axes = False
    frame = False
    
    # Image
    f_name = "img.png"
    w = 1
    h = 1
    img = None
    
    # Plane
    x_min = -2
    x_max = 2
    y_min = -2
    y_max = 2


    def __init__(self, img, w, h):
        self.img = img
        self.w = w
        self.h = h
    

    def set_plane(self, x0, x1, y0, y1):
        self.x_min = x0
        self.x_max = x1
        self.y_min = y0
        self.y_max = y1


    def set_axes(self, a):
        if a:
            self.axes = True
        else:
            self.axes = False
    
    def set_frame(self, a):
        if a:
            self.frame = True
        else:
            self.frame = False


    def gen_frame(self):
        frame_color = [0,0,0]
        
        for i in range(self.h):
            self.img[0][i] = frame_color
            self.img[self.w -1][i] = frame_color
        
        for i in range(self.w):
            self.img[i][0] = frame_color
            self.img[i][self.h -1] = frame_color


    def gen_axes(self):
        frame_color = [0,0,0]
        
        # 2*... = wat.
        x_zero = 2*int(self.w / (self.x_max - self.x_min))
        y_zero = 2*int(self.h / (self.y_max - self.y_min))
        
        for i in range(self.h):
            self.img[x_zero][i] = frame_color
        
        for i in range(self.w):
            self.img[i][y_zero] = frame_color

    #def create(self):
    #    return
    #    with open('img.png', 'wb') as f:
    #        wrt = png.Writer(self.w, self.h)
    #        wrt.write(f, self.img)
    
    
    #def create(self):
    #    png_img = Image.new('RGB', (self.w, self.h), (0, 0, 0))
    #    #self.img = png_img.load()
    #    png_img.save(self.img)
        
    def create(self):
        i = 0
        f_name = "img/" + str(i)
        
        while os.path.isfile(f_name + ".png"):
            i += 1
            f_name = "img/" + str(i)
        
        f_name = f_name + ".png"
        
        scipy.misc.imsave(f_name, self.img)
        
        #os.startfile(f_name)
        image = Image.open(f_name)
        image.show()