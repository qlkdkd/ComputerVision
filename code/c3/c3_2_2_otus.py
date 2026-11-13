import cv2 as cv
import sys

img = cv.imread('./soccer.jpg')

# img의 R 채널을 이진화 수행
t, bin_img = cv.threshold(
    img[:, :, 2], 0, 255,
    cv.THRESH_BINARY + cv.THRESH_OTSU)
print(f'Best threshold that finded by Otsu algorithm: {t}')

cv.imshow('R channel', img[:,:, 2])
cv.imshow('R channel binarization', bin_img)

cv.imwrite('./transformed/c3/R_chn.jpg', img[:, :, 2])
cv.imwrite('./transformed/c3/R_chn_bin.jpg', bin_img)

cv.waitKey()
cv.destroyAllWindows()