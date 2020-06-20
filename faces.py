#Cascading is a particular case of ensemble 
#learning based on the concatenation of several classifiers

import numpy as np 
import cv2

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')

recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.read("trainner.yml") # read trained model from faces-train.py --atribute error

cap = cv2.VideoCapture(0) #Single capture device 

while True:  # Continous reading of video
    ret, frame = cap.read()
    #using face_cascade

    # first convert rgb to gray -- due to this face_cascade
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors=5)
    
    for (x,y,w,h) in faces:
        print(x,y,w,h) # prints region of interest (roi), detects face is showing up in frame
        roi_gray = gray[y:y+h, x:x+w] #gather the pixels only in the roi
        roi_color = frame[y:y+h, x:x+h]

        # recognize roi - deep learned model to predict -- tensorflow, pytorch, scikit-learn
        id_, conf = recognizer.predict(roi_gray) # predict on region of interest, id_ and confidence
        if conf>=45 and conf <= 85:
            print(id_)

        img = "roi_image.png"
        img2 = "roi_color_image.png"
        cv2.imwrite(img, roi_gray)
        cv2.imwrite(img2, roi_color)

        #drawing a rectangle around roi
        color = (255, 0, 0) #BGR 0-255
        stroke = 2 # thickness of line
        cv2.rectangle(frame, (x,y), (x+w, y+h), color, stroke) ## rectange(frame, start x&y coord, end x&y coord)
                                                ## rectangle around the roi basically


    cv2.imshow('frame', frame) #imgshow doesn't work
    cv2.waitKey(1) # linux constant video frame works with waitKey(1)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

#When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
