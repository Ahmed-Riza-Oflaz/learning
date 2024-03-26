import cv2
from cvzone.FaceMeshModule import FaceMeshDetector
import csv
from datetime import datetime
import winsound
import time

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = FaceMeshDetector(maxFaces=1)

breakcount_s, breakcount_y = 0, 0
counter_s, counter_y = 0, 0
state_s, state_y = False, False

def alert():
    cv2.rectangle(img, (700, 20), (1250, 80), (0, 0, 0), cv2.FILLED)
    cv2.putText(img, "DİKKAT!!!", (710, 60),
                cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2)
    color = (0, 0, 255)
    intensity = int(128 * (1 + 0.5 * (1 - abs(time.time() * 2 % 2 - 1))))  # Yanıp sönen efekti
    color = (intensity, 0, 0) 


    winsound.Beep(1000, 1000)

def recordData(condition):
    file = open("database.csv", "a", newline="")
    now = datetime.now()
    dtString = now.strftime("%d-%m-%Y %H:%M:%S")
    writer = csv.writer(file)
    writer.writerow([dtString, condition])
    file.close()

while True:
    success, img = cap.read()

    img = cv2.flip(img, 1)

    img, faces = detector.findFaceMesh(img, draw=False)

    if faces:
        face = faces[0]
        eyeLeft = [27, 23, 130, 243]
        eyeRight = [257, 253, 463, 359]
        mouth = [11, 16, 57, 287]
        faceId = [27, 23, 130, 243, 257, 253, 463, 359, 11, 16, 57, 287]


        eyeLeft_ver, _ = detector.findDistance(face[eyeLeft[0]], face[eyeLeft[1]])
        eyeLeft_hor, _ = detector.findDistance(face[eyeLeft[2]], face[eyeLeft[3]])
        eyeLeft_ratio = int((eyeLeft_ver/eyeLeft_hor)*100)

        eyeRight_ver, _ = detector.findDistance(face[eyeRight[0]], face[eyeRight[1]])
        eyeRight_hor, _ = detector.findDistance(face[eyeRight[2]], face[eyeRight[3]])
        eyeRight_ratio = int((eyeRight_ver / eyeRight_hor) * 100)

        mouth_ver, _ = detector.findDistance(face[mouth[0]], face[mouth[1]])
        mouth_hor, _ = detector.findDistance(face[mouth[2]], face[mouth[3]])
        mouth_ratio = int((mouth_ver / mouth_hor) * 100)


        cv2.rectangle(img, (30,20), (400,150), (255,255,255), cv2.FILLED)
        cv2.putText(img, f'Sol Goz Ratio: {eyeLeft_ratio}', (50, 60),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)
        cv2.putText(img, f'Sag Goz Ratio: {eyeRight_ratio}', (50, 100),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.putText(img, f'Agız Oranı: {mouth_ratio}', (50, 140),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)


        cv2.putText(img, f'UYUKLAMA: {counter_s}', (900, 140),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)
        cv2.putText(img, f'ESNEME: {counter_y}', (900, 180),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)


        #------------------------Eye-----------------------------
        if eyeLeft_ratio <= 50 and eyeRight_ratio <= 50:
            breakcount_s += 1
            if breakcount_s >= 30:
                alert()
                if state_s == False:
                    counter_s += 1
                    recordData("Sleep")
                    state_s = not state_s
        else:
            breakcount_s = 0
            if state_s:
                state_s = not state_s

        # ------------------------Mouth-----------------------------
        if mouth_ratio > 60:
            breakcount_y += 1
            if breakcount_y >= 30:
                alert()
                if state_y == False:
                    counter_y += 1
                    recordData("Yawn")
                    state_y = not state_y
        else:
            breakcount_y = 0
            if state_y:
                state_y = not state_y


        for id in faceId:
            cv2.circle(img,face[id], 5, (0,0,255), cv2.FILLED)


    cv2.imshow("Image", img)
    cv2.waitKey(1)
