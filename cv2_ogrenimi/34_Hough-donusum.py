import cv2
import numpy as np

img = cv2.imread("./h_line.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,75,150)

lines = cv2.HoughLinesP(edges,1,np.pi/180,threshold=50,maxLineGap=200)

for line in lines:
    (x1,y1,x2,y2) = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow("img",img)
cv2.imshow("gray",gray)
cv2.imshow("edges",edges)


cv2.waitKey(0)
cv2.destroyAllWindows()

#kod açıklaması-------------------------------------------------------------

""" 
Bu kodlar, bir görüntü üzerinde Hough Dönüşümü kullanarak çizgileri algılar ve görüntüye çizgiyi ekler. Kodların yaptığı işlemleri adım adım açıklayalım:

import cv2 ve import numpy as np: OpenCV ve NumPy kütüphanelerini projeye dahil eder.

img = cv2.imread("./h_line.png"): "./h_line.png" dosyasından bir görüntüyü okur.

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY): Görüntüyü gri tonlamalıya dönüştürür.

edges = cv2.Canny(gray,75,150): Kenarları algılamak için Canny kenar algılama yöntemini uygular.

lines = cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=200): Hough dönüşümü kullanarak çizgileri algılar. İkinci parametre olan 1, çözünürlüğü ifade eder. Üçüncü parametre olan np.pi/180, radyan biriminde açı çözünürlüğünü belirtir. Dördüncü parametre olan 50, çizgi oluşturmak için gereken en az oy sayısını belirtir. maxLineGap ise aynı çizgi üzerinde kabul edilebilir maksimum boşluk miktarını belirtir.

for line in lines:: Algılanan çizgilerin her biri için döngü oluşturulur.

(x1,y1,x2,y2) = line[0]: Çizginin başlangıç ve bitiş koordinatlarını alır.

cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2): Algılanan çizgileri renkli görüntü üzerine çizer. (0,255,0) yeşil renk için RGB değeridir, 2 ise çizgi kalınlığını belirtir.

cv2.imshow("img",img), cv2.imshow("gray",gray), cv2.imshow("edges",edges): İşlenmiş görüntüleri gösterir.

cv2.waitKey(0), cv2.destroyAllWindows(): Bir tuşa basılana kadar bekler ve ardından pencereleri kapatır.

Bu kodlarla, gri tonlamalı görüntü üzerinde kenarları algılar, Hough dönüşümü kullanarak çizgileri bulur ve bu çizgileri renkli görüntüye çizer.

"""
#Hough dönüşümü nedir ve nerede kullanılır------------------------------------

""" 
Hough Dönüşümü, özellikle doğrusal yapıları (örneğin, çizgiler veya daireler) algılamak için kullanılan bir görüntü işleme tekniğidir. Özellikle OpenCV gibi kütüphanelerde sıkça kullanılır. Hough Dönüşümü'nün temel amacı, bir görüntüdeki doğrusal yapıları algılamak ve bu yapıların denklem parametrelerini hesaplamaktır. İşte Hough Dönüşümü'nün kullanım alanları ve faydaları:

Çizgi Algılama: Hough Dönüşümü, özellikle kenar algılama işlemlerinden sonra çizgileri algılamak için kullanılır. Bu çizgiler genellikle farklı açılarda olabilir ve Hough Dönüşümü, bu çizgilerin denklemlerini hesaplayarak görüntü üzerindeki doğrusal yapıları tanımlar.

Daire Algılama: Aynı şekilde, Hough Dönüşümü daireleri algılamak için de kullanılabilir. Bu, dairelerin merkez noktalarını ve yarıçaplarını belirlemek için kullanışlıdır.

Şekil Tespiti: Doğrusal olmayan şekilleri (örneğin, dikdörtgenler veya elipsler) algılamak için genişletilmiş Hough Dönüşümü kullanılabilir.

Görüntü Tabanlı Modelleme: Hough Dönüşümü, bir görüntüdeki belirli yapıları modellemek ve analiz etmek için kullanılabilir. Örneğin, bir çizginin görüntüdeki pozisyonunu, açısını ve uzunluğunu belirlemek için kullanılabilir.

Robust Algılama: Hough Dönüşümü, gürültülü ortamlarda veya karmaşık arka planlarda bile doğrusal yapıları güvenilir bir şekilde algılayabilir. Bu özelliği, görüntü işleme uygulamalarında kullanılmasını önemli kılar.

Genel olarak, Hough Dönüşümü, görüntüdeki doğrusal veya dairesel yapıları algılamak ve bu yapıların matematiksel açıdan temsil edilmesini sağlamak için kullanılan güçlü bir araçtır. Bu, nesne tanıma, otomasyon, robotik ve benzeri alanlarda yaygın olarak kullanılan bir tekniktir.

"""