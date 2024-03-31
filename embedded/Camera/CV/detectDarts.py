import cv2
import numpy as np
import urllib.request

# URL for video stream
url = 'http://192.168.1.20/getFrames.jpg'

def detect_darts(frame):
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define lower and upper bounds for light green color in HSV
    lower_green = np.array([40, 40, 40])  # Adjust as needed
    upper_green = np.array([80, 255, 255])  # Adjust as needed

    # Define lower and upper bounds for red color in HSV
    lower_red = np.array([0, 70, 50])  # Adjust as needed
    upper_red = np.array([10, 255, 255])  # Adjust as needed

    # Threshold the HSV image to get only light green and red regions
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_red = cv2.inRange(hsv, lower_red, upper_red)

    # Combine masks for green and red
    mask = cv2.bitwise_or(mask_green, mask_red)

    # Find contours in the combined mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours based on area and aspect ratio
    min_area = 1000  # Adjust as needed
    min_aspect_ratio = 1.0  # Adjust as needed
    detected_darts = []
    for contour in contours:
        # Approximate the contour to a polygon
        epsilon = 0.05 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Check if the contour is a rectangle (has 4 vertices) and meets area and aspect ratio criteria
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(contour)
            area = cv2.contourArea(contour)
            aspect_ratio = float(w) / h
            if area > min_area and aspect_ratio > min_aspect_ratio:
                # Extend the rectangle to the right edge of the image
                cv2.rectangle(frame, (x, y), (frame.shape[1]-180, y + h), (255, 0, 0), 1)
                detected_darts.append(approx)

    return frame, detected_darts

# def meets_dart_criteria(contour, image):
#     # Calculate the area of the contour
#     area = cv2.contourArea(contour)

#     # Calculate the perimeter of the contour
#     peri = cv2.arcLength(contour, True)

#     # Approximate the contour to a simpler shape with less vertices
#     epsilon = 0.02 * peri
#     approx = cv2.approxPolyDP(contour, epsilon, True)

#     # Check if the approximated shape is a rectangle
#     is_rectangle = len(approx) == 4

#     # Check if the area of the contour is within a certain range
#     min_area = 100
#     max_area = 1000
#     is_area_in_range = min_area <= area <= max_area

#     # Check if the aspect ratio of the contour is within a certain range
#     min_aspect_ratio = 0.8
#     max_aspect_ratio = 1.2
#     (x, y, w, h) = cv2.boundingRect(contour)
#     aspect_ratio = float(w) / h
#     is_aspect_ratio_in_range = min_aspect_ratio <= aspect_ratio <= max_aspect_ratio

#     # Check for the presence of sharp steel tip color (e.g., metallic tip color)
#     # Define the color range for the sharp steel tip
#     lower_color = np.array([0, 0, 120])  # Define the lower end of the color range (in BGR format)
#     upper_color = np.array([50, 50, 255])  # Define the upper end of the color range (in BGR format)

#     # Convert the image to the HSV color space
#     hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#     # Create a mask for the sharp steel tip color range
#     color_mask = cv2.inRange(hsv_image, lower_color, upper_color)

#     # Find contours in the color mask
#     color_contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # Check if the contour intersects with the color-based filter
#     intersects_color_filter = False
#     for c in color_contours:
#         area = cv2.contourArea(c)
#         if area > 10:  # Adjust the area threshold based on the expected size of the sharp steel tip
#             intersects_color_filter = True
#             break

#     # Return True if the contour meets all the criteria, including the color-based filter
#     return is_rectangle and is_area_in_range and is_aspect_ratio_in_range and intersects_color_filter

# resp = urllib.request.urlopen(url)
# image = np.asarray(bytearray(resp.read()), dtype="uint8")
# frame = cv2.imdecode(image, cv2.IMREAD_COLOR)

# # Apply Gaussian blur to reduce noise

# # Detect edges using Canny edge detector
# canny = cv2.Canny(frame, 100, 100)

# contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cont_img = cv2.drawContours(frame, contours, -1, (255, 0, 0), 1)
def main():
    while True:
        cap = urllib.request.urlopen(url)
        image = np.asarray(bytearray(cap.read()), dtype="uint8")
        frame = cv2.imdecode(image, cv2.IMREAD_COLOR)  # Replace with your camera sourceq
        detected_frame, detected_darts = detect_darts(frame)
        cv2.imshow("Detected Darts", detected_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
# # Find circles using Hough Circle Transform
# circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, dp=1, minDist=200, param1=200, param2=1, minRadius=10, maxRadius=10)

# # Ensure at least some circles were found
# if circles is not None:
#     circles = np.round(circles[0, :]).astype("int")

#     # Draw circles on the original image
#     for (x, y, r) in circles:
#         cv2.circle(frame, (x, y), r, (255, 0, 255), 4)

# trust = detect_darts(frame)

# # Display the image with circles
# # cv2.imshow("frame", frame)
# cv2.imshow("canny", canny)
# # cv2.imshow("contours", cont_img)
# cv2.imshow("trust", trust)
# cv2.waitKey(0)