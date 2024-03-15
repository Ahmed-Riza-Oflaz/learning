import cv2
import numpy as np

#############--Bu kod, kullanıcının renk kanallarını ve anahtarı ayarlayarak gerçek zamanlı olarak bir görüntünün rengini değiştirebileceği basit bir arayüz sağlar.

def nothing(x):
    pass

                #nothing() işlevi, createTrackbar() işlevinin olay işleyicisi olarak atanır ve bir şey yapmaz, yani geçerlidir.

img = np.zeros((412,612,3), np.uint8)

cv2.namedWindow("image")

cv2.createTrackbar("R", "image", 0, 255, nothing)
cv2.createTrackbar("G", "image", 0, 255, nothing)
cv2.createTrackbar("B", "image", 0, 255, nothing)

                #createTrackbar() işlevi, bir pencereye bir veya daha fazla kaydırıcı ekler. Bu örnekte, "image" adlı pencereye üç renk kanalı için kaydırıcılar ve bir anahtar için bir anahtar kaydırıcısı eklenir.

switch = "0: OFF, 1: ON"

cv2.createTrackbar(switch, "image", 0, 1, nothing)

while True:
    
    cv2.imshow("image", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

                #Bu kod parçası, kullanıcının "q" tuşuna basarak programı sonlandırmasını sağlar.

                # cv2.waitKey(1) fonksiyonu, programın 1 milisaniye boyunca beklemesini ve kullanıcıdan bir tuşa basmasını bekler. Bu, programın kullanıcı girişine yanıt vermesini sağlar ve aynı zamanda programın çökmemesini veya yanıt vermeyi durdurmasını engeller.

                # & 0xFF == ord("q") ifadesi, beklenen tuşa basılıp basılmadığını kontrol eder. Bu durumda, beklenen tuş "q" olduğu için, "q" tuşuna basıldığında ifade doğru olur ve döngüden çıkılır, yani program sonlanır.

                # Bu, kullanıcının programı kapatmak için "q" tuşunu kullanmasını sağlar.

    r = cv2.getTrackbarPos("R", "image")
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image")

                #getTrackbarPos() işlevi, bir kaydırıcının geçerli pozisyonunu döndürür. Bu örnekte, "R", "G" ve "B" adlı renk kaydırıcılarının pozisyonları alınır ve değişkenlere atanır.

    s = cv2.getTrackbarPos(switch, "image")

                #Anahtarın değeri (açık veya kapalı) s değişkeninde saklanır.

    if s == 0:
        img[:] = [0,0,0]
    else:
        img[:] = [b,g,r]

                # Bu kod parçası, anahtarın değeri (switch) 0 olduğunda, yani anahtar kapalı olduğunda, görüntüyü siyah renge ayarlar.

                # img[:] = [0, 0, 0] ifadesi, img dizisinin tüm elemanlarını sıfırlar. Bu durumda, img bir siyah görüntü oluşturur, çünkü siyah bir renk, tüm renk kanallarında (kırmızı, yeşil, mavi) sıfır değerine sahiptir.

                # Bu, anahtarın kapalı olduğunda görüntünün siyah olarak ayarlanmasını sağlar.

cv2.destroyAllWindows()