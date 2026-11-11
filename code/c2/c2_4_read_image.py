import cv2
import sys

img = cv2.imread('./soccer.jpg')

if img is None:
    sys.exit('Can\'t find a file.')

cv2.imshow('Image Display', img)

cv2.waitKey()
cv2.destroyAllWindows()