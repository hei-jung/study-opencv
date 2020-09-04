import cv2

cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()
    if ret:
        cv2.imshow('preview', frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
