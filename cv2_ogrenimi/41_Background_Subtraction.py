import cv2
import numpy as np

cap = cv2.VideoCapture("C:/Users/Acer/OneDrive/Masaüstü/python/car.mp4")

_,first_frame = cap.read()

first_frame = cv2.resize(first_frame,(640,480))

first_gray = cv2.cvtColor(first_frame,cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray,(5,5),0)

while 1:

    _,frame = cap.read()

    frame = cv2.resize(frame,(640,480))

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(5,5),0)

    diff = cv2.absdiff(first_gray,gray)

    _,diff = cv2.threshold(diff,25,255,cv2.THRESH_BINARY)

    cv2.imshow("frame",frame)
    cv2.imshow("first", first_frame )
    cv2.imshow("diff",diff)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

""" 
Bu kodlar, bir video dosyasından araç hareketini tespit etmek için kullanılır. İşleyişini adım adım açıklayalım:

import cv2 ve import numpy as np: OpenCV ve NumPy kütüphaneleri kod içinde kullanılabilir hale getirilir.

cap = cv2.VideoCapture("C:/Users/Acer/OneDrive/Masaüstü/python/car.mp4"): Belirtilen yol üzerindeki video dosyasını açar ve VideoCapture nesnesi oluşturur.

İlk kare (first_frame) okunur ve işlenir:

_, first_frame = cap.read(): VideoCapture nesnesi üzerinden ilk kare okunur ve first_frame değişkenine atanır.
first_frame = cv2.resize(first_frame, (640, 480)): İlk kare boyutlandırılır.
first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY): İlk kare gri tonlamalıya dönüştürülür.
first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0): Gürültüyü azaltmak için Gauss filtresi uygulanır.

Sonsuz bir döngü başlatılır (while 1:). Bu döngü, video akışından sürekli olarak yeni kareler alır ve işlemleri gerçekleştirir.

Video akışından yeni bir kare (frame) okunur ve işlenir:

_, frame = cap.read(): VideoCapture nesnesi üzerinden bir sonraki kare okunur ve frame değişkenine atanır.
frame = cv2.resize(frame, (640, 480)): Okunan kare boyutlandırılır.
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY): Okunan kare gri tonlamalıya dönüştürülür.
gray = cv2.GaussianBlur(gray, (5, 5), 0): Gürültüyü azaltmak için Gauss filtresi uygulanır.

İlk kare ile mevcut kare arasındaki fark tespit edilir (diff = cv2.absdiff(first_gray, gray)).

Fark görüntüsü üzerinde belirli bir eşik değeri kullanılarak ikili bir maske oluşturulur (_, diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)).

İşlenmiş kareler (frame, first_frame, diff) ekranda gösterilir (cv2.imshow()).

Klavyeden 'q' tuşuna basıldığında döngüden çıkılır ve program sonlandırılır.

VideoCapture nesnesi serbest bırakılır (cap.release()) ve tüm açık pencereler kapatılır (cv2.destroyAllWindows()).

Bu kodlar, video akışı üzerinde hareket algılama işlemi gerçekleştirerek, belirli bir eşik değerini aşan farklılıkları görselleştirir. Özellikle güvenlik kameralarında veya trafik izleme sistemlerinde araç hareketlerini tespit etmek için kullanılabilir.


"""