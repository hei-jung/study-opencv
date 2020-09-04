import cv2
from matplotlib import pyplot as plt

img = cv2.imread('rectangle.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(contours)
print(contours[0][0][0][0])
print(contours[0][1][0])

image1 = img.copy()
cv2.circle(image1, (contours[0][0][0][0], contours[0][0][0][1]), 20, (255,0,0), -1)
cv2.circle(image1, (contours[0][1][0][0], contours[0][1][0][1]), 20, (255,0,0), -1)
cv2.circle(image1, (contours[0][2][0][0], contours[0][2][0][1]), 20, (255,0,0), -1)
cv2.circle(image1, (contours[0][3][0][0], contours[0][3][0][1]), 20, (255,0,0), -1)
image2 = cv2.drawContours(img, contours, -1, (0,0,255), 20)

plt.subplot(121), plt.imshow(image1), plt.title('contour points')
plt.subplot(122), plt.imshow(image2), plt.title('drawContours')
plt.show()
