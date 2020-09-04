import cv2
img = cv2.imread('cat2.jpg')
img = cv2.resize(img, (300, 200))
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyWindow('img')
