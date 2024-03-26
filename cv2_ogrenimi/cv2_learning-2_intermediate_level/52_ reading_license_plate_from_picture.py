import cv2
import numpy as np
import pytesseract
import imutils

#---görselden plaka okumak--#



img = cv2.imread("license-plate.png")


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

filtered = cv2.bilateralFilter(gray,6,250,250)

edged = cv2.Canny(filtered,30,200)

edged_gray = cv2.Canny(gray,30,250)

contours = cv2.findContours(edged,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cont = imutils.grab_contours(contours)

cont = sorted(cont,key=cv2.contourArea,reverse=True)[:10]

screen = None

for c in cont:
    epsilon = 0.018*cv2.arcLength(c,True)
    approx =cv2.approxPolyDP(c,epsilon,True)

    if len(approx) == 4:
        screen = approx
        break

mask = np.zeros(gray.shape,np.uint8)

new_image = cv2.drawContours(mask,[screen],0,(255,255,255),-1)

new_image = cv2.bitwise_and(img,img,mask=mask)

(x,y) = np.where(mask == (255))

(topx,topy) = (np.min(x),np.min(y))

(bottomx,bottomy) = (np.max(x),np.max(y))

cropped = gray[topx:bottomx + 1,topy:bottomy + 1]

# # # text = pytesseract.image_to_string(cropped,lang="eng")

# # # print("dedect",text)

# cv2.imshow("license plate", img )
# cv2.imshow("licanse plate gray", gray )
# cv2.imshow("licanse plate filtered",filtered)
# cv2.imshow("licanse plate edged",edged_gray)

cv2.imshow("licanse plate edged",edged)
cv2.imshow("license plate end",new_image)
cv2.imshow("licanse plate cropt",cropped)


cv2.waitKey(0)
cv2.destroyAllWindows()

""" 
Bu kodlar, bir araba plakasından metin okuma işlemi gerçekleştirir. Kod adım adım şu işlemleri yapar:

cv2.imread("license-plate.png"): "license-plate.png" adlı görüntü dosyasını okur ve img değişkenine yükler.

cv2.cvtColor(img,cv2.COLOR_BGR2GRAY): Renkli görüntüyü gri tonlamalı görüntüye dönüştürür ve gray adlı değişkene kaydeder.

cv2.bilateralFilter(gray,6,250,250): Gri tonlamalı görüntüyü bilateral filtre ile işler ve filtrelenmiş görüntüyü filtered adlı değişkene kaydeder.

cv2.Canny(filtered,30,200): Filtrelenmiş görüntü üzerinde kenar tespiti yapar ve kenar görüntüsünü edged adlı değişkene kaydeder.

cv2.Canny(gray,30,250): Gri tonlamalı görüntü üzerinde ayrıca kenar tespiti yapar ve kenar görüntüsünü edged_gray adlı değişkene kaydeder.

cv2.findContours(edged,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE): Kenar görüntüsündeki konturları bulur.

imutils.grab_contours(contours): Konturları yakalar ve cont değişkenine kaydeder.

sorted(cont,key=cv2.contourArea,reverse=True)[:10]: Konturları alanlarına göre sıralar ve en büyük 10 konturu seçer.

Eğer seçilen kontur dört köşeli ise (len(approx) == 4), bu konturu plaka olarak kabul eder.

Plaka alanını maskeleme işlemi yapar.

Plaka alanını görüntüden çıkarır ve sadece plaka alanını içeren bir görüntü oluşturur.

Oluşturulan plaka görüntüsünden metin okuma işlemi yapar (pytesseract.image_to_string(cropped,lang="eng")) ve okunan metni ekrana yazdırır.

Bu kodlar, görüntü işleme ve metin tanıma (OCR) tekniklerini kullanarak bir araba plakasından metin okuma işlemini gerçekleştirir.

"""