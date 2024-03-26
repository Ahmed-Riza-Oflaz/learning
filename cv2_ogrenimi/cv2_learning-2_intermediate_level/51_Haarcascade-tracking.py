import cv2


cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:

    ret , frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)



    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x + w, y + h ),(0,0,255), thickness= 2 )



    cv2.imshow("image",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




cap.release()
cv2.destroyAllWindows()

""" 
Bu kodlar, kameradan canlı bir video akışı alır ve bu akış üzerinde yüz tespiti yaparak yüzleri çerçeveleme işlemini gerçekleştirir. Kodların işlevleri şu şekildedir:

import cv2: OpenCV kütüphanesini içe aktarır.

cap = cv2.VideoCapture(0): Kamerayı başlatır (0 argümanıyla varsayılan kamera kullanılır).

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml'): Yüz tespiti için önceden eğitilmiş haarcascade yüz tanıma sınıflandırıcısını yükler.

while True:: Sonsuz bir döngü başlatır.

ret , frame = cap.read(): Kameradan bir kare okur ve bu kareyi frame değişkenine atar.

Kareyi gri tonlamalıya dönüştürür (gray adında bir değişkende saklar).

Gri tonlamalı görüntü üzerinde yüz tespiti yapar ve tespit edilen yüzleri çerçeveleyerek gösterir.

Çerçevelenmiş görüntüyü ekranda gösterir.

Eğer klavyeden 'q' tuşuna basılırsa döngüyü sonlandırır ve programı kapatır.

cap.release(): Kamerayı serbest bırakır.

cv2.destroyAllWindows(): Tüm OpenCV pencerelerini kapatır.

Bu kodlar, kameradan alınan görüntü üzerinde haarcascade yüz tespiti kullanarak yüzleri tespit eder ve bu yüzleri çerçeveleyerek gösterir. Yüz tespiti gibi özellikler, genellikle güvenlik sistemleri, otomatik fotoğraf çekimi gibi uygulamalarda kullanılır.

"""