import cv2
import numpy as np

def nothing(x):
      pass

cap  = cv2.VideoCapture(0)

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

    frame = cv2.resize(frame,(640,480))

    lh = cv2.getTrackbarPos("Lower-Hue","Settings")
    ls = cv2.getTrackbarPos("Lower-Saturation","Settings")
    lv = cv2.getTrackbarPos("Lower-Value","Settings")

    uh = cv2.getTrackbarPos("Upper-Hue","Settings")
    us = cv2.getTrackbarPos("Upper-Saturation","Settings")
    uv = cv2.getTrackbarPos("Upper-Value","Settings")

    lowe_color = np.array([lh,ls,lv])
    upper_color = np.array([uh,us,uv])

    mask = cv2.inRange(hsv,lowe_color,upper_color)


    mask = cv2.flip(mask,1)

    mask = cv2.resize(mask,(640,480))

    bitwise = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("Bitwise and",bitwise)
    cv2.imshow("frame",frame)
    cv2.imshow("frame mask",mask)

    if cv2.waitKey(3) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

"""" 
36 102 51


Bu kodlar, webcam'den canlı görüntü alarak kullanıcı tarafından belirlenen renk aralığında nesneleri tespit etmek için kullanılır. İşleyişini adım adım açıklayalım:

import cv2 ve import numpy as np: OpenCV ve NumPy kütüphaneleri kod içinde kullanılabilir hale getirilir.

def nothing(x): pass: Trackbar'ın herhangi bir hareketi algıladığında bir işlem yapılmasını sağlayan boş bir işlev tanımlanır.

cap = cv2.VideoCapture(0): Bilgisayarın webcam'ini açar ve VideoCapture nesnesi oluşturur.

cv2.namedWindow("Settings"): Ayarlar penceresi oluşturulur.

Alt ve üst renk aralıklarını belirlemek için trackbarlar oluşturulur (createTrackbar fonksiyonu kullanılır).

Sonsuz bir döngü başlatılır (while 1:). Bu döngü, webcam'den sürekli olarak yeni kareler alır ve işleme sokar.

Webcam'den bir kare alınır (ret, frame = cap.read()).

Alınan kare HSV renk uzayına dönüştürülür (hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)).

Alt ve üst renk aralıkları trackbar'lardan okunur (lh = cv2.getTrackbarPos("Lower-Hue", "Settings"), vs.).

Belirlenen renk aralığına göre maske oluşturulur (mask = cv2.inRange(hsv, lower_color, upper_color)).

Orijinal kare üzerinde maskeleme işlemi yapılır (bitwise = cv2.bitwise_and(frame, frame, mask=mask)).

Oluşturulan görüntüler ekranda gösterilir (cv2.imshow kullanılarak).

Klavyeden 'q' tuşuna basıldığında döngüden çıkılır ve program sonlandırılır.

VideoCapture nesnesi serbest bırakılır (cap.release()) ve tüm açık pencereler kapatılır (cv2.destroyAllWindows()).

Bu kodlar, renk bazlı nesne tespiti ve maskeleme işlemi yaparak, belirlenen renk aralığına sahip nesneleri görsel olarak vurgular. Özellikle renk bazlı nesne takibi veya tespiti için kullanılabilir.


"""