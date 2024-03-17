import cv2
import numpy as np
from matplotlib import pyplot as plt

#Bu kod, bir görüntüyü üç farklı yöntemle eşikleme (thresholding) işlemine tabi tutar ve sonuçları gösterir. 

#Eşikleme işlemi, bir görüntüdeki piksellerin belirli bir eşiğe göre siyah veya beyaz olarak ayrılmasını sağlar, böylece görüntü üzerindeki nesneleri veya yapıları vurgular.

img = cv2.imread("../g1.jpeg",0)

ret, th1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY)

th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY ,11,2)

th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,51,2)

cv2.imshow("original img",img)
cv2.imshow("img-th1", th1)
cv2.imshow("img-th2",th2)
cv2.imshow("img-th3",th3)


cv2.waitKey(0)
cv2.destroyAllWindows()

""" 
cv2.threshold: Görüntüyü belirli bir eşiğe göre ikiye böler. Eşik değeri (50) kullanılarak pikseller 0 veya 255 olarak ayarlanır.

cv2.adaptiveThreshold (MEAN_C): Görüntü üzerinde lokal bir eşikleme işlemi uygular. Ortalama değer kullanılarak pikseller 0 veya 255 olarak ayarlanır. Komşu piksellerin ortalamasına göre bir eşik hesaplanır (11,2).

cv2.adaptiveThreshold (GAUSSIAN_C): Benzer şekilde, görüntü üzerinde lokal bir eşikleme işlemi uygular, ancak bu sefer Gauss filtresi kullanır. Bu yöntem daha yumuşak geçişler sağlayabilir (51,2).

Sonuç olarak, üç farklı eşikleme yöntemiyle işlenmiş görüntülerin ekrana gösterilmesini sağlar.

"""
