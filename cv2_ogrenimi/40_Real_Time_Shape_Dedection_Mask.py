import cv2
import numpy as np

font1 = cv2.FONT_HERSHEY_SIMPLEX
font2 = cv2.FONT_HERSHEY_COMPLEX

def nothing(x):
      pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("Settings")

cv2.createTrackbar("Lower-Hue","Settings",0,180,nothing)
cv2.createTrackbar("Lower-Saturation","Settings",0,255,nothing)
cv2.createTrackbar("Lower-Value","Settings",0,255,nothing)

cv2.createTrackbar("Upper-Hue","Settings",0,180,nothing)
cv2.createTrackbar("Upper-Saturation","Settings",0,255,nothing)
cv2.createTrackbar("Upper-Value","Settings",0,255,nothing)

while 1:

    ret , frame = cap.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    frame = cv2.flip(frame,1)

    lh = cv2.getTrackbarPos("Lower-Hue","Settings")
    ls = cv2.getTrackbarPos("Lower-Saturation","Settings")
    lv = cv2.getTrackbarPos("Lower-Value","Settings")

    uh = cv2.getTrackbarPos("Upper-Hue","Settings")
    us = cv2.getTrackbarPos("Upper-Saturation","Settings")
    uv = cv2.getTrackbarPos("Upper-Value","Settings")

    lowe_color = np.array([lh,ls,lv])
    upper_color = np.array([uh,us,uv])

    mask = cv2.inRange(hsv,lowe_color,upper_color)
    kernel = np.ones((5,5),np.uint8)
    mask = cv2.erode(mask,kernel)

    mask = cv2.flip(mask,1)

    contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        epsilon = 0.02*cv2.arcLength(cnt,True)

        approx = cv2.approxPolyDP(cnt,epsilon,True)

        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if area > 400:
            cv2.drawContours(frame,[approx],0,(0,0,0),5)

            if len(approx) == 3:
                cv2.putText(frame, "Triangle", (x, y), font1, 1, (0, 0, 0), 2)

            elif len(approx) == 4:
                cv2.putText(frame, "Rectangle", (x, y), font1, 1, (0, 0, 0), 2)

            elif len(approx) == 5:
                cv2.putText(frame, "Pentagon", (x, y), font1, 1, (0, 0, 0), 2)

            elif len(approx) == 6:
                cv2.putText(frame, "Hexagon", (x, y), font2, 1, (0, 0, 0), 2)

            else:
                cv2.putText(frame, "Ellipse", (x, y), font2, 1, (0, 0, 0), 2)

    cv2.imshow("frame",frame)
    cv2.imshow("frame mask",mask)

    if cv2.waitKey(3) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

""" 
Bu kodlar, bir webcam veya video kaynağından canlı görüntü alarak görüntü üzerinde renk algılama ve şekil tanıma işlemleri gerçekleştirir. Kodların işleyişini adım adım açıklayalım:

import cv2 ve import numpy as np: OpenCV ve NumPy kütüphaneleri kod içinde kullanılabilir hale getirilir.

font1 = cv2.FONT_HERSHEY_SIMPLEX ve font2 = cv2.FONT_HERSHEY_COMPLEX: Kullanılacak yazı fontları belirlenir.

def nothing(x): pass: Trackbar (izleme çubuğu) için boş bir işlev tanımlanır.

cap = cv2.VideoCapture(0): Bilgisayarın kameradan veya başka bir video kaynağından görüntü almak için bir VideoCapture nesnesi oluşturulur. Parametre olarak 0, varsayılan kamerayı belirtir.

Trackbar'lar oluşturulur ve ayarları yapılır:

"Lower-Hue", "Lower-Saturation", "Lower-Value": Alt eşikleme değerleri için trackbar'lar oluşturulur.
"Upper-Hue", "Upper-Saturation", "Upper-Value": Üst eşikleme değerleri için trackbar'lar oluşturulur.

Sonsuz bir döngü başlatılır (while 1:). Bu döngü, video akışından sürekli olarak yeni görüntüler alır ve işlemleri gerçekleştirir.

ret, frame = cap.read(): VideoCapture nesnesi üzerinden bir görüntü okunur ve frame değişkenine atanır.

Görüntü BGR formatından HSV formatına dönüştürülür (hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)).

Trackbar'ların değerleri alınarak renk aralıkları belirlenir ve bu renk aralıklarına göre bir maske oluşturulur.

Maske, görüntü üzerine uygulanır (cv2.bitwise_and(frame, frame, mask=mask)).

Maske üzerinde kontur analizi yapılır ve konturlar belirlenir.

Her kontur için alan ve köşe sayısı kontrol edilerek şekiller tespit edilir ve bu şekiller çizilerek veya işaretlenerek görüntü üzerinde belirtilir.

İşlenmiş görüntü ve maske görselleştirilir (cv2.imshow("frame", frame) ve cv2.imshow("frame mask", mask)).

Klavyeden 'q' tuşuna basıldığında döngüden çıkılır ve program sonlandırılır.

VideoCapture nesnesi serbest bırakılır (cap.release()) ve tüm açık pencereler kapatılır (cv2.destroyAllWindows()).

Bu kodlar, canlı bir video akışından görüntü alır, görüntü üzerinde renk algılama ve şekil tanıma işlemleri gerçekleştirir ve sonuçları görselleştirir. Özellikle renk tabanlı nesne tespiti ve şekil tanıma uygulamaları için kullanılabilir.


"""