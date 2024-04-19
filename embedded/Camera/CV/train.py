from ultralytics import YOLO
import torch

#print(torch.cuda.is_available())

model = YOLO("yolov8m.yaml")

results = model.train(data=r"C:\Users\victo\Desktop\Github REPOS\DartsSense\embedded\Camera\CV\config.yaml", epochs=1)
