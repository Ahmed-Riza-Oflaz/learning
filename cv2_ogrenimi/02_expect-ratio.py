import cv2

# resimleri yeniden boyutlandırmak**********************************

def resizewithApectRatio(img, width = None, height = None, inter = cv2.INTER_AREA):

    
    dimension = None

    (h,w) = img.shape[:2]

    if width is None and height is None:
        return img
            #Bu satır, eğer herhangi bir genişlik veya yükseklik belirtilmemişse, yani width ve height parametreleri None ise, orijinal görüntünün aynen döndürülmesini sağlar. Bu durumda, herhangi bir yeniden boyutlandırma işlemi yapılmasına gerek olmadığı anlamına gelir ve fonksiyon sadece orijinal görüntüyü geri döndürür. Bu, fonksiyonun esnekliğini artırır ve genişlik veya yükseklik belirtilmediğinde özel bir işlem yapılmasını sağlar.

    if width is None:
        r = height / float(h)
        dimension = (int(w*r), height)
            #Bu satır, eğer sadece genişlik (width) belirtilmemişse ve yükseklik (height) belirtilmişse, görüntünün boyutunu koruyarak belirtilen yükseklikte yeniden boyutlandırma işlemini gerçekleştirir.


    else:
        r = width / float(w)
        dimension = (width, int(h*r))
            #Bu satır, eğer sadece genişlik (width) belirtilmişse ve yükseklik (height) belirtilmemişse, görüntünün boyutunu koruyarak belirtilen genişlikte yeniden boyutlandırma işlemini gerçekleştirir.

    return cv2.resize(img, dimension, interpolation=inter)



img = cv2.imread("../g1.jpeg")

img1 = resizewithApectRatio(img, width = None, height = 600, inter = cv2.INTER_AREA)


cv2.imshow("Original",img)

cv2.imshow("Resized",img1)

cv2.waitKey(0) #tuşa basılıncaya kadar açık tut


cv2.destroyAllWindows() #tüm açık pencereleri sorunsuz kapat