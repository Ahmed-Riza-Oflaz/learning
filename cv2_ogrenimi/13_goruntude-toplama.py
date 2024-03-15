import cv2
import numpy as np

####Bu kod, üç farklı görüntü oluşturur ve bu görüntüleri birleştirerek yeni bir görüntü oluşturur.

canvas = np.zeros((512,512,3), np.uint8 ) + 255

cv2.circle(canvas, (256,256), 60 , (255,0,0), -1)




canvas1 = np.zeros((512,512,3), np.uint8 ) + 255

cv2.rectangle(canvas1, (150,150), (350,350), (0,0,255), thickness=-1 )

                    #cv2.rectangle() fonksiyonu, canvas1 üzerinde (150, 150) ve (350, 350) koordinatları arasında kalan alanı kırmızı bir dikdörtgenle doldurur.


add = cv2.add(canvas,canvas1)

                    #add: canvas ve canvas1 görüntülerini toplar, yani piksel değerlerini toplayarak iki görüntüyü birleştirir.


cv2.imshow("add", add)

cv2.imshow("canvas1", canvas1)

cv2.imshow("canvas", canvas)

cv2.waitKey(0)

cv2.destroyAllWindows()