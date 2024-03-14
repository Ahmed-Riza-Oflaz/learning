import cv2


#webcam üzerinden aldığı görüntüyü yansıtır


cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read() #frame okunan kareyi temsil eder / ret okunduysa True dödürür

    frame = cv2.flip(frame, 1) #yatayda aynalayarak görüntü sağlar

    cv2.imshow("Webcam", frame)
    cv2.waitKey(1) #okunan video kare hızı/kalite

    if cv2.waitKey(1) & 0xFF == ord("q"): # "q" basıldığında bitir
        break






cap.release() # serbest bırak video bağlantısını
cv2.destroyAllWindows()