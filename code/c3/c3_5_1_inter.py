import cv2 as cv
from make_folder import root

img = cv.imread('./rose.png')
print(img.shape)
patch = img[250:350, 170:270, :] # 100x100 패치 자르기
print(patch.shape)

# 패치에 최근접이웃 진행
# 파란색 사각형
img = cv.rectangle(img, (170, 250), (270, 350), (255, 0, 0), 3)
# 최근접 이웃 보간
patch1 = cv.resize(
    patch, dsize=(0, 0), fx=5, fy=5, interpolation=cv.INTER_NEAREST
)
# 선형 보간
patch2 = cv.resize(
    patch, dsize=(0, 0), fx=5, fy=5, interpolation=cv.INTER_LINEAR
)
# 양3차 보간
patch3 = cv.resize(
    patch, dsize=(0, 0), fx=5, fy=5, interpolation=cv.INTER_CUBIC
)


cv.imshow('Origianl', img)
cv.imwrite(root + '/3_5_1_Original.png', img)

cv.imshow('Resize nearest', patch1)
cv.imwrite(root + '/3_5_1_nearest.png', patch1)

cv.imshow('Resize bilinear', patch2)
cv.imwrite(root+'/3_5_1_bilinear.png', patch2)

cv.imshow('Resize bicubic', patch3)
cv.imwrite(root+'/3_5_1_cubic.png', patch3)

cv.waitKey()
cv.destroyAllWindows()