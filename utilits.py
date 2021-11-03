import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np



data_in = 'assets\input'
data_in = 'assets\output'

def padronizar_imagem(img_name):
    
    
    try:
        # faz a leitura da imagem
        img = cv.imread(img_name, 1)
        # pega o numero de pixels horizonta e vertical
        h, w = img.shape[:2]

        res = cv.resize(img, (int(w / 2), int(h / 2)), interpolation= cv.INTER_CUBIC )
        cv.imshow('diminuida', res)
    except IOError:
        print('Erro na leitura do arquivo!')

    
def filtro_de_gabro(img_name):
    try:
        kernel = cv.getGaborKernel((5, 5), 1.0, np.pi/4, 5, 0, 1, ktype=cv.CV_32F)

        img = cv.imread(img_name)
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        filtered_img = cv.filter2D(img, cv.CV_8UC3, kernel)

        cv.imshow('image', img)
        cv.imshow('filtered image', filtered_img)

        h, w = kernel.shape[:2]
        kernel = cv.resize(kernel, (3*w, 3*h), interpolation=cv.INTER_CUBIC)
        cv.imshow('gabor kernel (Resize)', kernel)
    except IOError:
        print('Arquivo nao encontrado!')




if __name__ == '__main__':

    img = 'assets\input\loli.jpg'
    # padronizar_imagem(img)
    filtro_de_gabro(img)

    
    cv.waitKey(0)
    cv.destroyAllWindows()