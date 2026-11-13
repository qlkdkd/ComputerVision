import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('./mistyroad.jpg')

# 이미지 명암으로 변경
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
plt.imshow(gray, cmap='gray')
plt.xticks([]); plt.yticks([]); plt.savefig('./transformed/c3/gray_img.jpg')
plt.show()


# 히스토그램 구해서 출력
h = cv.calcHist(
    [gray], [0], None, [256], [0, 256]
)
plt.plot(h, color='r', linewidth=1)
plt.savefig('./transformed/c3/hist_graph.jpg')
plt.show()


# 평활화 적용한 이미지
equal = cv.equalizeHist(gray)
plt.imshow(equal, cmap='gray')
plt.xticks([]); plt.yticks([])
plt.savefig('./transformed/c3/flattened_hist.jpg')
plt.show()


# 평활화 적용한 이미지의 히스토그램
h = cv.calcHist(
    [equal], [0], None, [256], [0, 256]
)
plt.plot(h, color='r', linewidth=1)
plt.savefig('./transformed/c3/flattened_hist_graph.jpg')
plt.show()
