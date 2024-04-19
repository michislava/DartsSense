from ultralytics import YOLO
import torch

<<<<<<< HEAD
#print(torch.cuda.is_available())

model = YOLO("yolov8m.yaml")

results = model.train(data=r"C:\Users\victo\Desktop\Github REPOS\DartsSense\embedded\Camera\CV\config.yaml", epochs=1)
=======
model = YOLO("yolov8n.yaml")

results = model.train(data=r"C:\Users\Viktorio\Desktop\DartsSense\DartsSense\embedded\Camera\CV\config.yaml", epochs=40)
>>>>>>> 75c648e955ba6b08187e3d60f2eb67da181b6124
