import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def main():
    img = cv.imread("img_00.png")
    '''
    cv.namedWindow('Windows', cv.WINDOW_AUTOSIZE)
    cv.imshow('Windows', img)
    cv.waitKey(0)
    cv.destroyWindow('Windows')
    '''
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.plot([50, 100], [200, 100], 'c', linewidth=5)
    plt.show()

if __name__ == '__main__':
    main()
