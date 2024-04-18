import cv2
import numpy as np
import urllib.request
import imutils

# URL for video stream
url = 'http://192.168.1.9/getFrames.jpg'

img1 = cv2.imread('C:/Users/victo/Documents/Lightshot/test.jpg')
img1 = cv2.resize(img1, (640, 480))
img2 = cv2.imread('C:/Users/victo/Documents/Lightshot/test2.jpg')
img2 = cv2.resize(img2, (640, 480))

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

diff = cv2.absdiff(gray1, gray2)
cv2.imshow('diff', diff)

thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

kernel = np.ones((2, 2), np.uint8)
dilate = cv2.dilate(thresh, kernel, iterations=2)
cv2.imshow('dilate', dilate)

contours = cv2.findContours(dilate.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

for c in contours:
    if cv2.contourArea(c) > 100:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 2)

# cv2.imshow('thresh', thresh)
# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
x = np.zeros((480,10,3), np.uint8)
result = np.hstack((img1, x, img2))
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# def detect_darts_tips(image):
#     # Preprocess the image
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     blur = cv2.GaussianBlur(gray, (3, 3), cv2.BORDER_DEFAULT)

#     # Apply Canny edge detection
#     edges = cv2.Canny(blur, 50, 150)

#     # Find contours
#     contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # Filter contours based on shape, area, and aspect ratio
#     darts_tips = []
#     min_area = 100  # Minimum area for a contour to be considered a dart tip
#     min_aspect_ratio = 0.5  # Minimum aspect ratio for a contour to be considered a dart tip

#     for contour in contours:
#         area = cv2.contourArea(contour)
#         peri = cv2.arcLength(contour, True)
#         approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

#         # Calculate the bounding box of the contour
#         x, y, w, h = cv2.boundingRect(contour)
#         aspect_ratio = float(w) / h

#         if area > min_area and len(approx) == 4 and aspect_ratio > min_aspect_ratio:
#             darts_tips.append(contour)

#     # Draw circles around the darts tips
#     for tip in darts_tips:
#         (x, y), radius = cv2.minEnclosingCircle(tip)
#         center = (int(x), int(y))
#         cv2.circle(image, center, int(radius), (255, 0, 0), 3)

#     return image

# resp = urllib.request.urlopen(url)
# image = np.asarray(bytearray(resp.read()), dtype="uint8")
# frame = cv2.imdecode(image, cv2.IMREAD_COLOR)

# # Apply Gaussian blur to reduce noise

# # Detect edges using Canny edge detector
# canny = cv2.Canny(frame, 100, 100)

# contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cont_img = cv2.drawContours(frame, contours, -1, (255, 255, 0), 3)

# # Find circles using Hough Circle Transform
# circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, dp=1, minDist=200, param1=200, param2=1, minRadius=10, maxRadius=10)

# # Ensure at least some circles were found
# if circles is not None:
#     circles = np.round(circles[0, :]).astype("int")

#     # Draw circles on the original image
#     for (x, y, r) in circles:
#         cv2.circle(frame, (x, y), r, (255, 0, 255), 4)

# trust = detect_darts_tips(frame)

# # Display the image with circles
# # cv2.imshow("frame", frame)
# cv2.imshow("canny", canny)
# # cv2.imshow("contours", cont_img)
# cv2.imshow("trust", trust)
# cv2.waitKey(0)