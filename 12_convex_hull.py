import cv2
from matplotlib import pyplot as plt

img = cv2.imread('contours.png')
img1 = img.copy()

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)

contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Convex Hull이란 contours point를 모두 포함하는 볼록한 외관선
# Contour Approximation과 유사한 결과지만, 방법은 전혀 다름
# 손모양에서 외곽선까지의 거리 중에서 countours와 hull과의 최대거리 ---> convexity defect
# print(len(contours)) # 4
cnt1 = contours[1]
cnt2 = contours[2]
cnt3 = contours[3]  # 0: 테두리, 1: 바위, 2: 보, 3: 가위
hull1 = cv2.convexHull(cnt1)
hull2 = cv2.convexHull(cnt2)
hull3 = cv2.convexHull(cnt3)

# checking convexity
# contour가 convex인지 판단 (오목한 부분이 없으면 True)
cv2.isContourConvex(contours[0])

cv2.drawContours(img1, [hull1], 0, (0, 0, 255), 3)
cv2.drawContours(img1, [hull2], 0, (0, 255, 0), 3)
cv2.drawContours(img1, [hull3], 0, (255, 0, 0), 3)

titles = ['Original', 'Convex Hull']
images = [img, img1]

for i in range(2):
    plt.subplot(1, 2, i + 1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()
