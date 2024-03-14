import cv2
import numpy as np 

#################################-----sayfa oluşturarak çizim yapmak------#############################


img = np.zeros((10,10), np.uint8 ) 

    #np.zeros: NumPy kütüphanesinde bulunan bir fonksiyondur ve belirtilen boyutta, tüm elemanları sıfır olan bir dizi oluşturur.

    #np.uint8: Oluşturulan dizinin veri tipini belirtir. 8-bitlik işaretsiz tamsayılar kullanıldığından, her bir kanal için piksel değerleri 0 ile 255 arasında olacaktır.


img[0,0] = 255
img[0,1] = 250
img[0,2] = 200
img[0,3] = 150
img[0,4] = 100


img = cv2.resize(img, ( 500,500), interpolation=cv2.INTER_AREA )

    #cv2.resize(): OpenCV kütüphanesinde bulunan bir fonksiyondur ve bir görüntüyü yeniden boyutlandırır.

    #(500, 500): Yeniden boyutlandırılan görüntünün hedef genişlik ve yüksekliğini belirtir.

    #interpolation=cv2.INTER_AREA: Yeniden boyutlandırma işlemi sırasında kullanılacak interpolasyon yöntemini belirtir. cv2.INTER_AREA, yeniden boyutlandırma işlemi sırasında alan arama yöntemini kullanır, yani bir pikselin değeri hesaplanırken komşu piksellerin ortalaması alınır.



cv2.imshow("canvas resize", img)

cv2.waitKey(0)

cv2.destroyAllWindows()
