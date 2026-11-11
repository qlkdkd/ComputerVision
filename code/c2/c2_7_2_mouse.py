import cv2 as cv
import sys

img = cv.imread('./girl_laughing.jpg')
if img is None: sys('Failure to fine files')


# 이미지 클릭하면 사각형 그리는 콜백 함수
def draw(event, x, y, flags,param):

    # 마우스 좌클릭하면 200x200 크기의 빨간 정사각형
    if event == cv.EVENT_LBUTTONDOWN:
        cv.rectangle(
            img, (x, y), (x+200, y+200), (0, 0, 255), 2
        )

    # 우클릭하면 100x100 크기의 파란 정사각형
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.rectangle(
            img, (x, y), (x+100, y+100), (255, 0, 0), 2
        )

    cv.imshow('Drawing', img)


cv.namedWindow('Drawing')
cv.imshow('Drawing',img)

# Drawing 윈도우에 draw 콜백함수 지정
cv.setMouseCallback('Drawing',draw)

while True:
    if cv.waitKey(1) == ord('q'):
        cv.imwrite('./transformed/c2/clicked_img.jpg', img)
        cv.destroyAllWindows()
        break