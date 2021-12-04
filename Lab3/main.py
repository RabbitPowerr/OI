import glob

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import skimage.exposure as exposure


def DFFTnp(img):
    f = np .fft.fft2(img)
    fshift = np.fft.fftshift(f)
    return fshift


def reverseDFFTnp(dfft):
    f_ishift = np.fft.ifftshift(dfft)
    reverse_image = np.fft.ifft2(f_ishift)
    return reverse_image


def showDFFT(img, fft, name):
    magnitude = np.abs(fft)
    plt.subplot(121)
    plt.imshow(img, 'Greys', vmin=0, vmax=255)
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    #plt.subplot(122), plt.imshow(np.log(np.abs(magnitude)), 'Greys')
    #plt.title('Centred Spectrum'), plt.xticks([]), plt.yticks([])
    #plt.show()


folder_path = r"F:\\OI\\OI\\Lab3\\pictures\\"
images = glob.glob(folder_path + '00_88.png')

for name in images:
    img = np.float32(cv.imread(name, 0))
    fshift = DFFTnp(img)
    showDFFT(img, fshift, name)
    ksize = 7
    kernel = np.zeros(img.shape)
    blur = cv.getGaussianKernel(ksize, -1)
    blur = np.matmul(blur, np.transpose(blur))
    
    mask = cv.GaussianBlur(img, (13, 13), 0)
    fshift_masked = np.multiply(fshift, mask) / 255
    back_ishift_masked = np.fft.ifftshift(fshift_masked)
    img_filtered = np.fft.ifft2(back_ishift_masked, axes=(0,1))
    img_filtered = np.abs(img_filtered).clip(0,255).astype(np.uint8)


    sobelx = cv.Sobel(mask,cv.CV_64F,1,0,ksize=3)
    sobely = cv.Sobel(mask,cv.CV_64F,0,1,ksize=3)

    sobelx_norm = exposure.rescale_intensity(sobelx, in_range='image', out_range=(0,255)).clip(0,255).astype(np.uint8)
    sobely_norm = exposure.rescale_intensity(sobelx, in_range='image', out_range=(0,255)).clip(0,255).astype(np.uint8)

    sobelx2 = cv.multiply(sobelx,sobelx)
    sobely2 = cv.multiply(sobely,sobely)

    sobel_magnitude = cv.sqrt(sobelx2 + sobely2)
    sobel_magnitude = exposure.rescale_intensity(sobel_magnitude, in_range='image', out_range=(0,255)).clip(0,255).astype(np.uint8)
    fshift_masked_2 = np.multiply(fshift, sobel_magnitude) / 255
    back_ishift_masked_2 = np.fft.ifftshift(fshift_masked_2)
    img_filtered_2 = np.fft.ifft2(back_ishift_masked_2, axes=(0,1))
    img_filtered_2 = np.abs(img_filtered_2).clip(0,255).astype(np.uint8)
    
    plt.subplot(122), plt.imshow(abs(img_filtered), 'Greys')
    outimg = np.abs(img_filtered_2)
    plt.subplot(122), plt.imshow(outimg, 'Greys')
    plt.title('Out'), plt.xticks([]), plt.yticks([])
    cv.imwrite("out.png", outimg)

    plt.show()
