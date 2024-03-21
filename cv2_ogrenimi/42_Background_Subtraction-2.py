import cv2
import numpy as np

cap = cv2.VideoCapture("C:/Users/Acer/OneDrive/Masaüstü/python/car.mp4")

subtractor = cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=90,detectShadows=True)

while 1:

    _,frame = cap.read()

    frame = cv2.resize(frame,(640,480))

    mask = subtractor.apply(frame)

    cv2.imshow("frame",frame)
    cv2.imshow("frame mask",mask)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

"""  
Bu kodlar, video akışında arka plan çıkarma işlemi yapmak için kullanılır. İşleyişini adım adım açıklayalım:

import cv2 ve import numpy as np: OpenCV ve NumPy kütüphaneleri kod içinde kullanılabilir hale getirilir.

cap = cv2.VideoCapture("C:/Users/Acer/OneDrive/Masaüstü/python/car.mp4"): Belirtilen yol üzerindeki video dosyasını açar ve VideoCapture nesnesi oluşturur.

subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=90, detectShadows=True): MOG2 (Gauss Karışım Tabanlı Arka Plan Çıkarıcı) algoritmasını kullanarak bir arka plan çıkarma nesnesi (subtractor) oluşturulur. Bu nesne, geçmiş kare sayısı (history), varyans eşik değeri (varThreshold), ve gölgelerin tespit edilip edilmeyeceği (detectShadows) gibi parametrelerle yapılandırılabilir.

Sonsuz bir döngü başlatılır (while 1:). Bu döngü, video akışından sürekli olarak yeni kareler alır ve arka plan çıkarma işlemi gerçekleştirir.

Video akışından yeni bir kare (frame) okunur ve boyutlandırılır (frame = cv2.resize(frame, (640, 480))).

Arka plan çıkarma işlemi yapılır ve maske oluşturulur (mask = subtractor.apply(frame)).

Orijinal kare ve oluşturulan maske ekranda gösterilir (cv2.imshow("frame", frame) ve cv2.imshow("frame mask", mask)).

Klavyeden 'q' tuşuna basıldığında döngüden çıkılır ve program sonlandırılır.

VideoCapture nesnesi serbest bırakılır (cap.release()) ve tüm açık pencereler kapatılır (cv2.destroyAllWindows()).

Bu kodlar, MOG2 algoritması kullanılarak arka plan çıkarma işlemi yaparak, video akışında hareketli nesnelerin tespitini kolaylaştırır. Özellikle hareketli nesneleri izlemek veya hareket tespiti yapmak için güvenlik kameralarında veya trafik izleme sistemlerinde kullanılabilir.

"""