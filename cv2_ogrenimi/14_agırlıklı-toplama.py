import cv2
import numpy as np


canvas = np.zeros((512,512,3), np.uint8 ) + 255
cv2.circle(canvas, (256,256), 60 , (255,0,0), -1)




canvas1 = np.zeros((512,512,3), np.uint8 ) + 255
cv2.rectangle(canvas1, (150,150), (350,350), (0,0,255), thickness=-1 )


add = cv2.add(canvas,canvas1)


dst = cv2.addWeighted(canvas1, 0.3, canvas, 0.7, 65 )

                    #Bu formülde kullanılan parametreler şunlardır:

                    # canvas1: İlk görüntü.

                    # 0.3: İlk görüntünün ağırlık katsayısı. Bu değer, ilk görüntüye ne kadar ağırlık verileceğini belirler.

                    # canvas: İkinci görüntü.

                    # 0.7: İkinci görüntünün ağırlık katsayısı. Bu değer, ikinci görüntüye ne kadar ağırlık verileceğini belirler.

                    # 0: Eklenen sabit değer. Bu değer, iki görüntüyü toplarken kullanılan sabit bir öteleme değeridir.

                    # cv2.addWeighted() fonksiyonu, iki görüntüyü ağırlıklı olarak birleştirir ve sonucu dst adlı yeni bir görüntü olarak döndürür.

                    # Örneğin, eğer canvas1 görüntüsüne %30 ağırlık verilirse ve canvas görüntüsüne %70 ağırlık verilirse, bu iki görüntü birleştirilir ve elde edilen görüntü dst olur. Bu işlem, görüntüler arasında ağırlıklı bir geçiş oluşturarak renklerin karışımını sağlar.

cv2.imshow("dst", dst)
# cv2.imshow("add", add)
cv2.imshow("canvas1", canvas1)
cv2.imshow("canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()