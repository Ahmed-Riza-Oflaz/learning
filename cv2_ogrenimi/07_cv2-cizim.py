import cv2
import numpy as np  


##########################------cv2-solid----------#################3

canvas = np.zeros((512,512,3), dtype=np.uint8) + 255

#np.zeros fonksiyonu, belirtilen boyutlarda tüm elemanları sıfır olan bir dizi oluşturur.255 eklenerek beyaz bir canvas elde edilir.

#np.zeros((512,512,3), dtype=np.uint8): 512x512 piksel boyutunda, üç kanallı (RGB) bir siyah canvas oluşturur. dtype=np.uint8 ifadesi, veri tipinin 8-bitlik işaretsiz tamsayılar olduğunu belirtir.

#+ 255: Oluşturulan siyah canvas'ın tüm piksel değerlerine 255 ekler. Bu işlem, her bir kanal için maksimum değer olan 255'i ekleyerek tüm pikselleri beyaza dönüştürür.


print(canvas)


cv2.imshow("canvas", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()


#sonuç olarak bu kod bir canvas (çizim tahtası oluşturur.)