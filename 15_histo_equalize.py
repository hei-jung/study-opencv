import cv2
import numpy as np
from matplotlib import pyplot as plt

# numpy 사용
img = cv2.imread('foggy.jpg')
print('img=', end='')
print(img)

hist, bins = np.histogram(img.flatten(), 256, [0, 256])

cdf = hist.cumsum()

cdf_m = np.ma.masked_equal(cdf, 0)

cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max() - cdf_m.min())

cdf = np.ma.filled(cdf_m, 0).astype('uint8')
print('cdf=', end='')
print(cdf)

img2 = cdf[img]
print('img2=', end='')
print(img2)
plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.subplot(122), plt.imshow(img2), plt.title('Equalization')
plt.show()

# openCV 내장함수 사용
'''img = cv2.imread('foggy.jpg', 0)
img2 = cv2.equalizeHist(img)
img = cv2.resize(img, (400, 300))
img2 = cv2.resize(img, (400, 300))

dst = np.hstack((img, img2))
cv2.imshow('img', dst)
cv2.waitKey()
cv2.destroyAllWindows()'''

# CLAHE(Contrast Limited Adaptive Histogram Equalization) 적용
'''img = cv2.imread('foggy.jpg', 0)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
img2 = clahe.apply(img)

img = cv2.resize(img, (400,300))
img2 = cv2.resize(img2, (400,300))

dst = np.hstack((img, img2))
cv2.imshow('img', dst)
cv2.waitKey()
cv2.destroyAllWindows()'''
