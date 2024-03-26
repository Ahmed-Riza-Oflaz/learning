import cv2

img = cv2.VideoCapture(0)

while True:
    ret, frame = img.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret, thres = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        cv2.drawContours(frame, contours, -1, (0, 0, 255), 3)

    cv2.imshow("images", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

img.release()
cv2.destroyAllWindows()
