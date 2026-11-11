import cv2 as cv
import numpy as np
import sys

cap = cv.VideoCapture(0, cv.CAP_DSHOW)
if not cap.isOpened(): sys.exit('failure to connect camera')

frames = []

# 이미지 수집
while True:
    # 비디오 읽기
    ret, frame = cap.read()
    if not ret:
        print('Exit loop because of failure to get frames')
        break

    cv.imshow('Video desplay', frame)

    # 이미지 수집 과정
    key = cv.waitKey(1) # 1ms동안 키보드입력 기다리기
    # c 입력하면 프레임 추가
    if key==ord('c'):
        frames.append(frame)
    # q 입력하면 루프 나감
    elif key==ord('q'):
        break

cap.release()
cv.destroyAllWindows()

# 읽어들인 이미지 합치기
if len(frames) > 0:
    imgs = frames[0]
    
    # 프레임 3개까지 합치기
    for i in range(1, min(3, len(frames))):
        imgs = np.hstack((imgs, frames[i]))

    cv.imshow('collected images', imgs)
    cv.imwrite('./transformed/c2/frames.jpg', imgs)
    cv.waitKey()
    cv.destroyAllWindows()