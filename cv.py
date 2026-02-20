
import cv2

cam1 = cv2.VideoCapture("http://192.168.137.115:8080/video")
cam2 = cv2.VideoCapture("http://192.168.137.95:8080/video")

while True:
    ret1, frame1 = cam1.read()
    ret2, frame2 = cam2.read()

    if not ret1 or not ret2:
        print("Camera not reading properly")
        break

    # Resize both to same size
    frame1 = cv2.resize(frame1, (640, 480))
    frame2 = cv2.resize(frame2, (640, 480))

    combined = cv2.hconcat([frame1, frame2])

    cv2.imshow("Blind Corner Monitor", combined)

    if cv2.waitKey(1) == 27:
        break

cam1.release()
cam2.release()
cv2.destroyAllWindows()
