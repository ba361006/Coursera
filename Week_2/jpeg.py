"""
Function Name: jpeg.py
*
Description: In this programme, we are going to create out own jpeg compression.
             For better understanding, we will do it with OOP, which may not be the
             most efficient way to implement this method.
*
Edited by: [date] [author name]
"""
import cv2 
import numpy as np 

class jpeg():
    def __init__(self, image_in):
        self.__image_in = image_in
        assert len(self.__image_in.shape) > 2, "shape of image_in should be greater than 2"
        self.__rows = self.__image_in.shape[0]
        self.__cols = self.__image_in.shape[1]
        self.__channels = self.__image_in.shape[2]

        self.__divide()
        self.__dct()

    def __divide(self):
        """
        Function Name: __divide
        *
        Description: This will append the image divided into multiple 8x8 blocks to self.__blocks
        *
        Parameters: None 
        *
        Return: None
        *
        Edited by: [date] [author name]
        """        
        copy_image = self.__image_in.copy()
        row_block = int(self.__rows/8)
        col_block = int(self.__cols/8)
        self.__blocks = []
        # print(f"row_block: {row_block}, col_block: {col_block}")
        for row in range(row_block):
            for col in range(col_block):
                self.__blocks.append(copy_image[row*8:(row+1)*8, col*8:(col+1)*8, :])

        
    def __dct(self):
        self.__dct = []
        for block in self.__blocks:
            self.__dct.append(cv2.dct(block))

        



if __name__ == "__main__":
    image_in = cv2.imread("./image/lena.png")
    jpeg(image_in)
    # cv2.imshow("image_in", image_in)
    # cv2.waitKey()

