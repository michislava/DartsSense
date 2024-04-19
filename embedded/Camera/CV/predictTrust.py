from ultralytics import YOLO
import cv2
import math
import numpy as np
import requests
import json

device = "1"
score = 24

# Sample score data
score_data = {
    "deviceID": device,
    "score": score
}

# Load YOLO model
model = YOLO('C:/Users/victo/Desktop/Github REPOS/DartsSense/embedded/Camera/CV/runs/detect/train19/weights/best.pt')

# Define class names
classNames = ["cal1", "cal2", "cal3", "cal4", "center", "tip"]

# Define dartboard colors
dartboard_colors = {
    'red': {'lower': np.array([0, 70, 50]), 'upper': np.array([10, 255, 255]), 'color': (0, 0, 255)},
    'white': {'lower': np.array([0, 0, 100]), 'upper': np.array([180, 50, 255]), 'color': (255, 255, 255)},
    'green': {'lower': np.array([40, 70, 50]), 'upper': np.array([80, 255, 255]), 'color': (0, 255, 0)},
    'black': {'lower': np.array([0, 0, 0]), 'upper': np.array([180, 255, 50]), 'color': (0, 0, 0)}
}

# Function to preprocess frame
def preprocess_frame(frame):
    # Apply Gaussian blur
    blur = cv2.GaussianBlur(frame, (7, 7), cv2.BORDER_DEFAULT)
    # Convert frame to HSV color space
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    return hsv

# Function to detect individual colors
def detect_color(frame, color):
    mask = cv2.inRange(frame, color['lower'], color['upper'])
        
    # Apply morphological operations to refine the mask
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((5,5), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))
    
    return mask

# Load the image
img = cv2.imread('C:/Users/victo/Desktop/Github REPOS/DartsSense/embedded/Camera/CV/dataset/1/valid/images/-103-_jpg.rf.c8a84a7d3bb1c0ed27b185b4f1c24ca9.jpg')
#img = cv2.imread('C:/Users/victo/Desktop/Github REPOS/DartsSense/embedded/Camera/CV/dataset/1/valid/images/-28-_jpg.rf.9c6bdfc931e5ddcf81474a6881213b07.jpg')
#img = cv2.imread('C:/Users/victo/Desktop/Github REPOS/DartsSense/embedded/Camera/CV/dataset/1/valid/images/-58-_jpg.rf.9db29c0ad69cf71dac8ee7663bffee71.jpg')
#img = cv2.imread('C:/Users/victo/Desktop/Github REPOS/DartsSense/embedded/Camera/CV/dataset/1/test/images/-105-_jpg.rf.cf2c5be62632628541fe43a1bf26af2f.jpg')
#img = cv2.imread('C:/Users/victo/Documents/Lightshot/board8.png')

# Perform object detection
results = model(img, stream=True)

# Extracting bounding boxes and confidence scores
for r in results:
    boxes = r.boxes
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        w, h = x2-x1, y2-y1
        # cv2.circle(img, (x1, y1), 5, (0, 255, 0), 5)
        # cv2.circle(img, (x2, y2), 5, (0, 0, 255), 5)
        cv2.rectangle(img, (x1+3, y1+3), (x1+w-3, y1+h-3), (0, 255, 0), 2, cv2.LINE_AA)

        conf = math.ceil((box.conf[0]*100))/100
        cls = box.cls[0]
        name = classNames[int(cls)]

        if name == 'tip':
            # Preprocess frame
            hsv = preprocess_frame(img)
            # Detect individual colors
            for color, color_info in dartboard_colors.items():
                mask = detect_color(hsv, color_info)
                if mask[x2, y2] == 255:
                    print(f"The tip is located in the {color} area.")
                    break

        # Draw text on the image
        cv2.putText(img, f'{name} {conf}', (max(0,x1), max(35,y1)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2, cv2.LINE_AA)

# Display the image
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
