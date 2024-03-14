import cv2
import numpy as np   
import matplotlib.pyplot as plt


path ="../g1.jpeg"

img = cv2.imread(path) 

print(img.shape) # width , height , channel değerlerini belirtir

#channnel görüntünün renkli olup olmadığını gösterir
# channnel değeri == 3 renkli , değer = 1 grayscale

cv2.imshow("foto", img)

cv2.waitKey(0)

cv2.destroyAllWindows()

