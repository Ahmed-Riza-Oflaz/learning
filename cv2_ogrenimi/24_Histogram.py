import cv2
import numpy as np
from matplotlib import pyplot as plt

img = np.zeros((500,500), np.uint8) + 50


cv2.rectangle(img,(250,170),(350,200,),(255,255,255),-1)



cv2.imshow("mg",img)

plt.hist(img.ravel(),256,[0,256])
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()

""" 

Bu kod örneği, siyah bir arka plan üzerine beyaz bir dikdörtgen çizen ve ardından bu görüntünün histogramını çizen bir çalışmadır. İşlevleri şu şekildedir:

img = np.zeros((500,500), np.uint8) + 50: 500x500 boyutlarında ve tek kanallı (siyah-beyaz) bir görüntü oluşturur. Bu görüntünün tüm piksel değerlerini 50 olarak ayarlar, böylece bir gri arka plan elde edilir.

cv2.rectangle(img,(250,170),(350,200,),(255,255,255),-1): Oluşturulan gri arka plan üzerine (250, 170) ve (350, 200) koordinatları arasında beyaz renkte (-1) bir dikdörtgen çizer.

plt.hist(img.ravel(),256,[0,256]): Oluşturulan görüntünün histogramını hesaplar ve çizer. ravel() fonksiyonu, görüntünün piksel değerlerini tek boyutlu bir diziye dönüştürür. Histogram, 0 ile 255 arasındaki piksel değerlerini 256 parçaya böler ve bu değerlerin görüntüdeki dağılımını gösterir.

plt.show(): Oluşturulan histogramı görsel olarak ekranda görüntüler.

cv2.imshow("mg",img): Oluşturulan görüntüyü ekranda gösterir.

Bu kod örneği, bir dikdörtgen şeklinde beyaz bir bölge oluşturarak bu bölgenin piksel değerlerinin histogramını çıkarır. Bu şekilde, bir görüntünün belirli bir bölgesinin piksel değerlerini analiz etmek için kullanılabilir.

"""