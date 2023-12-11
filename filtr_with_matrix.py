import cv2
import numpy as np
import matplotlib.pyplot as plt

from skimage import io

image_height = 400
image_width = 600
dpi = 100

url = f"https://placekitten.com/{image_width}/{image_height}"
img = io.imread(url)

filter = np.array([[1.5, 0, 0],
                    [0, 1.5, 0],
                    [0, 0, 1.5]])
filter_new = np.array([[-2, 3, -2],
                       [3, 1, 3],
                       [-2, 3, -2]])
saturation = cv2.filter2D(img, -1, filter)
new = cv2.filter2D(img, -1, filter_new)

plt.subplot(141), plt.imshow(img), plt.title('Original')
plt.subplot(142), plt.imshow(saturation), plt.title('Filtered')
plt.subplot(143), plt.imshow(new), plt.title('Filtered2')
plt.show()
