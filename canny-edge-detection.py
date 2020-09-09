# Do all the relevant imports
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

# Read in the image and convert to grayscale
# Note: in the previous example we were reading a .jpg 
# Here we read a .png and convert to 0,255 bytescale
image = mpimg.imread('exit-ramp.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

# Define a kernel size for Gaussian smoothing / blurring
kernel_size = 3 # Must be an odd number (3, 5, 7...)
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)

# Define our parameters for Canny and run it
low_threshold = 80
high_threshold = 200 # high_threshold ist der wichtigere Schwellwert der beiden.
                     # Je höher dieser ist, um so weniger Edges werden angezeigt.
                     # Logik: Erst ab einem Gradienten von 200 (von Pixel zum benachbarten Pixel) wird der Pixel als Edge angezeigt.
                     # low_threshold: Er bestimmt im Wesentlichen nur noch die Spanne zwischen low und high_threshold. Je größer 
                     # diese Spanne ist, umso mehr direkt benachbarte Pixel werden zusätzlich als Edges angezeigt.
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

# Display the image
plt.imshow(edges, cmap='Greys_r')
