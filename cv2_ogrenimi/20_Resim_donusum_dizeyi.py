import cv2
import numpy as np

img = cv2.imread("../g1.jpeg",0)

row,col = img.shape

                                        # row, col = img.shape kodu, img adlı görüntünün satır (row) ve sütun (column) sayısını row ve col değişkenlerine atar. Bu kod, görüntünün boyutlarıyla ilgili bilgi almak için kullanılır. img.shape ifadesi, görüntünün boyutlarını (yükseklik, genişlik ve kanal sayısı) döndürür ve bu değerler row ve col değişkenlerine sırasıyla atanır. Bu bilgi, görüntü üzerinde işlemler yaparken boyutları kontrol etmek veya boyutlarla ilgili işlemler yapmak için kullanılır.




M = np.float32([[1, 0, 50], [0, 1, 70]])

                                        #Bu kod, bir dönüşüm matrisi oluşturur. Dönüşüm matrisi, görüntü üzerinde geometrik dönüşümler yapmak için kullanılır. np.float32([[1, 0, 50], [0, 1, 70]]) ifadesindeki değerler:

                                        # satır: [1, 0, 50]
                                        # satır: [0, 1, 70]

                                        # Bu değerler, x ve y koordinatları üzerinde bir kaydırma (translation) dönüşümünü temsil eder. Özellikle bu dönüşüm matrisi, x koordinatlarını 50 birim, y koordinatlarını ise 70 birim kaydırarak bir görüntüyü belirli bir yönde hareket ettirmek için kullanılabilir. Örneğin, bir görüntüyü sağa 50 birim, aşağıya 70 birim kaydırmak için bu dönüşüm matrisi kullanılabilir.

dst = cv2.warpAffine(img,M,(row,col))

                                        # Bu kod, bir görüntünün bir dönüşüm matrisine (M) göre döndürülmesini (warping) sağlar. cv2.warpAffine() işlevi, bir görüntüyü belirli bir dönüşüm matrisine göre döndürmek için kullanılır.

                                        # Parametreler şu şekildedir:

                                        # img: Döndürülecek olan görüntü.
                                        # M: Dönüşüm matrisi. Bu matris, görüntünün dönüşümünü tanımlar.
                                        # (row, col): Orijinal görüntünün satır ve sütun sayısı.
                                        # Örneğin, dst = cv2.warpAffine(img, M, (row, col)) ifadesi, img görüntüsünün M dönüşüm matrisine göre döndürülmüş halini dst değişkenine atar. Bu işlem genellikle görüntü düzenleme veya görüntü işleme uygulamalarında geometrik dönüşümler yapmak için kullanılır


cv2.imshow("dst",dst)

cv2.waitKey(0)

cv2.destroyAllWindows()