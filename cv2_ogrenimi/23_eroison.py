import cv2
import numpy as np

#Bu kod, morfolojik işlemleri uygulamak için OpenCV'yi kullanır. Morfolojik işlemler, görüntüdeki şekil ve yapıları değiştirmek için kullanılır.


img = cv2.imread("../g1.jpeg")


kernel = np.ones((10,1),np.uint8)

eroison = cv2.erode(img,kernel,iterations=5)

dilation = cv2.dilate(img,kernel,iterations=5)

opening = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)





cv2.imshow("ereison",eroison)
cv2.imshow("original",img)
cv2.imshow("dilation",dilation)
cv2.imshow("opening",opening)

cv2.waitKey(0)
cv2.destroyAllWindows()


""" 
cv2.erode: İkinci argüman olarak belirtilen kernel ile erozyon işlemi uygular. Erozyon işlemi, nesnelerin kenarlarını aşındırarak küçültür.

cv2.dilate: İkinci argüman olarak belirtilen kernel ile genişletme işlemi uygular. Genişletme işlemi, nesnelerin kenarlarını genişleterek büyütür.

cv2.morphologyEx: İkinci argüman olarak belirtilen morfolojik işlemi (bu örnekte MORPH_CLOSE) uygular. MORPH_CLOSE, ilk olarak erozyon işlemi uygulayıp ardından genişletme işlemi uygular. Bu işlem genellikle nesnelerin kenarlarını yumuşatır ve delikleri doldurur.

"""