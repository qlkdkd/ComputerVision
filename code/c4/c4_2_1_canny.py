import cv2 as cv
from make_folder import root


img = cv.imread('./soccer.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
x, y = gray.shape[:2]
x //= 2; y //= 2
gray = cv.resize(gray, (y, x))  # 이미지 크기 조정

canny1 = cv.Canny(gray, 50, 150) # T_low=50, T_high=150
canny2 = cv.Canny(gray, 100, 200) # T_low=100, T_high=200


imgs = [gray, canny1, canny2]
titles = ['gray', 'canny1', 'canny2']

for i,j in zip(imgs, titles):
    cv.imshow(j, i)
    cv.imwrite(root + '/c4_2_1' +j + '.jpg', i)

cv.waitKey()
cv.destroyAllWindows()