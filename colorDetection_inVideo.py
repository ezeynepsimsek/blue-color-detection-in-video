import cv2
import numpy as np

vid = cv2.VideoCapture("C:\\Users\\Zeynep\\Downloads\\dalgaVideo.mp4")

while 1 :
    _,frame = vid.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_blue = np.array([10,50,50])
    upper_blue = np.array([130,255,255])

    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    cv2.imshow("Frame",frame)
    cv2.imshow("MASK",mask)

    if cv2.waitKey(20) & 0xFF == ord("q"):
       break

vid.release()
cv2.destroyAllWindows()
