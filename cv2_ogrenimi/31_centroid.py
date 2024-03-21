import cv2
import numpy as np

img = cv2.imread("./images.jpeg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret , thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]

area = cv2.contourArea(cnt)
print(area)

M = cv2.moments(cnt)

print(M)

perimeter = cv2.arcLength(cnt,True)

print(perimeter)

cv2.imshow("Sonuç", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

""" 
Bu kod örnek bir kontur analizi yapar. İşte her bir bölümün ne işe yaradığına dair bir açıklama:

img = cv2.imread("./images.jpeg"): "images.jpeg" adlı bir resim dosyasını okur.

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY): Resmi gri tonlama dönüşümü yaparak gri tonlu bir görüntü elde eder.

ret , thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY): Gri tonlu görüntüyü ikili bir görüntüye dönüştürmek için eşik değeriyle işlem yapar.

contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE): Eşiklenmiş görüntüdeki konturları bulur. contours değişkeni, kontur bilgilerini içeren bir liste olur.

cnt = contours[0]: İlk konturu seçer.

area = cv2.contourArea(cnt): Konturun alanını hesaplar.

M = cv2.moments(cnt): Konturun momentlerini hesaplar.

perimeter = cv2.arcLength(cnt,True): Konturun çevresini hesaplar.

cv2.imshow("Sonuç", img): İşlenmiş görüntüyü ekranda gösterir.

cv2.waitKey(0): Kullanıcının bir tuşa basmasını bekler.

cv2.destroyAllWindows(): Tüm açık pencereleri kapatır.

Bu kod parçacığı, konturların alanını, momentlerini ve çevresini hesaplar ve bu bilgileri ekrana yazdırır. Bu tür analizler genellikle nesne tespiti, nesne tanıma ve şekil analizi gibi görüntü işleme uygulamalarında kullanılır.

"""

"""  
cv2 modülündeki kontur analizi, görüntülerdeki nesnelerin sınırlarını, şekillerini ve diğer özelliklerini analiz etmek için kullanılır. Kontur analizi, görüntü işleme ve bilgisayarlı görüş uygulamalarında birçok faydalı işlevi yerine getirir. İşte kontur analizinin temel amaçları:

Nesne Tanıma ve Algılama: Kontur analizi, nesnelerin sınırlarını belirleyerek nesne tanıma ve algılama işlemlerinde kullanılır. Nesnelerin şekilleri, boyutları ve diğer özellikleri üzerinde analiz yaparak farklı nesneleri ayırt etmeye ve tanımaya yardımcı olur.

Hareket Algılama: Video görüntülerindeki hareketi algılamak için kontur analizi kullanılabilir. Nesnelerin hareket eden kısımlarını belirleyerek hareketli nesneleri tespit etmek mümkündür.

Nesne Sayma ve Ölçme: Kontur analizi, görüntülerdeki nesne sayısını ve boyutlarını ölçmek için kullanılabilir. Örneğin, ürün paketlerini saymak veya belirli bir boyutta olan nesneleri ölçmek için kullanışlıdır.

Alan Hesaplama: Nesnelerin alanlarını hesaplamak için kontur analizi kullanılır. Bu, tarım alanında bitki sayımı veya endüstriyel uygulamalarda ürün sayımı gibi alanlarda kullanışlıdır.

Öznitelik Çıkarımı: Kontur analizi ile nesnelerin çeşitli öznitelikleri çıkarılabilir. Örneğin, merkez noktası, dış çevre uzunluğu, alan, eksen oranı gibi öznitelikler elde edilebilir.

Kesir Analizi: İki nesne arasındaki kesir analizi yapılabilir. Bu, nesnelerin birbirine olan bağlılığını veya ilişkilerini analiz etmek için kullanılabilir.

Kontur analizi, temel olarak bir görüntüdeki şekil ve yapıları tespit etmek, özelliklerini çıkarmak ve bu bilgileri kullanarak çeşitli işlemler yapmak için kullanılır. Bu işlemler genellikle nesne tanıma, hareket algılama, nesne sayma, öznitelik çıkarımı gibi alanlarda kullanılmaktadır.

"""