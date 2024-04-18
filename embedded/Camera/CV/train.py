from ultralytics import YOLO
import torch

model = YOLO("yolov8s.yaml")

<<<<<<< HEAD
#print(torch.cuda.is_available())

model = YOLO("yolov8n.yaml")

results = model.train(data=r"C:\Users\victo\Desktop\Github REPOS\DartsSense\embedded\Camera\CV\config.yaml", epochs=1, device=0)
=======
results = model.train(data=r"C:\Users\Viktorio\Desktop\DartsSense\DartsSense\embedded\Camera\CV\config.yaml", epochs=20)
>>>>>>> 6c397215b2d58f2df22b73d32654fe5eef96f0d1
