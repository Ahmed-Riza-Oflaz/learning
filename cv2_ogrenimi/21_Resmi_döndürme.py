import cv2
import numpy as np

img = cv2.imread("../g1.jpeg",0)

row,col = img.shape

M = cv2.getRotationMatrix2D((col/3,row/3),25,1)

dst = cv2.warpAffine(img,M,(col,row))

cv2.imshow("dst",dst)

cv2.waitKey(0)

cv2.destroyAllWindows()