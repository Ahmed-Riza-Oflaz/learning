import cv2
import numpy as np 

vid = cv2.VideoCapture("C:/Users/Acer/OneDrive/Masaüstü/python/line.mp4")

while True:

    ret , frame = vid.read()

    frame = cv2.resize(frame, (640, 480))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_yellow = np.array([18, 94, 140], np.uint8)
    upper_yellow = np.array([48, 255, 255], np.uint8)

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    edges = cv2.Canny(mask, 75, 250)

    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=50)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow("frame video", frame)
    cv2.imshow("mask video", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()


""" 
Bu kodlar bir video dosyası üzerinde sarı renkli çizgileri tespit ederek bu çizgileri yeşil renkte kalın çizgilerle işaretler. İşte kodların yaptığı işlemler:

import cv2 ve import numpy as np: OpenCV ve NumPy kütüphaneleri kod içinde kullanılabilir hale getirilir.

vid = cv2.VideoCapture("C:/Users/Acer/OneDrive/Masaüstü/python/line.mp4"): Belirtilen dosya yolundaki videoyu açar ve video akışını alır.

while True:: Sonsuz bir döngü başlatır. Video akışından sürekli olarak yeni kareler alır ve işler.

ret, frame = vid.read(): Video akışından bir kare (frame) okur ve bu kareyi frame değişkenine atar. ret değeri, kare okuma işleminin başarılı olup olmadığını gösterir.

frame = cv2.resize(frame, (640, 480)): Okunan kareyi yeniden boyutlandırır. Bu, görüntünün boyutunu belirli bir boyuta ayarlamak için kullanılır.

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV): Okunan kareyi renk uzayını HSV'ye (Hue, Saturation, Value) dönüştürür. Bu, renk algılama ve ayırma işlemleri için daha uygun bir formattır.

lower_yellow ve upper_yellow: Sarı renk aralığını belirler. Bu renk aralığı, sarı renkli nesneleri maskelemek için kullanılır.

mask = cv2.inRange(hsv, lower_yellow, upper_yellow): Belirtilen renk aralığına göre bir maske oluşturur. Bu maske, sarı renkli nesneleri belirler.

edges = cv2.Canny(mask, 75, 250): Maske üzerinde kenar tespiti algoritması olan Canny'yi uygular. Bu, sarı renkli nesnelerin kenarlarını belirler.

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=50): Kenarlar üzerinde Hough dönüşümü yaparak çizgi tespiti yapar. Bu çizgiler, sarı renkli çizgileri temsil eder.

if lines is not None:: Eğer çizgiler tespit edilmişse:

for line in lines: ...: Her çizgi için döngü başlatır ve çizgileri yeşil renkte kalın çizgilerle işaretler.

cv2.imshow("frame video", frame), cv2.imshow("mask video", mask): İşlenmiş kareleri ve maskeleri görselleştirir.

if cv2.waitKey(1) & 0xFF == ord('q'): break: Kullanıcı "q" tuşuna basarsa veya pencereyi kapatırsa döngüyü sonlandırır.

vid.release(): Video kaynağını serbest bırakır.

cv2.destroyAllWindows(): Tüm OpenCV pencelerini kapatır.

Bu kodlar, sarı renkli çizgileri tespit etmek için renk algılama, maskeleme, kenar tespiti ve Hough dönüşümü gibi işlemleri kullanır ve bu çizgileri görüntü üzerinde yeşil renkte kalın çizgilerle işaretler.


"""