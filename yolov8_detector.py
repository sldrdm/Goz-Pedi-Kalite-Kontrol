from ultralytics import YOLO
import cv2
import os

# Modeli belleğe bir kez yükle (model yolunu güncelle)
model = YOLO("C:\\Users\\gulce\\yolo_pad_project_merged\\runs\\detect\\pad_model_v3\\weights\\best.pt")

def detect_pad(image_path, conf=0.25):
    """
    YOLOv8 ile göz pedi tespiti yapar.
    """
    results = model(image_path, conf=conf)
    detections = []

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            conf_score = float(box.conf[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            detections.append({
                "class_id": cls,
                "confidence": round(conf_score, 2),
                "box": [x1, y1, x2, y2]
            })

    return detections
