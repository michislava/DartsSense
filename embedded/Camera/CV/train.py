from ultralytics import YOLO
import torch

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

print(torch.cuda.device_count())

# model = YOLO("yolov8n.yaml")

# results = model.train(data=r"C:\Users\victo\Desktop\Github REPOS\DartsSense\embedded\Camera\CV\config.yaml", epochs=1, device=)