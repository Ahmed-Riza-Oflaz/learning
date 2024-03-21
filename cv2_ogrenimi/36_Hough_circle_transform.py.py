import cv2
import numpy as np


img1 = cv2.imread("./coins.jpg")
img2 = cv2.imread("./balls.jpg")

gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

img1_blur = cv2.medianBlur(gray1,5)
img2_blur = cv2.medianBlur(gray2,5)

circles1 = cv2.HoughCircles(img1_blur,cv2.HOUGH_GRADIENT,1,img1.shape[0]/4,param1=200,param2=10,minRadius=35,maxRadius=90) 

circles2 = cv2.HoughCircles(img2_blur,cv2.HOUGH_GRADIENT,1,img2.shape[0]/8,param1=200,param2=10,minRadius=5,maxRadius=100) 

if circles1 is not None:
    circles1 = np.uint16(np.around(circles1))
    for i in circles1[0,:]:
        cv2.circle(img1,( i[0], i[1]), i[2] , (0,255,0),2 )

if circles2 is not None:
    circles2 = np.uint16(np.around(circles2))
    for i in circles2[0,:]:
        cv2.circle(img2,( i[0], i[1]), i[2] , (0,255,0),2 )



cv2.imshow("img1 original",img1)
cv2.imshow("img2 original ",img2)

cv2.imshow("img1 circles",circles1)
cv2.imshow("img2 circles",circles2)



cv2.waitKey(0)
cv2.destroyAllWindows()

""" 
Bu kodlar, dairelerin (halkaların) tespit edilmesi ve görüntüler üzerinde işaretlenmesi için kullanılır. İşlemleri adım adım açıklayalım:

import cv2 ve import numpy as np: OpenCV ve NumPy kütüphaneleri kod içinde kullanılabilir hale getirilir.

img1 = cv2.imread("./coins.jpg") ve img2 = cv2.imread("./balls.jpg"): İki farklı görüntü dosyası okunur.

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) ve gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY): Renkli görüntüler gri tonlamalı görüntülere dönüştürülür.

img1_blur = cv2.medianBlur(gray1, 5) ve img2_blur = cv2.medianBlur(gray2, 5): Gri tonlamalı görüntüler üzerinde median blur (medyan bulanıklaştırma) işlemi uygulanır. Bu işlem, görüntülerdeki gürültüyü azaltır ve daha düzgün bir görüntü elde etmeye yardımcı olur.

circles1 = cv2.HoughCircles(img1_blur, cv2.HOUGH_GRADIENT, 1, img1.shape[0]/4, param1=200, param2=10, minRadius=35, maxRadius=90): Hough dönüşümü kullanılarak img1_blur görüntüsündeki daireler tespit edilir. param1, param2, minRadius ve maxRadius parametreleri ile dairesel nesnelerin tespiti ve çapları hakkında bilgi verilir.

circles2 = cv2.HoughCircles(img2_blur, cv2.HOUGH_GRADIENT, 1, img2.shape[0]/8, param1=200, param2=10, minRadius=5, maxRadius=100): Aynı işlem ikinci görüntü olan img2_blur üzerinde de uygulanır.

if circles1 is not None: ve if circles2 is not None:: Eğer daireler tespit edilmişse (None değilse), bu daireler çizilir.

cv2.circle(img1, (i[0], i[1]), i[2], (0, 255, 0), 2) ve cv2.circle(img2, (i[0], i[1]), i[2], (0, 255, 0), 2): Tespit edilen daireler, orijinal görüntüler üzerinde yeşil renkte çizilir.

cv2.imshow("img1 original", img1) ve cv2.imshow("img2 original", img2): Orijinal görüntüler ile işaretlenmiş dairelerin olduğu görüntüler görselleştirilir.

cv2.imshow("img1 circles", circles1) ve cv2.imshow("img2 circles", circles2): Sadece dairelerin olduğu görüntüler görselleştirilir.

cv2.waitKey(0): Bir tuşa basılmasını bekler. Herhangi bir tuşa basıldığında program devam eder.

cv2.destroyAllWindows(): Tüm açık pencereleri kapatır.

Bu kodlar, Hough dönüşümü kullanarak görüntülerdeki daireleri tespit eder ve bu daireleri yeşil renkte işaretler. Sonuç olarak, orijinal görüntüler ile işaretlenmiş dairelerin olduğu görüntüler görüntülenir. Bu tür bir işlem, nesne tespiti ve özelliklerini belirleme gibi görüntü işleme uygulamalarında yaygın olarak kullanılır.


"""