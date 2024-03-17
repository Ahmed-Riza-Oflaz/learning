import cv2


cap = cv2.VideoCapture(0)

while True:

    ret , frame = cap.read()

    frame = cv2.flip(frame,1)

    edges = cv2.Canny(frame,100,200)

    cv2.imshow("Frame",frame)
    cv2.imshow("Edges",edges)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

""" 
cv2.VideoCapture(0) ile kameradan görüntü alınır.

cap.read() ile kameradan bir kare alınır ve ret ve frame değişkenlerine atanır.

cv2.flip(frame,1) ile alınan kare yatay olarak çevrilir.

cv2.Canny(frame,100,200) ile kenar dedektörü uygulanır ve kenarları içeren bir görüntü elde edilir.

cv2.imshow("Frame",frame) ve cv2.imshow("Edges",edges) ile orijinal ve kenarlar görüntüleri ekranda gösterilir.

cv2.waitKey(5) & 0xFF == ord("q") ile kullanıcı "q" tuşuna basarsa döngü sonlandırılır.

cap.release() ile kamera kaynağı serbest bırakılır.

cv2.destroyAllWindows() ile tüm pencereler kapatılır.

"""