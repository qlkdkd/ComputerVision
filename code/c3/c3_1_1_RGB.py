import cv2 as cv

img = cv.imread('./soccer.jpg')
root = './transformed/c3'

# 원본
cv.imshow(f'Original(size: {img.shape})', img)
cv.imwrite('./transformed/c3/Original.jpg', img)


# 왼쪽 상단 부분
img_ULH = img[0:img.shape[0]//2, 0:img.shape[1]//2, :]
cv.imshow('Upper left half', img_ULH)
cv.imwrite('./transformed/c3/Upper_left_half.jpg', img_ULH)


# 중앙
img_CH =  img[img.shape[0]//4:3 * img.shape[0]//4,
               img.shape[1]//4:3 * img.shape[1]//4]
cv.imshow('Central half', img_CH)
cv.imwrite('./transformed/c3/Central_Half.jpg', img_CH)


# R 채널
img_R = img[:, :, 2]
cv.imshow('R channel', img_R)
cv.imwrite(f'{root}/img_R.jpg', img_R)


# G 채널
img_G = img[:, :, 1]
cv.imshow('G channel', img_G)
cv.imwrite(f'{root}/img_G.jpg', img_G)

# B 채널
img_B = img[:, :, 0]
cv.imshow('B channel', img_B)
cv.imwrite(f'{root}/img_B.jpg', img_G)

cv.waitKey()
cv.destroyAllWindows()