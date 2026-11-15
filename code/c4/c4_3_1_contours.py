import cv2 as cv
import numpy as np
from make_folder import root

img = cv.imread('soccer.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
x, y = gray.shape[:2]
x //= 2; y //= 2
gray = cv.resize(gray, (y, x))  # 이미지 크기 조정
img = cv.resize(img, (y, x))

canny = cv.Canny(gray, 100, 200)


# 직선 검출
contour, hierarchy = cv.findContours(
    canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE
)


# 경계선으로 판정된 값을 리스트에 담기
lcounter = []
for i in range(len(contour)):
    if len(contour[i]) > 100:
        lcounter.append(contour[i])


# 경계선 그리기
cv.drawContours(img, lcounter, -1, (0, 255, 0), 3)

imgs = [img, canny]; titles = ['Original_with_contours.jpg','Canny.jpg']
for t, i in zip(titles, imgs):
    cv.imshow(t, i)
    cv.imwrite(root+'c4_3_1'+t, i)

cv.waitKey()
cv.destroyAllWindows()