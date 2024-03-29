import cv2
import numpy as np
import urllib.request

# URL for video stream
url = 'http://192.168.1.20/getFrames.jpg'

# Define HSV color ranges for dartboard segments
dartboard_colors = {
    'black': {'lower': np.array([0, 0, 0]), 'upper': np.array([180, 255, 30])},
    'red': {'lower': np.array([0, 70, 50]), 'upper': np.array([10, 255, 255])},
    'white': {'lower': np.array([0, 0, 180]), 'upper': np.array([180, 25, 255])},
    'green': {'lower': np.array([40, 70, 50]), 'upper': np.array([80, 255, 255])}
}

# Function to preprocess frame
def preprocess_frame(frame):
    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    return hsv

# Function to detect individual colors
def detect_color(frame, color):
    mask = cv2.inRange(frame, color['lower'], color['upper'])
    return mask

def main():
    while True:
        # Read frame from the video stream
        resp = urllib.request.urlopen(url)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        frame = cv2.imdecode(image, cv2.IMREAD_COLOR)

        # Preprocess frame
        hsv = preprocess_frame(frame)

        # Detect individual colors
        color_masks = {}
        for color, color_range in dartboard_colors.items():
            mask = detect_color(hsv, color_range)
            color_masks[color] = mask

        # Display each color mask separately
        for color, mask in color_masks.items():
            cv2.imshow(color.capitalize(), mask)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()