import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('cat2.jpg')

mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255

masked_img = cv2.bitwise_and(img, img, mask=mask)

hist_full = cv2.calcHist([img], [1], None, [256], [0, 256])

hist_mask = cv2.calcHist([img], [1], mask, [256], [0, 256])

plt.subplot(221), plt.imshow(img, 'gray'), plt.title('Original Image')
plt.subplot(222), plt.imshow(mask, 'gray'), plt.title('Mask')
plt.subplot(223), plt.imshow(masked_img, 'gray'), plt.title('Masked Image')

plt.subplot(224), plt.title('Histogram')
plt.plot(hist_full, color='r'), plt.plot(hist_mask, color='b')

plt.show()
