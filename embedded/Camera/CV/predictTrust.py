from ultralytics import YOLO
import cv2
import cvzone
import math

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

model = YOLO('/runs/detetct/train13/weights/best.pt')

classNames = ["cal1",
"cal2",
"cal3",
"cal4",
"center",
"tip"]

while True:
    success, img  =cap.read()
    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2-x1, y2-y1
            cvzone.cornerRect(img, (x1, y1, w, h))

            conf = math.ceil((box.conf[0]*100))/100

            cls = box.cls[0]
            name = classNames[int(cls)]

            cvzone.putTextRect(img, f'{name} 'f'{conf}', (max(0,x1), max(35,y1)), scale = 0.5)

    cv2.imshow("Image", img)
    cv2.waitKey(1)