from ultralytics import YOLO
import torch

model = YOLO("yolov8n.yaml")

results = model.train(data=r"C:\Users\Viktorio\Desktop\DartsSense\DartsSense\embedded\Camera\CV\config.yaml", epochs=40)
