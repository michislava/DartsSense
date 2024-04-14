import cv2
import numpy as np
import urllib.request

# URL for video stream
url = 'http://192.168.1.9/getFrames.jpg'

def detect_darts_tips(image):
    # Preprocess the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), cv2.BORDER_DEFAULT)

    # Apply Canny edge detection
    edges = cv2.Canny(blur, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours based on shape, area, and aspect ratio
    darts_tips = []
    min_area = 100  # Minimum area for a contour to be considered a dart tip
    min_aspect_ratio = 0.5  # Minimum aspect ratio for a contour to be considered a dart tip

    for contour in contours:
        area = cv2.contourArea(contour)
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

        # Calculate the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = float(w) / h

        if area > min_area and len(approx) == 4 and aspect_ratio > min_aspect_ratio:
            darts_tips.append(contour)

    # Draw circles around the darts tips
    for tip in darts_tips:
        (x, y), radius = cv2.minEnclosingCircle(tip)
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
cont_img = cv2.drawContours(frame, contours, -1, (255, 255, 0), 3)

# Find circles using Hough Circle Transform
circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, dp=1, minDist=200, param1=200, param2=1, minRadius=10, maxRadius=10)

# Ensure at least some circles were found
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")

    # Draw circles on the original image
    for (x, y, r) in circles:
        cv2.circle(frame, (x, y), r, (255, 0, 255), 4)

trust = detect_darts_tips(frame)

# Display the image with circles
# cv2.imshow("frame", frame)
cv2.imshow("canny", canny)
# cv2.imshow("contours", cont_img)
cv2.imshow("trust", trust)
cv2.waitKey(0)