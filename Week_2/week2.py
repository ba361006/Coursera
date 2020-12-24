import numpy as np
import cv2 

image = cv2.imread("./image/lena.png")
row, col, channel = image.shape
print("image.shape: ", image.shape)
# cv2.imshow("image", image)

blocks = []
for idx in range(row):
    blocks.append(image[idx:idx+8])


# cv2.waitKey()