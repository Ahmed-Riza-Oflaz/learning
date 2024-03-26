import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)


    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=22)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)
            cv2.putText(frame, 'Smile Detected', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    cv2.imshow('Smile Detection', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

""" 
Bu kodlar, kameradan canlı bir video akışı alır ve bu akış üzerinde yüz tespiti ve gülümseme tespiti yaparak gülümseyen yüzleri çerçeveleme ve gülümseme tespit edildiğinde bir metinle işaretleme işlemlerini gerçekleştirir. Kodların işlevleri şu şekildedir:

import cv2: OpenCV kütüphanesini içe aktarır.

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'): Yüz tespiti için önceden eğitilmiş haarcascade yüz tanıma sınıflandırıcısını yükler.

smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml'): Gülümseme tespiti için önceden eğitilmiş haarcascade gülümseme tanıma sınıflandırıcısını yükler.

cap = cv2.VideoCapture(0): Kamerayı başlatır (0 argümanıyla varsayılan kamera kullanılır).

while True:: Sonsuz bir döngü başlatır.

ret, frame = cap.read(): Kameradan bir kare okur ve bu kareyi frame değişkenine atar.

Kareyi gri tonlamalıya dönüştürür (gray adında bir değişkende saklar).

Yüzleri tespit eder ve bu yüzleri çerçeveleyerek gösterir.

Her tespit edilen yüz için, yüz bölgesini (roi_gray ve roi_color) belirler.

Gülümseme tespiti yapar ve gülümseyen yüzleri çerçeveleyerek gösterir.

Gülümseme tespit edildiğinde, kare üzerinde bir metinle gülümseme tespit edildiğini belirtir.

İşlenmiş görüntüyü ekranda gösterir.

Eğer klavyeden 'q' tuşuna basılırsa döngüyü sonlandırır ve programı kapatır.

cap.release(): Kamerayı serbest bırakır.

cv2.destroyAllWindows(): Tüm OpenCV pencerelerini kapatır.

Bu kodlar, kameradan alınan görüntü üzerinde yüz ve gülümseme tespiti yaparak bu özellikleri görsel olarak işaretler. Gülümseme tespiti gibi özellikler, genellikle duygu analizi ve insan davranışı analizi gibi alanlarda kullanılır.

"""