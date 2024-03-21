import cv2
import numpy as np

img = cv2.imread("../g1.jpeg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur = cv2.blur(gray,(3,3))

ret , thresh = cv2.threshold(blur,150,255,cv2.THRESH_BINARY)

contours,hıerarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

hull = []

for i in range(len(contours)):
    hull.append(cv2.convexHull(contours[i],False))

bg = np.zeros((thresh.shape[0],thresh.shape[1],3),np.uint8)

for i in range(len(contours)):
    cv2.drawContours(bg,contours,i,(255,0,0),3,8,)
    cv2.drawContours(bg,hull,i,(0,255,0),1,8)

cv2.imshow("original",img)
cv2.imshow("gray",gray)
cv2.imshow("blur",blur)
cv2.imshow("thresh",thresh)

cv2.imshow("ımage-contor",bg)

cv2.waitKey(0)
cv2.destroyAllWindows()


""" 
img = cv2.imread("../g1.jpeg"): "g1.jpeg" adlı bir resim dosyasını okur.

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY): Resmi gri tonlama dönüşümü yaparak gri tonlu bir görüntü elde eder.

blur = cv2.blur(gray,(3,3)): Gri tonlu görüntüyü bulanıklaştırarak görüntüyü yumuşatır.

ret , thresh = cv2.threshold(blur,150,255,cv2.THRESH_BINARY): Bulanıklaştırılmış görüntüyü ikili bir görüntüye dönüştürmek için eşik değeriyle işlem yapar.

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.

CHAIN_APPROX_SIMPLE): Eşiklenmiş görüntüdeki konturları ve hiyerarşiyi bulur.

hull = []: Boş bir liste oluşturur.

for i in range(len(contours)):: Konturların sayısı kadar döngü oluşturur.

hull.append(cv2.convexHull(contours[i],False)): Her kontur için dışbükey kabuğu hesaplar ve hull listesine ekler.

bg = np.zeros((thresh.shape[0],thresh.shape[1],3),np.uint8): İkili eşiklenmiş görüntüyle aynı boyutta siyah bir görüntü oluşturur.

for i in range(len(contours)):: Konturların sayısı kadar döngü oluşturur.

cv2.drawContours(bg,contours,i,(255,0,0),3,8,): Görüntü üzerine konturları çizer.

cv2.drawContours(bg,hull,i,(0,255,0),1,8): Görüntü üzerine dışbükey kabukları çizer.

cv2.imshow("original",img): Orjinal görüntüyü gösterir.
cv2.imshow("gray",gray): Gri tonlu görüntüyü gösterir.
cv2.imshow("blur",blur): Bulanıklaştırılmış görüntüyü gösterir.
cv2.imshow("thresh",thresh): Eşiklenmiş görüntüyü gösterir.
cv2.imshow("image-contour",bg): Konturları ve dışbükey kabukları çizilmiş görüntüyü gösterir.

cv2.waitKey(0): Kullanıcının bir tuşa basmasını bekler.
cv2.destroyAllWindows(): Tüm açık pencereleri kapatır.

Bu kod, bir resmin konturlarını bulanıklaştırma, ikili eşikleme, kontur çizme ve dışbükey kabukları çizme gibi temel görüntü işleme işlemlerini içerir. Bu tür işlemler, nesne tanıma, şekil analizi ve görüntü işleme uygulamalarında yaygın olarak kullanılır.

"""

""" 
Bu kodlar genel amacı olarak bir dış bükey kabuk oluşturur.

Dışbükey kabuklar, nesne tanıma, şekil analizi, nesne takibi ve görüntü işleme gibi birçok uygulamada önemli bir role sahiptir. İşte dışbükey kabukların önemi ve kullanım alanları:

Nesne Tanıma ve Sınıflandırma: Nesne tanıma sistemleri genellikle nesnelerin dış konturlarını ve şekillerini analiz eder. Dışbükey kabuklar, nesnelerin daha basit ve özetlenmiş bir temsilini sağlar ve nesne sınıflandırmasında kullanılabilir.

Nesne Takibi: Nesne takibi, bir nesnenin hareketini izlemeyi içerir. Dışbükey kabuklar, nesnenin sınırlarını ve şeklini temsil etmek için kullanılabilir, bu da takip algoritmaları için önemli bir veri kaynağı olabilir.

Görüntü İşleme ve Analiz: Görüntü işleme uygulamalarında, dışbükey kabuklar genellikle kontur analizi, nesne boyutu ve şekli hakkında bilgi elde etmek için kullanılır. Örneğin, nesnelerin boyutunu, alanını veya yüzeyini belirlemek için kullanılabilirler.

Robotik ve Otonom Sistemler: Robotik ve otonom sistemlerde, dışbükey kabuklar nesne algılama, haritalama ve navigasyon gibi işlevlerde kullanılabilir. Özellikle, robotik kollar veya manipülatörler tarafından nesnelerin ele alınması ve yerleştirilmesinde kullanışlı olabilirler.

Biometrik Tanıma: Yüz tanıma, parmak izi tanıma ve diğer biyometrik tanıma sistemlerinde, dışbükey kabuklar öznitelik çıkarma ve desen tanıma için kullanılabilir.

Bu kullanım alanlarına ek olarak, dışbükey kabuklar genellikle görüntü işleme ve bilgisayarlı görü alanlarında temel bir bileşen olarak kabul edilir. Görsel analiz ve bilgisayarlı görü alanındaki birçok algoritmanın temeli, nesnelerin konturları ve şekilleri üzerinde yapılan işlemlere dayanır. Bu nedenle, dışbükey kabuklar bu algoritmaların uygulanmasında önemli bir rol oynarlar.


"""