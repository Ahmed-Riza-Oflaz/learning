import cv2
import numpy as np

# Göz tanımlama için Cascade sınıflandırıcısını yükleme
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Kamerayı başlatma
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Gri tonlamalı görüntü elde etme
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Gözleri tanımlama
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Tanımlanan gözleri dikdörtgenle çevreleme ve göz merkezini bulma
    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        eye_center = (x + w // 2, y + h // 2)
        cv2.circle(frame, eye_center, 3, (255, 0, 0), -1)

        # Göz merkezini takip etmek için bir çizgi çizme
        cv2.line(frame, (frame.shape[1] // 2, frame.shape[0] // 2), eye_center, (0, 0, 255), 2)

    # Çerçeveyi gösterme
    cv2.imshow('Eye Tracking', frame)

    # Çıkış için 'q' tuşuna basma kontrolü
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera serbest bırakma ve pencereleri kapatma
cap.release()
cv2.destroyAllWindows()
