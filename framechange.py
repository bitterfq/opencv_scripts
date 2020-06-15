# showcasing opencv resolution scaling, for faster processing on rpi for example to not overload 
# 1080p needs to be scaled down to 480p for low file size and reduce load

import numpy as np 
import cv2

cap = cv2.VideoCapture(0) #Single capture device 

# change resoulution method
def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)

def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)

def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)

# returns resized frame
def rescale_frame(frame, percent = 75):
    width = int(frame.shape[1] * percent / 100)
    height = int(frame.shape[0] * percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim , interpolation=cv2.INTER_AREA)

while True:  # Continous reading of video
    ret, frame = cap.read()
    frame = rescale_frame(frame, percent=30)

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

