import cv2
import sys
import os

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    sys.exit('failure to connect camera')

print(cap)
while True:
    ret, frame = cap.read() # 비디오를 구성하는 프레임 획득

    if not ret:
        print('Exit loop because of failure to get frames')
        break

    cv2.imshow('Videw display', frame)
    cv2.imwrite('./transformed/c2/frame.jpg', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release() # 카메라와 연결 끊기
cv2.destroyAllWindows()