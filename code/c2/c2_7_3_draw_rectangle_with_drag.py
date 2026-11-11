import cv2 as cv
import sys

img = cv.imread('./girl_laughing.jpg')
if img is None: sys('Failure to fine files')


# 드래그 콜백함수
def draw(event, x, y, flags,param):
    global ix, iy
    # 마우스 왼쪽 버튼 클릭하면 초기 위치 저장
    if event == cv.EVENT_LBUTTONDOWN:
        ix, iy = x, y

    # 마우스 왼쪽버튼 놓으면 직사각형 그리기
    elif event == cv.EVENT_LBUTTONUP:
        cv.rectangle(img, (ix, iy), (x, y), (0, 0, 255), 2)

    cv.imshow('Drawing', img)


cv.namedWindow('Drawing')
cv.imshow('Drawing',img)

# Drawing 윈도우에 draw 콜백함수 지정
cv.setMouseCallback('Drawing',draw)

while True:
    if cv.waitKey(1) == ord('q'):
        cv.imwrite('./transformed/c2/dragged_img.jpg', img)
        cv.destroyAllWindows()
        break