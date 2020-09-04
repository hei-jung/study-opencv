import cv2
import numpy as np
img = cv2.imread('cat2.jpg')

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
yellow = (0, 255, 255)
white = (255, 255, 255)
black = (0, 0, 0)

img = cv2.line(img, (5, 10), (5, 100), red, 3)
img = cv2.rectangle(img, (10, 10), (50, 50), green, 3)
img = cv2.circle(img, (200, 200), 100, blue, 3)
img = cv2.ellipse(img, (30, 40), (50, 20), 0, 0, 180, yellow, 3)
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1, 1, 2))
img = cv2.polylines(img, [pts], True, white)
img = cv2.putText(img, "cat", (10, 400), cv2.FONT_HERSHEY_SIMPLEX, 4, black, 3)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyWindow('img')
