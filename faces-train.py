import numpy as np
import os 
from PIL import Image
import cv2
import pickle # use to save label IDs

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')

# Open-cv face-recognizer

recognizer = cv2.face.createLBPHFaceRecognizer()


base_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(base_dir, "images")

current_id = 0
label_ids = {}
y_labels = []
x_train = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            #giving labels
            label = os.path.basename(os.path.dirname(path)).replace(" ", "-").lower()

            # if person not in label_id, add them using current_id and update
            if not label in label_ids:
                label_ids[label] = current_id
                current_id += 1

            id_ = label_ids[label]
            #print(label_ids)
            #y_labels.append(label) # number value to label
            #x_train.append(path) # verify this image, turn into NUMPY array, GRAY
            pil_image = Image.open(path).convert("L") # grayscale
            image_array = np.array(pil_image, "uint8")
            #print(image_array)
            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

            for (x,y,w,h) in faces:
                roi = image_array[y:y+h, x:x+h]
                x_train.append(roi)
                y_labels.append(id_)

with open("labels.pickle", 'wb') as f:
    pickle.dump(label_ids, f) # dump in label ids to file --what the labels actually are

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainner.yml")