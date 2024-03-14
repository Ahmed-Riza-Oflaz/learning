import cv2



cv2.namedWindow("image",  cv2.WINDOW_NORMAL) #normal olarak aç büyük küçük

img = cv2.imread("../g1.jpeg",0) #sıfır; gri tonlama yapar ve imread okur

img= cv2.resize(img, (640,480)) #resmin görmek istediğim boyutları


# print(img)


cv2.imshow("Image", img )
cv2.imwrite("../g1.jpeg", img)

cv2.waitKey(0) #ekrana yazdır

cv2.destroyAllWindows() #hatasız kapat