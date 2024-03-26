import cv2
import numpy as np

# Telefonun IP adresi ve bağlantı portu
url = "http://192.168.45.2:8080/video"

# IP Webcam'den görüntü almak için VideoCapture kullanımı
cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Görüntü alınamıyor.")
        break
    
    frame = cv2.resize(frame,(640,480))


    cv2.imshow('Frame', frame)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()

""" 
Bu kodlar, bir IP Webcam uygulamasından video akışı alır ve bu akışı görüntüler. Kodların işlevleri şu şekildedir:

import cv2, import numpy as np: OpenCV ve NumPy kütüphanelerini içe aktarır.

url = "http://192.168.43.1:8080/video": IP Webcam uygulamasının video akışı için URL adresini belirtir. Bu URL adresi, IP Webcam uygulamasının çalıştığı cihazın IP adresi ve bağlantı portunu içerir.

cap = cv2.VideoCapture(url): VideoCapture nesnesi oluşturarak belirtilen URL adresinden video akışı almayı başlatır.

while True:: Sonsuz bir döngü başlatır.

ret, frame = cap.read(): Video akışından bir kare okur ve bu kareyi frame değişkenine atar.

Eğer kare alınamazsa (ret değeri False ise), "Görüntü alınamıyor." mesajını yazdırır ve döngüden çıkar.

Okunan kareyi 640x480 boyutuna yeniden boyutlandırır.

Yeniden boyutlandırılmış kareyi ekranda gösterir.

Eğer klavyeden 'q' tuşuna basılırsa döngüyü sonlandırır.

cap.release(): Video akışı alımını durdurur ve kaynakları serbest bırakır.

cv2.destroyAllWindows(): Tüm OpenCV pencerelerini kapatır.

Bu kodlar, IP Webcam uygulamasından alınan video akışını görüntüler ve kullanıcı tarafından 'q' tuşuna basıldığında programı sonlandırır. Bu tür kodlar genellikle uzaktan video izleme veya IP kamera entegrasyonu gibi uygulamalarda kullanılır.

"""