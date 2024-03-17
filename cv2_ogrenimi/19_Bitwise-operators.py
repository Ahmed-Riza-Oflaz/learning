import cv2
import numpy as np

# Görüntülerin dosya yolları
img1_path = "../g1.jpeg"
img2_path = "./images.jpeg"

# Görüntüleri yükle
img1 = cv2.imread(img1_path)
img2 = cv2.imread(img2_path)

# Görüntüleri aynı boyuta getir
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

                                        # Bu kod satırı, img2 adlı görüntünün boyutunu img1 görüntüsünün boyutuyla aynı hale getirir. Yani, img1 ve img2 aynı boyuta sahip olur. Bu, görüntüler arasında bitwise operatörlerini kullanırken boyut uyumluluğunu sağlamak için gereklidir. Bitwise operatörleri, aynı boyutta olan iki görüntüyü kullanarak piksel bazında mantıksal operasyonlar yapar. Bu nedenle, görüntülerin boyutlarının aynı olması gereklidir.

                                        # Özetle, img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0])) kod satırı, img2 görüntüsünün boyutunu img1 görüntüsünün boyutuyla aynı hale getirerek, bitwise operatörlerini doğru şekilde kullanmak için boyut uyumluluğunu sağlar.

# Bitwise AND
bit_And = cv2.bitwise_and(img2, img1)

                                        # Bu kod, img2 ve img1 adlı iki görüntü arasında bitwise AND işlemi yapar. Bitwise AND işlemi, her iki pikselin de değerleri 0-255 arasında olduğunda sonuçta o pikselin değeri korunur, değerlerden biri veya her ikisi de 0 ise sonuç 0 olur.

                                        # Yani, bit_And = cv2.bitwise_and(img2, img1) kodu img2 ve img1 görüntülerinin her bir pikselini karşılaştırır ve her iki görüntüde de piksel değerleri 0-255 arasında ise yeni görüntüde bu pikselin değeri korunur, değerlerden biri veya her ikisi de 0 ise yeni görüntüde bu pikselin değeri 0 olur. Bu işlem genellikle görüntü işleme ve analizinde kullanılan bir işlemdir.

# Bitwise OR
bit_or = cv2.bitwise_or(img2, img1)


                                        # Bu kod, img2 ve img1 adlı iki görüntü arasında bitwise OR (veya) işlemi yapar. Bitwise OR işlemi, her iki pikselin de değeri 0-255 arasında olduğunda sonuçta o pikselin değeri korunur, değerlerden herhangi biri veya her ikisi de 255 ise sonuç 255 olur.

                                        # Yani, bit_or = cv2.bitwise_or(img2, img1) kodu img2 ve img1 görüntülerinin her bir pikselini karşılaştırır ve her iki görüntüde de piksel değerleri 0-255 arasında ise yeni görüntüde bu pikselin değeri korunur, değerlerden biri veya her ikisi de 255 ise yeni görüntüde bu pikselin değeri 255 olur. Bu işlem genellikle görüntü işleme ve analizinde kullanılan bir işlemdir.

# Bitwise XOR
bit_xor = cv2.bitwise_xor(img2, img1)


                                        # bit_xor = cv2.bitwise_xor(img2, img1) kodu, img2 ve img1 adlı iki görüntü arasında bitwise XOR (exclusive OR) işlemi yapar. Bitwise XOR işlemi, her iki pikselin de değeri 0-255 arasında olduğunda sonuçta o pikselin değeri 0 olur, değerlerden biri veya her ikisi de 255 ise sonuç 0 olur. Yalnızca bir pikselin değeri 255 iken diğerinin değeri 0 ise sonuç 255 olur.

                                        # Yani, bu işlem img2 ve img1 görüntülerinin her bir pikselini karşılaştırır ve her iki görüntüde de piksel değerleri 0-255 arasında ise yeni görüntüde bu pikselin değeri 0 olur, değerlerden biri veya her ikisi de 255 ise yeni görüntüde bu pikselin değeri 0 olur. Bu işlem genellikle görüntü işleme ve analizinde kullanılan bir işlemdir.

# Bitwise NOT
bit_not = cv2.bitwise_not(img1)

                                        # bit_not = cv2.bitwise_not(img1) kodu, img1 adlı görüntünün her pikselinin bitwise NOT (tersini alma) işlemini yapar. Bitwise NOT işlemi, her pikselin değerini tersine çevirir. Yani, 0 olan piksel değerleri 255'e, 255 olan piksel değerleri ise 0'a dönüştürülür. Bu işlem genellikle görüntü işleme uygulamalarında, görüntünün negatifini almak veya bazı özel efektler oluşturmak için kullanılır.


bit_not2 = cv2.bitwise_not(img2)


                                        # bit_not2 = cv2.bitwise_not(img2) kodu, img2 adlı görüntünün her pikselinin bitwise NOT (tersini alma) işlemini yapar. Bitwise NOT işlemi, her pikselin değerini tersine çevirir. Yani, 0 olan piksel değerleri 255'e, 255 olan piksel değerleri ise 0'a dönüştürülür. Bu işlem genellikle görüntü işleme uygulamalarında, görüntünün negatifini almak veya bazı özel efektler oluşturmak için kullanılır.

# Sonuçları göster
cv2.imshow("Bitwise AND", bit_And)
cv2.imshow("Bitwise OR", bit_or)
cv2.imshow("Bitwise XOR", bit_xor)
cv2.imshow("Bitwise NOT - img1", bit_not)
cv2.imshow("Bitwise NOT - img2", bit_not2)
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()