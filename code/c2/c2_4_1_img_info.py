import cv2
import sys

img = cv2.imread('./soccer.jpg')

print(type(img))
print(img.shape)

print(img[0, 0, 0], img[0, 0, 1], img[0, 0, 2])