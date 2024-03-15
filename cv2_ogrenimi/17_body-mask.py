import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar", 500, 500)

cv2.createTrackbar("Lower - H", "Trackbar", 0, 180, nothing)
cv2.createTrackbar("Lower - S", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("Lower - V", "Trackbar", 0, 255, nothing)

cv2.createTrackbar("Upper - H", "Trackbar", 180, 180, nothing)
cv2.createTrackbar("Upper - S", "Trackbar", 255, 255, nothing)
cv2.createTrackbar("Upper - V", "Trackbar", 255, 255, nothing)

while True:
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_h = cv2.getTrackbarPos("Lower - H", "Trackbar")
    lower_s = cv2.getTrackbarPos("Lower - S", "Trackbar")
    lower_v = cv2.getTrackbarPos("Lower - V", "Trackbar")

    upper_h = cv2.getTrackbarPos("Upper - H", "Trackbar")
    upper_s = cv2.getTrackbarPos("Upper - S", "Trackbar")
    upper_v = cv2.getTrackbarPos("Upper - V", "Trackbar")

    lower_color = np.array([lower_h, lower_s, lower_v])
    upper_color = np.array([upper_h, upper_s, upper_v])

    mask = cv2.inRange(frame_hsv, lower_color, upper_color)

    cv2.imshow("original", frame)
    cv2.imshow("Mask", mask)

    if ret == False:
        break

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


"""
Bu kod, bir video kaynağından görüntü alır ve kullanıcının belirlediği renk aralığına göre maskeleme işlemi yapar. 

cv2.VideoCapture(0): Bilgisayarınızda mevcut olan bir kamera cihazından görüntü almak için bir VideoCapture nesnesi oluşturur. Kameranın 
numarası 0 olarak belirtilmiştir.

def nothing(x): pass: Trackbar'ların varsayılan değerini belirlemek için bir fonksiyon tanımlanır.

Trackbar'ların oluşturulması:

cv2.createTrackbar("Lower - H", "Trackbar", 0, 180, nothing): Alt sınır renk değeri için bir Trackbar oluşturur.
cv2.createTrackbar("Lower - S", "Trackbar", 0, 255, nothing): Alt sınır doygunluk değeri için bir Trackbar oluşturur.
cv2.createTrackbar("Lower - V", "Trackbar", 0, 255, nothing): Alt sınır parlaklık değeri için bir Trackbar oluşturur.
cv2.createTrackbar("Upper - H", "Trackbar", 0, 180, nothing): Üst sınır renk değeri için bir Trackbar oluşturur.
cv2.createTrackbar("Upper - S", "Trackbar", 0, 255, nothing): Üst sınır doygunluk değeri için bir Trackbar oluşturur.
cv2.createTrackbar("Upper - V", "Trackbar", 0, 255, nothing): Üst sınır parlaklık değeri için bir Trackbar oluşturur.
cv2.setTrackbarPos("Upper - H", "Trackbar", 180): Üst sınır renk değerini varsayılan olarak 180 olarak ayarlar.
cv2.setTrackbarPos("Upper - S", "Trackbar", 255): Üst sınır doygunluk değerini varsayılan olarak 255 olarak ayarlar.
cv2.setTrackbarPos("Upper - V", "Trackbar", 255): Üst sınır parlaklık değerini varsayılan olarak 255 olarak ayarlar.

while True:: Sonsuz bir döngü başlatır.

ret, frame = cap.read(): Kameradan bir kare alır.

frame = cv2.flip(frame, 1): Görüntüyü yatay olarak çevirir.

frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV): Görüntüyü BGR renk uzayından HSV renk uzayına dönüştürür.

Trackbar'lardan alınan değerlerle alt ve üst sınır renk aralıklarını oluşturur.

mask = cv2.inRange(frame_hsv, lower_color, upper_color): Belirlenen renk aralığında olan pikselleri maskeleme işlemiyle ayırır.

cv2.imshow("original", frame): Orijinal görüntüyü ekranda gösterir.
cv2.imshow("Mask", mask): Maskeleme sonucunu ekranda gösterir.

Kullanıcının "q" tuşuna basması durumunda döngüyü sonlandırır ve kaynakları serbest bırakır.

Bu kod, kullanıcının Trackbar'ları kullanarak belirlediği renk aralığında olan nesneleri maskeleme işlemi yaparak görüntülemeyi sağlar.

"""