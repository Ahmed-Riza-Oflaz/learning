import cv2

cap = cv2.VideoCapture("video1.mp4")

while True:
    ret , frame = cap.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if ret == False:
        break

    cv2.imshow("video",frame)

    if cv2.waitKey(30) % 0xFF == ord("q"):
        break


                    # Bu Python kodu, bir video dosyasını açarak gri tonlamalı (siyah beyaz) olarak görüntüler. Kodun adım adım açıklaması şu şekildedir:

                    # cv2.VideoCapture("video1.mp4"): "video1.mp4" adlı video dosyasını açar ve cap adlı bir VideoCapture nesnesine atar.
                    
                    # while True:: Sonsuz bir döngü başlatır. Bu döngü, video çerçevelerini okuyarak işleme devam eder.
                    
                    # ret , frame = cap.read(): cap nesnesinden bir video çerçevesi (frame) okur ve bu işlem başarılıysa ret değişkenine True değerini atar.
                    
                    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY): Okunan video çerçevesini BGR renk uzayından Gri tonlamalı (siyah beyaz) renk uzayına dönüştürür.
                    
                    # if ret == False:: Video çerçevesi başarıyla okunamazsa (ret değeri False ise), döngüyü sonlandırır (break).
                    
                    # cv2.imshow("video",frame): Gri tonlamalı olarak dönüştürülmüş video çerçevesini ekranda gösterir.
                    
                    # if cv2.waitKey(30) % 0xFF == ord("q"):: 30 milisaniye boyunca bir tuşa basılmasını bekler ve basılan tuşun "q" tuşu olup olmadığını kontrol eder. Eğer "q" tuşuna basılmışsa, döngüyü sonlandırır ve video oynatımını durdurur.
                    
                    # cap.release(): Video kaynağını serbest bırakır.
                    
                    # cv2.destroyAllWindows(): Açık olan tüm pencereleri kapatır.
                    
                    # Bu kod, belirtilen video dosyasını açarak her çerçeveyi gri tonlamalı olarak işleyerek ekranda gösterir ve "q" tuşuna basıldığında videoyu durdurur.




cap.release()
cv2.destroyAllWindows()