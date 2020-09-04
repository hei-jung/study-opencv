import cv2
from matplotlib import pyplot as plt

img = cv2.imread('cat2.jpg')
plt.imshow(img)
plt.xticks([])
plt.yticks([])
plt.show()
