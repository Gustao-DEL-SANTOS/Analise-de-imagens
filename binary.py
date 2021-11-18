import numpy as np
import cv2 as cv

path = r'assets/input/digital1.jpg'
path = r'assets/input/yunna.jpg'

img = cv.imread(path, -1)

print(img.shape[0])
print(img.shape[1])
print(img.shape[2])
print(img.shape[0])
for i in range(399):
    for j in range(img.shape[1]-1):
            print(img.shape[i][j][0])
            




cv.imshow('digital', img)
cv.waitKey(0)
cv.destroyAllWindows()

