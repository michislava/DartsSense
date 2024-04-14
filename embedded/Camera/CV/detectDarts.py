import cv2
import numpy as np
import urllib.request
import time

# URL for video stream
url = 'http://192.168.1.9/getFrames.jpg'

def grabScore(detected_darts, score):
    if detected_darts: 
        maxScore = 301
        print("Detected darts at:\n", detected_darts)
        print("ScoredNow: {}".format(score), "Score {}".format(maxScore-score))
def detectDarts(frame):
    score = 15
    # HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_green = np.array([40, 40, 40])  
    upper_green = np.array([80, 255, 255])  

    # Маска за (в момента за зелени стрели)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # Търсене на контури със зелена маска
    contours, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Филтриране на контури
    min_area = 1600  
    min_aspect_ratio = 1.2  
    detected_darts = []
    for contour in contours:
        # Контур -> полигон
        epsilon = 0.03 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Проверка за дартс
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(contour)
            area = cv2.contourArea(contour)
            aspect_ratio = float(w) / h
            if area > min_area and aspect_ratio > min_aspect_ratio:
                # Правоъгълник + текст
                cv2.rectangle(frame, (x, y), (frame.shape[1]-190, y + h), (0, 255, 255), 3)
                cv2.putText(frame, "Score: {}".format(score), (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,255,255), thickness=2)

                #right_midpoint_x = x + w  e
                right_midpoint_y = y + h // 2  

                # Draw a yellow circle at the midpoint
                cv2.circle(frame, (frame.shape[1]-190, right_midpoint_y), radius=8, color=(0, 255, 255), thickness=-1)

                detected_darts.append((x, y))
                

    return frame, detected_darts, score

def main():
    while True:
        cap = urllib.request.urlopen(url)
        image = np.asarray(bytearray(cap.read()), dtype="uint8")
        frame = cv2.imdecode(image, cv2.IMREAD_COLOR)  # Replace with your camera sourceq
        detected_frame, detected_darts, score = detectDarts(frame)
        cv2.imshow("DartsSense", detected_frame)
        grabScore(detected_darts, score)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
