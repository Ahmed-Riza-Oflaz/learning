import cv2
import numpy as np


font1 = cv2.FONT_HERSHEY_SIMPLEX
font2 = cv2.FONT_HERSHEY_COMPLEX

img = cv2.imread("./polygons.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray,240,255,cv2.THRESH_BINARY)

contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    epsilon = 0.01*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)

    cv2.drawContours(img,[approx],0,(0),5)

    x = approx.ravel()[0]

    y = approx.ravel()[1]

    if len(approx) == 3:
        cv2.putText(img,"Triangle",(x,y),font1,1,(0))

    elif len(approx) == 4:
        cv2.putText(img,"rectangle",(x,y),font1,1,(0))

    elif len(approx) == 5:
        cv2.putText(img,"Pentagon",(x,y),font1,1,(0))

    elif len(approx) == 6:
        cv2.putText(img,"Hexagon",(x,y),font2,1,(0))

    else:
        cv2.putText(img,"Ellipse",(x,y),font2,1,(0))

cv2.imshow("IMG",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

""" 
Bu kodlar, bir görüntüdeki çokgenleri ve elipsleri tespit ederek bu şekilleri işaretler ve şekillerin türlerini yazıyla belirtir. İşlemleri adım adım açıklayalım:

import cv2 ve import numpy as np: OpenCV ve NumPy kütüphaneleri kod içinde kullanılabilir hale getirilir.

font1 = cv2.FONT_HERSHEY_SIMPLEX ve font2 = cv2.FONT_HERSHEY_COMPLEX: Kullanılacak yazı fontları belirlenir.

img = cv2.imread("./polygons.png"): Belirtilen dosya yolundaki görüntü dosyası okunur.

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY): Renkli görüntü gri tonlamalı görüntüye dönüştürülür.

_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY): Gri tonlamalı görüntü üzerinde bir eşikleme işlemi uygulanır. Bu işlem, görüntüyü siyah-beyaz bir formata dönüştürür.

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE): Eşiklenmiş görüntü üzerindeki konturlar (çizgiler) tespit edilir. Bu konturlar, görüntüdeki çokgenleri ve elipsleri temsil eder.

for cnt in contours: ...: Her kontur için döngü başlatılır. Her kontur, bir çokgen veya elipsi temsil eder.

epsilon = 0.01*cv2.arcLength(cnt, True): Her kontur için bir epsilon değeri hesaplanır. Bu değer, konturun köşelerini belirlemede kullanılır.

approx = cv2.approxPolyDP(cnt, epsilon, True): Konturun köşeleri yaklaşık olarak hesaplanır. Bu işlem, çokgenin köşelerini ve kenar sayısını belirler.

cv2.drawContours(img, [approx], 0, (0), 5): Çokgenin veya elipsin konturunu çizer. Çizilen şekillerin rengi siyah ve kalınlığı 5 piksel olarak belirlenir.

Şeklin türüne göre yazı eklenir. cv2.putText fonksiyonu ile şeklin türü, köşelerine yakın bir konuma yazılır.

cv2.imshow("IMG", img): İşlenmiş görüntüyü görselleştirir.

cv2.waitKey(0): Bir tuşa basılmasını bekler. Herhangi bir tuşa basıldığında program devam eder.

cv2.destroyAllWindows(): Tüm açık pencereleri kapatır.

Bu kodlar, çokgenleri ve elipsleri tespit ederek bu şekilleri işaretler ve her şeklin türünü yazıyla belirtir. Özellikle şekil türlerini algılama ve işaretlemeye yönelik bir görüntü işleme uygulamasıdır.

"""