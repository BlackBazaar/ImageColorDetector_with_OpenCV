import numpy as np
import cv2 as cv

img = cv.imread('assets/bluetheme.jpg', 1)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):

        blue = img[i, j, 0]
        green = img[i, j, 1]
        red = img[i, j, 2]

        if blue > 70 and not(blue == green or blue == red) and blue > green and blue > red:
            img[i, j] = [255, 255, 255]


cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()
