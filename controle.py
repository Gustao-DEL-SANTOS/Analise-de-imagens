from PyQt5 import uic, QtWidgets
from PyQt5 import QtGui
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np



def analisar():
    dgtela.lbl1.setPixmap(QtGui.QPixmap('digital1.jpg'))
    dgtela.lbl2.setPixmap(QtGui.QPixmap('digital1.jpg'))
    dgtela.lbl3.setPixmap(QtGui.QPixmap('digital1.jpg'))
    dgtela.lbl4.setPixmap(QtGui.QPixmap('digital1.jpg'))


def binar(data):
    br = cv.imread(data, 1)
    # cv.imshow('img',br)


    gray = cv.cvtColor(br, cv.COLOR_BGR2GRAY)

    # res, thresh = cv.threshold(gray, 0, 255,
    #                             cv.THRESH_BINARY_INV +
    #                             cv.THRESH_OTSU)

    # cv.imwrite('dg1.jpg', thresh)
    # diminuir('digital1.jpg')
    
    # dgtela.lbl2.setPixmap(QtGui.QPixmap('dgResult.jpg'))

    # res, thresh = cv.threshold(gray, 0, 255,
    #                             cv.THRESH_BINARY_INV +
    #                             cv.THRESH_OTSU)

    # cv.imwrite('dg4.jpg', thresh)
    # dgtela.lbl3.setPixmap(QtGui.QPixmap('dg3.jpg'))

    # # cv.imshow('img2', thresh)
    # diminuir('dg4.jpg')
    # dgtela.lbl1.setPixmap(QtGui.QPixmap('dgResult2.jpg'))
    # dgtela.lbl4.setPixmap(QtGui.QPixmap('dgResult4.jpg'))
    



    res, thresh = cv.threshold(gray, 0, 255,
                                # cv.THRESH_BINARY_INV +
                                cv.THRESH_OTSU)

    cv.imshow('img3', thresh)


def erosao():
        # Reading the input image
    img = cv.imread('digital_real5.jpg', 0)
    
    # Taking a matrix of size 5 as the kernel
    kernel = np.ones((5,5), np.uint8)
    
    # The first parameter is the original image,
    # kernel is the matrix with which image is
    # convolved and third parameter is the number
    # of iterations, which will determine how much
    # you want to erode/dilate a given image.
    img_erosion = cv.erode(img, kernel, iterations=1)
    img_dilation = cv.dilate(img, kernel, iterations=1)
    cv.imshow('Input', img)
    cv.imshow('Erosion', img_erosion)
    cv.imshow('Dilation', img_dilation)

def diminuir(f_name):
    try:
        # Read image from disk.
        img = cv.imread(f_name)
    
        # Get number of pixel horizontally and vertically.
        (height, width) = img.shape[:2]
    
        # Specify the size of image along with interploation methods.
        # cv2.INTER_AREA is used for shrinking, whereas cv2.INTER_CUBIC
        # is used for zooming.
        res = cv.resize(img, (int(width / 2), int(height / 2)), interpolation = cv.INTER_CUBIC)
    
        # Write image back to disk.
        cv.imwrite('dgResult4.jpg', res)
    
    except IOError:
        print ('Error while reading files !!!')










app = QtWidgets.QApplication([])
dgtela = uic.loadUi('digitais.ui')

# analisar()
# diminuir('digital1.jpg')
binar('assets\input\digital_real5.jpg')

# erosao()

# dgtela.show()
app.exec()
cv.waitKey(0)
cv.destroyAllWindows()