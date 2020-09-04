import cv2
img = cv2.imread('cat2.jpg')
img = cv2.resize(img, (600, 400))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('cat2_gray.jpg', gray)
cv2.imshow('gray', gray)
cv2.waitKey(0)
cv2.destroyWindow('gray')
