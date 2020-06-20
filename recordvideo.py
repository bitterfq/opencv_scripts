import numpy as np 
import cv2

filename = 'video.avi' #.avi -- encoded file type for vidoes / .mp4 is another example
frames_per_second = 24 # typical movie frames
def_res = '720p' # lower the size of big file (1080p)

def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)

STD_DIMENSIONS = {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160)
}

# grab resolution dimesions and set video capture to it
def get_dims(cap, res='1080p'):
    width, height = STD_DIMENSIONS["480p"]

    if res in STD_DIMENSIONS:
        width,height = STD_DIMENSIONS[res]

    ## change the current capture device 
    ## to the resulting resolution 
    change_res(cap, width, height)
    return width, height

##ffmpeg - for audio file
cap = cv2.VideoCapture(0) #Single capture device 
dims = get_dims(cap, res=def_res)

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
