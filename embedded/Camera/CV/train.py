from ultralytics import YOLO
import torch

model = YOLO("yolov8s.yaml")

results = model.train(data=r"C:\Users\Viktorio\Desktop\DartsSense\DartsSense\embedded\Camera\CV\config.yaml", epochs=20)