import cv2
import numpy as np   
import matplotlib.pyplot as plt

#################---PXELS---###############################

path = "../g1.jpeg"

img = cv2.imread(path)


px = img[10,10] #x ve y eksenindeki 10 a 10 değerlerinin renk karşılıkları
print(px)



cv2.imshow("fotograf",img)


cv2.waitKey(0)

cv2.destroyAllWindows()


""" 
BGR/RGB

B: 0 - 255
G: 0 - 255
R: 0 - 255

0 = black
255 = white

"""



#############################----accessing pixel's-----value###### pixel degiş

print("RED Value:(BEFORE)", img.item(10,10,2) )


img.itemset((10,10,2), 100)

print("RED VALUE (AFTER) :", img.item(10,10,2) )

#############################################3

corner = img[0:550,0:350] #ilk değer "y" eksenini ikinci değer "x" eksenini tarar

### !!  corner = img[  y-start : y-end , x-start : x-end ]  !!######



cv2.imshow("corner",corner)


cv2.waitKey(0)

cv2.destroyAllWindows()
 
