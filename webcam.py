import numpy as np 
import cv2

cap = cv2.VideoCapture(0) #Single capture device 

while True:  # Continous reading of video
    ret, frame = cap.read()
    
    #change video rgb to gray
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    #cv2.imshow('gray', gray)

    cv2.imshow('frame', frame) #imgshow doesn't work
    cv2.waitKey(1) # linux constant video frame works with waitKey(1)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

#When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
