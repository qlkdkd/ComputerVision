import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('./soccer.jpg')

# R 채널에서 히스토그램 구하기
h = cv.calcHist([img], [2], None, [256], [0, 256])
plt.plot(h, color='r', linewidth=1)
plt.show()
