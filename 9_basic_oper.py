import cv2
from matplotlib import pyplot as plt
img = cv2.imread('cat2.jpg')
b, g, r = cv2.split(img)
img = cv2.merge([r, g, b])
roi = img[300:400, 100:200]
plt.subplot(121), plt.imshow(img), plt.title('img')
plt.subplot(122), plt.imshow(roi), plt.title('roi')
plt.show()
