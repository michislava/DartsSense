import cv2
import urllib.request
import numpy as np

# Replace the URL with the IP camera's stream URL
url = 'http://192.168.1.20/getFrames.jpg'
cv2.namedWindow("DartsSense Preview", cv2.WINDOW_AUTOSIZE)


# Create a VideoCapture object
cap = cv2.VideoCapture(url)

# Check if the IP camera stream is opened successfully
if not cap.isOpened():
    print("Failed to open the IP camera stream")
    exit()

# Read and display video frames
while True:
    # Read a frame from the video stream
    img_resp=urllib.request.urlopen(url)
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    #ret, frame = cap.read()
    im = cv2.imdecode(imgnp,-1)

    cv2.imshow('DartsSense Preview',im)
    key=cv2.waitKey(5)
    if key==ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()