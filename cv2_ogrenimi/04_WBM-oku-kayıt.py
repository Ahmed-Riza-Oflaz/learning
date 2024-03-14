import cv2

cap = cv2.VideoCapture(0)

fileName = "C:\Webcam.avi"

codec = cv2.VideoWriter_fourcc('W','M','V', '2') #videoyu sıkıştırmak için

framRate = 30 #kalite/kare

resulation = (640,480) #boyut

videoFileOutput = cv2.VideoWriter(fileName, codec , framRate, resulation)
#video_writer = cv2.VideoWriter('output_video.wmv', codec, 30, (640, 480)) olabilirdi


while True:

    ret, frame = cap.read() #frame okunan kareyi temsil eder / ret okunduysa True dödürür

    frame = cv2.flip(frame, 1) #yatayda aynalayarak görüntü sağlar

    videoFileOutput.write(frame)

    cv2.imshow("Webcam", frame)
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord("q"): # "q" basıldığında bitir
        break

cap.release() # serbest bırak video bağlantısını
cv2.destroyAllWindows()