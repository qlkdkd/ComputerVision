import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 4개의 채널을 가진 영상
# IMREAD_UNCHANGED로 모든 채널 읽어오기
img = cv.imread(
    './JohnHancocksSignature.png',
    cv.IMREAD_UNCHANGED)

# 구조 요소
se = np.uint8([
    [0, 0, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0]
])


# 오츄 이진화
t, bin_img = cv.threshold(
    img[:, :, 3], 0, 255,
    cv.THRESH_BINARY + cv.THRESH_OTSU)

plt.imshow(bin_img, cmap='gray')
plt.xticks([]); plt.yticks([])
plt.savefig('./transformed/c3/otsu_bin.png')
plt.show()


# 모폴로지 확인용으로 영상 자르기
b = bin_img[
    bin_img.shape[0]//2:bin_img.shape[0],
    0:bin_img.shape[0]//2+1
]
plt.imshow(b, cmap='gray')
plt.xticks([]); plt.yticks([])
plt.savefig('./transformed/c3/cutted.png')
plt.show()


# 팽창
b_dilation = cv.dilate(b, se, iterations=1)
plt.imshow(b_dilation, cmap='gray')
plt.xticks([]); plt.yticks([])
plt.savefig('./transformed/c3/delation.png')
plt.show()


# 침식
b_erosion = cv.erode(b, se, iterations=1)
plt.imshow(b_dilation,  cmap='gray')
plt.xticks([]); plt.yticks([])
plt.savefig('./transformed/c3/erosion.png')
plt.show()


# 닫힘
b_closing = cv.erode(cv.dilate(b, se, iterations=1), se, iterations=1)
plt.imshow(b_dilation, cmap='gray')
plt.xticks([]); plt.yticks([])
plt.savefig('./transformed/c3/closed.png')
plt.show()
