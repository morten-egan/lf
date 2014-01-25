import cv2
import numpy as np
from matplotlib import pyplot as plt

def inverte(imagem, name):
    imagem = (255-imagem)
    cv2.imwrite(name, imagem)

image = cv2.imread('images/IMG_2024.JPG')

gs_imagem = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverte(gs_imagem, "images/inverted.png")