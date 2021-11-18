import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image, ImageFilter


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



def open_img(img_name):
    # Abrindo a Imagem
    img_original = Image.open(img_name)
    return img_original

def edge_detection(img_name):
    img_original = img_name

    # Converter a imagem para tons de cinza
    img_original = img_original.convert('L')

    # Kernel de matriz (3X3)
    m = (3,3)
    # kernel de 3x3
    mk = [
          -1, -1, -1,
          -1,  8, -1, # Filtro laplaciano
          -1, -1, -1
          ]
    # mk = [
    #       -1,  0, 1,
    #       -2,  0, 2,
    #       -1, -0, 1
    #       ]
    # mk = [
    #       1,  2, 1,
    #       0,  0, 2,
    #       -1, -2, -1
    #       ]

    # Scala
    scale = 1
    # offset
    offset = 0
    
    # Criação do Kernel
    kernel = ImageFilter.Kernel(m, mk, scale, offset)

    # Aplicação do kernel/mascara
    img_filtrada = img_original.filter(kernel)

    img_filtrada.show()
    img_original.show()

    return img_filtrada

def blur_filter(img_name):
    # img_original  = Image.open(img_name)
    img_original = img_name

    img_filtrada = img_original.filter(ImageFilter.GaussianBlur(2))
    img_filtrada.show()

    return img_filtrada

if __name__ == '__main__':

    img = 'assets\input\\'+'rua.jpg'
    # padronizar_imagem(img)
    # filtro_de_gabro(img)

    op_img = open_img(img)
    edge = edge_detection(op_img)
    # blur = blur_filter(edge)
    # edge = edge_detection(blur)
    
    cv.waitKey(0)
    cv.destroyAllWindows()