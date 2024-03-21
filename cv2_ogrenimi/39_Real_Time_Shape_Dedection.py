import cv2
import numpy as np

font1 = cv2.FONT_HERSHEY_SIMPLEX
font2 = cv2.FONT_HERSHEY_COMPLEX

cap = cv2.VideoCapture(0)

while True:

    ret , frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray,240,255,cv2.THRESH_BINARY)

    contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        epsilon = 0.01*cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,epsilon,True)

        cv2.drawContours(frame,[approx],0,(0),5)

        x = approx.ravel()[0]

        y = approx.ravel()[1]

        if len(approx) == 3:
            cv2.putText(frame,"Triangle",(x,y),font1,1,(0))

        elif len(approx) == 4:
            cv2.putText(frame,"rectangle",(x,y),font1,1,(0))

        elif len(approx) == 5:
            cv2.putText(frame,"Pentagon",(x,y),font1,1,(0))

        elif len(approx) == 6:
            cv2.putText(frame,"Hexagon",(x,y),font2,1,(0))

        else:
            cv2.putText(frame,"Ellipse",(x,y),font2,1,(0))

    cv2.imshow("IMG",frame)
    cv2.imshow("gray img",gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    

cv2.waitKey(0)
cv2.destroyAllWindows()

""" 
Bu kodlar, bir webcam veya video kaynağından canlı görüntü alarak bu görüntü üzerinde çokgenleri ve elipsleri tespit eder ve bu şekilleri çizerek veya işaretleyerek belirtir. İşlemleri adım adım açıklayalım:

import cv2 ve import numpy as np: OpenCV ve NumPy kütüphaneleri kod içinde kullanılabilir hale getirilir.

font1 = cv2.FONT_HERSHEY_SIMPLEX ve font2 = cv2.FONT_HERSHEY_COMPLEX: Kullanılacak yazı fontları belirlenir.

cap = cv2.VideoCapture(0): Bilgisayarın kameradan veya başka bir video kaynağından görüntü almak için bir VideoCapture nesnesi oluşturulur. Parametre olarak 0, varsayılan kamerayı belirtir.

while True: ...: Sonsuz bir döngü başlatılır. Bu döngü, kameradan sürekli olarak yeni görüntüler alır ve işlemleri gerçekleştirir.

ret, frame = cap.read(): VideoCapture nesnesi üzerinden bir görüntü okunur ve frame değişkenine atanır.

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY): Okunan renkli görüntü gri tonlamalı görüntüye dönüştürülür.

_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY): Gri tonlamalı görüntü üzerinde bir eşikleme işlemi uygulanır. Bu işlem, görüntüyü siyah-beyaz bir formata dönüştürür.

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE): Eşiklenmiş görüntü üzerindeki konturlar (çizgiler) tespit edilir. Bu konturlar, görüntüdeki çokgenleri ve elipsleri temsil eder.

for cnt in contours: ...: Her kontur için döngü başlatılır. Her kontur, bir çokgen veya elipsi temsil eder.

epsilon = 0.01*cv2.arcLength(cnt, True): Her kontur için bir epsilon değeri hesaplanır. Bu değer, konturun köşelerini belirlemede kullanılır.

approx = cv2.approxPolyDP(cnt, epsilon, True): Konturun köşeleri yaklaşık olarak hesaplanır. Bu işlem, çokgenin köşelerini ve kenar sayısını belirler.

Şeklin türüne göre yazı eklenir ve kontur çizilir.

cv2.imshow("IMG", frame): İşlenmiş görüntüyü görselleştirir.

cv2.imshow("gray img", gray): Gri tonlamalı görüntüyü görselleştirir.

if cv2.waitKey(1) & 0xFF == ord('q'): ...: Klavyeden 'q' tuşuna basıldığında döngüden çıkılır ve program sonlandırılır.

cv2.waitKey(0): Bir tuşa basılmasını bekler. Herhangi bir tuşa basıldığında program devam eder.

cv2.destroyAllWindows(): Tüm açık pencereleri kapatır.

Bu kodlar, canlı bir video akışından görüntü alır, görüntü üzerinde çokgenleri ve elipsleri tespit eder, bu şekilleri çizerek veya işaretleyerek belirtir ve sonuçları görselleştirir. Özellikle şekil türlerini algılama ve işaretlemeye yönelik bir uygulamadır.

"""