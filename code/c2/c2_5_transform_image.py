import cv2
import sys
import os # 폴더 만들려고 임포트

img = cv2.imread('soccer.jpg')
if img is None: sys.exit('Can\'t find a file.')

# 회색조 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_small = cv2.resize(
    gray, dsize=(0, 0), fx=0.5, fy=0.5) # 반으로 축소

# 영상을 파일에 저장
if not os.path.exists('transformed/c2'):
    os.makedirs('transformed/c2')

cv2.imwrite('./transformed/c2/soccer_gray.jpg', gray)
cv2.imwrite('./transformed/c2/soccer_gray_small.jpg', gray_small)

# 이미지 출력
cv2.imshow('Color image', img)
cv2.imshow('Gray image', gray)
cv2.imshow('Gray image small', gray_small)

cv2.waitKey()
cv2.destroyAllWindows()