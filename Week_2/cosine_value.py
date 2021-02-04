# import numpy as np 

# N = 8
# for i in range(8):
#     print(f"\ni = {i}")
#     for x in range(8):
#         print(f"x = {x}, cosine: {np.cos(((2*x+1)*i*np.pi)/(2*N))}")


import numpy as np 
import cv2 


# # 0:32
# # 64:96
# # 128:160
# # 192:224
block = np.zeros([256,256], dtype=np.uint8)
for i in range(4):
    block[:,64*i:32+64*i] = 255
cv2.imshow("block",block)
cv2.waitKey()