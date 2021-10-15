import cv2


#cap = cv2.VideoCapture(-1)
cap = cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FPS, 60)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
while True:
    ret, img = cap.read()
    cv2.imshow("camera", img)
    if cv2.waitKey(10) == 27:
        break
    
cap.release()
cv2.destroyAllWindows()