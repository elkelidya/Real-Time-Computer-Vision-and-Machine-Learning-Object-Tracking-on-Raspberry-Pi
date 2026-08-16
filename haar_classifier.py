import cv2

owl_cascade = cv2.CascadeClassifier('owl-cascade.xml')
face_cascade = cv2.CascadeClassifier('face-cascade.xml')

cv2.namedWindow('Video')

cap = cv2.VideoCapture(0)
cap.set(3, 720)
cap.set(4, 480)

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEI
GHT)))
out = cv2.VideoWriter("haarcascade.avi", fourcc, 20.0, size)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    owls = owl_cascade.detectMultiScale(gray)

    for (x,y,w,h) in owls:
        roi_gray = gray[y:y+h, x:x+w]
        faces = face_cascade.detectMultiScale(roi_gray)
        for (fx,fy,fw,fh) in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,0), 2)
            cx = x+(w/2)
            cy = y+(h/2)
            center = (cx,cy)
            cv2.putText(frame,"X",center, cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2)
            if cy<160:
                cv2.putText(frame, "forward", (20,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
            elif cy>320:
                cv2.putText(frame, "backward", (20,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
            elif cx<240:
                cv2.putText(frame, "turnleft", (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
            elif cx>480:
                cv2.putText(frame, "turnright", (20,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
            else:
                cv2.putText(frame, "stop", (20,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)

    out.write(frame)
    cv2.imshow('Video', frame)
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()