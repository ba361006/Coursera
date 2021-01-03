"""
Function Name: jpeg.py
*
Description: In this programme, we are going to create out own jpeg compression.
             For simplicity and better understanding, we will do it with OOP, which may not be the
             most efficient way to implement this method.
*
Edited by: [date] [author name]
"""
import cv2 
import numpy as np 

class jpeg():
    def __init__(self, image_in):
        assert len(image_in.shape) > 2, "shape of image_in should be greater than 2"

        # setting constant
        self.__image_in = image_in
        self.__ROWS = self.__image_in.shape[0]
        self.__COLS = self.__image_in.shape[1]
        self.__CHANNELS = self.__image_in.shape[2]
        self.__JPEG_TABLE = np.array([[16,11,10,16,24,40,51,61],
                                      [12,12,14,19,26,58,60,55],
                                      [14,13,16,24,40,57,69,56],
                                      [14,17,22,29,51,87,80,62],
                                      [18,22,37,56,68,109,103,77],
                                      [24,35,55,64,81,104,113,92],
                                      [49,64,78,87,103,121,120,101],
                                      [72,92,95,98,112,100,103,99]],
                                      dtype=np.float32)

        self.__divide()
        self.__dct()
        self.__quantize()

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
        row_block = int(self.__ROWS/8)
        col_block = int(self.__COLS/8)
        self.__blocks = []
        # print(f"row_block: {row_block}, col_block: {col_block}")
        for row in range(row_block):
            for col in range(col_block):
                self.__blocks.append(copy_image[row*8:(row+1)*8, col*8:(col+1)*8, :])

        
    def __dct(self):
        self.__dct = []
        for block in self.__blocks:
            block = np.float32(block)
            self.__dct.append([cv2.dct(block[:,:,0]), cv2.dct(block[:,:,1]), cv2.dct(block[:,:,2])])
    
    def __quantize(self):
        self.__quantization = []
        result = cv2.divide(self.__dct[0][0], self.__JPEG_TABLE)
        # print("Result: ", result)
        # result = round(result)
        # print("Result: ", result)
        print(np.round(1.1))


        



if __name__ == "__main__":
    image_in = cv2.imread("./image/lena.png")
    # jpeg(image_in)
    cv2.imshow("image_in", image_in)
    cv2.waitKey()

