import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    ret , frame = cap.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    sensevity = 15

    lower_while = np.array([0,0,255-sensevity])

    upper_while = np.array([255,sensevity,255])

    mask = cv2.inRange(hsv,lower_while,upper_while)

    res = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("result",res)

    k = cv2.waitKey(5) & 0xFF

    if k == 27:
        break


""" 
Bu kodlar, bir kameradan video akışı alır ve bu video akışı üzerinde renk algılama yapar. Özellikle, beyaz renge duyarlı bir maske oluşturarak beyaz nesneleri tespit etmeye çalışır. İşte kodların yaptığı işlemler:

import cv2 ve import numpy as np: OpenCV ve NumPy kütüphaneleri kod içinde kullanılabilir hale getirilir.

cap = cv2.VideoCapture(0): Kamerayı başlatır ve video akışını alır. 0 parametresi, birincil kamerayı temsil eder. Daha fazla kamera varsa, bu parametre değiştirilebilir.

while(1):: Sonsuz bir döngü başlatır. Kameradan sürekli olarak yeni kareler alır ve işler.

ret, frame = cap.read(): Kameradan bir kare (frame) okur ve bu kareyi frame değişkenine atar. ret değeri, kare okuma işleminin başarılı olup olmadığını gösterir.

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV): Okunan kareyi renk uzayını HSV'ye (Hue, Saturation, Value) dönüştürür. Bu, renk algılama için daha uygun bir formattır.

sensevity = 15: Renk duyarlılık değerini belirler. Bu değer, renk aralığını genişletmek veya daraltmak için kullanılır.

lower_while = np.array([0, 0, 255 - sensevity]) ve upper_while = np.array([255, sensevity, 255]): Beyaz renge duyarlı bir maske oluşturmak için alt ve üst sınırlar belirlenir. Bu renk aralığı, beyaz renk tonlarını algılamak için kullanılır.

mask = cv2.inRange(hsv, lower_while, upper_while): Belirtilen renk aralığına göre bir maske oluşturur. Bu maske, beyaz renge duyarlı olduğu için beyaz nesneleri belirler.

res = cv2.bitwise_and(frame, frame, mask=mask): Maskeyi kullanarak orijinal kare üzerinde beyaz nesneleri belirler. Bu işlem, beyaz renk alanları dışında kalan diğer renkleri siyah yapar.

cv2.imshow("frame", frame), cv2.imshow("mask", mask), cv2.imshow("result", res): İşlenmiş kareleri ve maskeleri görselleştirir.

k = cv2.waitKey(5) & 0xFF: Kullanıcının bir tuşa basmasını bekler. 5 milisaniye içinde bir tuş basılırsa, döngüye devam eder.

if k == 27: break: Eğer kullanıcı "Esc" tuşuna basarsa (ASCII değeri 27), döngüyü sonlandırır ve programı kapatır.

Bu kodlar, beyaz renkli nesneleri tespit etmek için kullanılır. HSV renk uzayını kullanarak belirli bir renk aralığında (burada beyaz) nesneleri algılar ve bu nesneleri görüntü üzerinde görselleştirir.

"""