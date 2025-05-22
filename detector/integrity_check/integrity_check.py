import cv2
import numpy as np
import os

def analyze_integrity(image_input):
    if isinstance(image_input, str):
        image = cv2.imread(image_input)
        image_name = os.path.basename(image_input)
    else:
        image = image_input
        image_name = "camera_frame.jpg"

    if image is None:
        print(f"Görüntü yüklenemedi.")
        return None

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not contours:
        return {"image": image_name, "status": "defective", "reason": "no_contours"}

    c = max(contours, key=cv2.contourArea)
    area = cv2.contourArea(c)
    hull = cv2.convexHull(c)
    hull_area = cv2.contourArea(hull)
    solidity = round(area / hull_area, 3) if hull_area != 0 else 0

    status = "ok" if solidity > 0.85 else "defective"

    return {
        "image": image_name,
        "area": area,
        "solidity": solidity,
        "status": status
    }
