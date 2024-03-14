import cv2
import numpy as np 

#################################-----sayfa oluşturarak çizim yapmak------#############################


img = np.zeros((10,10,3), np.uint8) 

    #np.zeros: NumPy kütüphanesinde bulunan bir fonksiyondur ve belirtilen boyutta, tüm elemanları sıfır olan bir dizi oluşturur.

    #(10, 10, 3): Oluşturulan dizinin şeklini belirtir. Bu durumda, 10x10 piksel boyutunda ve üç kanala (RGB) sahip bir görüntü oluşturulacaktır.

    #np.uint8: Oluşturulan dizinin veri tipini belirtir. 8-bitlik işaretsiz tamsayılar kullanıldığından, her bir kanal için piksel değerleri 0 ile 255 arasında olacaktır.


img[0,0] = (255,255,255) #Bu kod, oluşturulan siyah görüntünün sol üst köşesindeki pikselin rengini beyaza ((255,255,255)) ayarlar.
img[0,1] = (255,255,200) #img: Oluşturulan siyah görüntüyü temsil eden bir NumPy dizisidir.
img[0,2] = (255,255,150) #[0, 2]: Görüntünün piksel konumunu belirtir.
img[0,3] = (255,255,100) #(255, 255, 255): Belirtilen pikselin rengini beyaz olarak ayarlar. Renk kodları, RGB (Red, Green, Blue).
img[0,4] = (255,255,50)  


img[5,5] = (255,255,255) #sayfanın ortasına pixellik beyazlık oluşturur.




img = cv2.resize(img, ( 500,500), interpolation=cv2.INTER_AREA )

    #cv2.resize(): OpenCV kütüphanesinde bulunan bir fonksiyondur ve bir görüntüyü yeniden boyutlandırır.

    #(500, 500): Yeniden boyutlandırılan görüntünün hedef genişlik ve yüksekliğini belirtir.

    #interpolation=cv2.INTER_AREA: Yeniden boyutlandırma işlemi sırasında kullanılacak interpolasyon yöntemini belirtir. cv2.INTER_AREA, yeniden boyutlandırma işlemi sırasında alan arama yöntemini kullanır, yani bir pikselin değeri hesaplanırken komşu piksellerin ortalaması alınır.




cv2.imshow("canvas resize", img)

cv2.waitKey(0)

cv2.destroyAllWindows()
