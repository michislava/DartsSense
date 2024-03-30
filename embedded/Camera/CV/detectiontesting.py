import cv2
import numpy as np
import urllib.request

# URL for video stream
url = 'http://192.168.1.20/getFrames.jpg'

def detect_and_draw_circles(image, threshold):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (3, 3), cv2.BORDER_DEFAULT)

    # Apply Canny edge detection with a larger filter
    edges = cv2.Canny(blur, threshold[0], threshold[1], apertureSize=3, L2gradient=False)
    
    # Find contours of the edges
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw circles around the sharp edges
    for contour in contours:
        # Approximate the contour to a circle
        (x, y), radius = cv2.minEnclosingCircle(contour)
        center = (int(x), int(y))
        cv2.circle(image, center, int(radius), (255, 0, 0), 3)
    
    return image

resp = urllib.request.urlopen(url)
image = np.asarray(bytearray(resp.read()), dtype="uint8")
frame = cv2.imdecode(image, cv2.IMREAD_COLOR)

# Apply Gaussian blur to reduce noise

# Detect edges using Canny edge detector
canny = cv2.Canny(frame, 100, 100)

contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cont_img = cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

# Find circles using Hough Circle Transform
circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, dp=1, minDist=200, param1=200, param2=1, minRadius=10, maxRadius=10)

# Ensure at least some circles were found
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")

    # Draw circles on the original image
    for (x, y, r) in circles:
        cv2.circle(frame, (x, y), r, (255, 0, 255), 4)

trust = detect_and_draw_circles(frame, [200, 200])

# Display the image with circles
# cv2.imshow("frame", frame)
cv2.imshow("canny", canny)
# cv2.imshow("contours", cont_img)
cv2.imshow("trust", trust)
cv2.waitKey(0)