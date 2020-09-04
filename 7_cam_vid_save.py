import cv2
cap = cv2.VideoCapture(0)
codec = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('a.avi', codec, 25.0, (640, 480))
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        out.write(frame)
        cv2.imshow('preview', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
