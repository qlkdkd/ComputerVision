import cv2 as cv
import numpy as np

img = cv.imread('soccer.jpg')
img = cv.resize(img, dsize=(0, 5), fx=0.25, fy=0.25) # 1/4 크기로

def gamma(f, gamma=1.0):
    f1 = f / 255.0
    return np.uint8(255 * (f1**gamma))

gc = np.hstack((
    img,
    gamma(img, 0.5),
    gamma(img, 0.75),
    gamma(img, 1.0),
    gamma(img, 2.0),
    gamma(img, 3.0)
))

cv.imshow('gamma', gc)
cv.imwrite('./transformed/c3/gammas.jpg', gc)
cv.waitKey()
cv.destroyAllWindows()