import cv2

img = cv2.imread("./images.jpeg")

##Bu kod, bir resmi farklı renk uzaylarına dönüştürmek ve bu dönüşümleri görselleştirmek için kullanılır.

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                    #cv2.cvtColor(img, cv2.COLOR_BGR2RGB): img adlı resmi BGR (Mavi, Yeşil, Kırmızı) renk uzayından RGB (Kırmızı, Yeşil, Mavi) renk uzayına dönüştürür ve img_rgb adlı değişkene atar.


img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

                    #cv2.cvtColor(img, cv2.COLOR_BGR2HSV): img adlı resmi BGR renk uzayından HSV (Ton, Doyma, Parlaklık) renk uzayına dönüştürür ve img_hsv adlı değişkene atar.

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                    #cv2.cvtColor(img, cv2.COLOR_BGR2GRAY): img adlı resmi BGR renk uzayından Gri tonlamalı (siyah beyaz) renk uzayına dönüştürür ve img_gray adlı değişkene atar.



cv2.imshow("g1", img)


cv2.imshow("g1-2", img_rgb)
cv2.imshow("g1-3", img_hsv)
cv2.imshow("g1-4", img_gray)


cv2.waitKey(0)

cv2.destroyAllWindows()