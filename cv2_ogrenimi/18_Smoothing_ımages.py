import cv2
import numpy as np


img_filter = cv2.imread("./images.jpeg")

blur  = cv2.blur(img_filter,(10,5),cv2.BORDER_DEFAULT)

blur2 = cv2.medianBlur(img_filter,(5),cv2.BORDER_DEFAULT)

cv2.imshow("blur-2",blur2)

cv2.imshow("original",img_filter)

cv2.imshow("blur",blur)

cv2.waitKey(0)

cv2.destroyAllWindows()


""" 
Bu kod parçası, OpenCV kütüphanesini kullanarak bir görüntüyü farklı bulanıklık (blurring) teknikleriyle işleyen basit bir örnek içeriyor. İşlenen görüntülerin ekranda gösterilmesi için OpenCV'nin imshow ve waitKey fonksiyonları kullanılmıştır. İşte kodun bir açıklaması:

cv2.imread("./images.jpeg"): "./images.jpeg" adlı bir görüntüyü okur ve img_filter adlı değişkene atar.

cv2.blur(img_filter,(10,5),cv2.BORDER_DEFAULT): img_filter görüntüsünü 10x5 boyutunda bir bulanıklık uygular. cv2.BORDER_DEFAULT parametresi, piksel değerlerinin dışında kalan kenar pikselleri için varsayılan kenar tipini kullanır.

cv2.medianBlur(img_filter,(5),cv2.BORDER_DEFAULT): img_filter görüntüsüne median filtre uygular. Median filtre, piksel değerlerini belirli bir çekirdek boyutu içindeki piksellerin ortancasını kullanarak düzenler.

cv2.imshow("blur-2",blur2): Median filtre uygulanmış görüntüyü gösterir.

cv2.imshow("original",img_filter): Orjinal görüntüyü gösterir.

cv2.imshow("blur",blur): Bulanıklaştırılmış görüntüyü gösterir.

cv2.waitKey(0): Bir tuşa basılmasını bekler (0, yani sonsuz bir süre bekler) ve ardından devam eder.

cv2.destroyAllWindows(): Tüm pencere ve kaynakları serbest bırakır, işlem sona erer.

Bu kod örneği, görüntü işleme alanında farklı filtreleme tekniklerini anlamak için basit bir başlangıç noktası olabilir.

"""