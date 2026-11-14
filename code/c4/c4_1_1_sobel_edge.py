import cv2 as cv
from make_folder import root

img = cv.imread('soccer.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
x, y = gray.shape[:2]
x //= 2; y //= 2
gray = cv.resize(gray, (y, x))  # 이미지 크기 조정


# 소벨 연산자 적용
grad_x = cv.Sobel(gray, cv.CV_32F, 1, 0, ksize=3)
grad_y = cv.Sobel(gray, cv.CV_32F, 0, 1, ksize=3)


# 절대값을 취해 양수 영상으로 변환
sobel_x = cv.convertScaleAbs(grad_x)
sobel_y = cv.convertScaleAbs(grad_y)


# 에지 강도 계싼
edge_strength = cv.addWeighted(
    sobel_x, 0.5, sobel_y, 0.5, 0
)

cv.imshow('Original', gray)
cv.imshow('sobelx', sobel_x)
cv.imshow('sobely', sobel_y)
cv.imshow('edge_strength', edge_strength)

cv.imwrite(root + '/4_1_1_Original.jpg', gray)
cv.imwrite(root + '/4_1_1_sobelx.jpg', sobel_x)
cv.imwrite(root + '/4_1_1_sobely.jpg', sobel_y)
cv.imwrite(root + '/4_1_1_edge_strength.jpg', edge_strength)

cv.waitKey(0)
cv.destroyAllWindows()