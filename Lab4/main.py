import glob
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import shape
from numpy.lib.function_base import angle

# Steps that we should to have the best result
# 1.Normalize image
# 2.Apply Gabor filter
# 3.Normalize and convert to int8( adaptiveThreshold work only with int8  )
# 4.Binarize 
# 5.Apply median blur

def normalize_image(img):
    norm_image = cv.normalize(
        img, None, alpha=0, beta=1, norm_type=cv.NORM_MINMAX, dtype=cv.CV_32F)
    return norm_image


def normalize8(I):
  mn = I.min()
  mx = I.max()

  mx -= mn

  I = ((I - mn)/mx) * 255
  return I.astype(np.uint8)

def Gabor_filtering(img, ker_size, si, t, l, angle):
    kernel = cv.getGaborKernel((ker_size,ker_size),si,t,l,angle)
    out =  cv.filter2D(img,-1,kernel)
    return out

def apply_gabor_filter(img):
    angles = [0,20,40,60,80,90]
    out = []
    for a in angles:
        res = Gabor_filtering(img, 15, 7, 11, 3, a)
        out.append(res)
    return out,angles

def pre_processing(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = normalize_image(img)
    return img    

def post_poccessing(img):
    result =  img

    result = normalize8(img)
    result = cv.adaptiveThreshold(result,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
    result = cv.medianBlur(result,5)
    return result

path = 'F:\OI\OI\Lab4\dataset\\'
name = '3'
path = path + name+'.png'

img =  cv.imread(path)
img = pre_processing(img)
result ,angles = apply_gabor_filter(img)
i = 0 
for x in result:
    x = post_poccessing(x)
    filename = '.\\result\\'+name+'result_angle'+str(angles[i])+'.png'
   
    cv.imwrite(filename,x)
    i+=1    
    
