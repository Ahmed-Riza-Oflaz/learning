import cv2
import numpy as np


canvas = np.zeros((512,512,3), dtype=np.uint8 ) + 255

font1 = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(canvas, "OpenCV", (15,260), font1, 4, (0,0,0), cv2.LINE_AA )


gray = cv2.cvtColor(canvas,cv2.COLOR_BGR2GRAY)


gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray,100000,0.01,10)

corners = np.int0(corners)

for corner in corners:
    x,y = corner.ravel()

    cv2.circle(canvas,(x,y),3,(0,0,255),-1)


cv2.imshow("canvas", canvas )

cv2.waitKey(0)
cv2.destroyAllWindows()


""" 
512x512 piksel boyutlarında beyaz bir zemin oluşturulur.

Bu zemin üzerine "OpenCV" metni siyah renkte ve belirli bir font büyüklüğüyle eklenir.

Oluşturulan resim gri tonlamalı bir formata dönüştürülür.

Köşe noktalarını tespit etmek için "goodFeaturesToTrack" fonksiyonu kullanılır. 

Bu fonksiyon, Harris Corner Detection algoritmasını temel alır ve belirtilen eşik değerlerine göre köşe noktalarını bulur.

Tespit edilen köşe noktaları kırmızı dairelerle işaretlenir ve bu işaretlenmiş görüntü ekranda gösterilir.

Bu kod, köşe noktalarının tespit edilmesi ve görselleştirilmesi için kullanılır. Özellikle köşe noktalarının nesne tespiti veya izleme gibi uygulamalarda önemli olduğu durumlarda kullanılabilir.

"""