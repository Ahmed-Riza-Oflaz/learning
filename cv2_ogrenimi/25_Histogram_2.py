import cv2
import numpy as np
from matplotlib import pylab as plt


img = cv2.imread("../g1.jpeg")

b,g,r = cv2.split(img)




cv2.imshow("mg",img)

plt.hist(img.ravel(),256,[0,256])
plt.show()


cv2.imshow("img",img)

cv2.waitKey(0)

cv2.destroyAllWindows()


""" 
Bu kod örneği, bir görüntünün renk kanallarını (mavi, yeşil, kırmızı) ayırarak her bir kanalın histogramını çıkarmak için kullanılır. İşlevleri şu şekildedir:

img = cv2.imread("../g1.jpeg"): Belirtilen dosya yolundan bir görüntüyü yükler.

b,g,r = cv2.split(img): Görüntünün mavi (blue), yeşil (green) ve kırmızı (red) renk kanallarını ayrı ayrı alır.

plt.hist(img.ravel(),256,[0,256]): Görüntünün piksel değerlerinin histogramını çıkarır ve çizer. 

ravel() fonksiyonu, görüntünün piksel değerlerini tek boyutlu bir diziye dönüştürür. Histogram, 0 ile 255 arasındaki piksel değerlerini 256 parçaya böler ve bu değerlerin görüntüdeki dağılımını gösterir.

plt.show(): Oluşturulan histogramı görsel olarak ekranda gösterir.

cv2.imshow("mg",img): Görüntüyü ekranda gösterir.

cv2.waitKey(0): Bir tuşa basılmasını bekler (0 ms süreyle, sonsuza kadar). Bu, bir tuşa basılana kadar pencerenin açık kalmasını sağlar.

cv2.destroyAllWindows(): Tüm açık penceleri kapatır ve programı sonlandırır.

Bu kod örneği, bir görüntünün her bir renk kanalının histogramını çıkarmak ve görselleştirmek için kullanılır. Bu, görüntüdeki renk dağılımını analiz etmek ve renk kanallarının hangi aralıklarda yoğun olduğunu görmek için yararlıdır.

"""