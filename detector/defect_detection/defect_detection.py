import cv2
import numpy as np
import os

def detect_stains(image, threshold=30):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mean_val = np.mean(gray)
    mean_image = np.full_like(gray, mean_val, dtype=np.uint8)
    diff = cv2.absdiff(gray, mean_image)
    _, binary = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)
    stain_ratio = np.sum(binary > 0) / (gray.shape[0] * gray.shape[1])
    return round(stain_ratio, 4)

def detect_cuts(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    edge_density = np.sum(edges > 0) / (edges.shape[0] * edges.shape[1])
    return round(edge_density, 4)

def analyze_defects(image_input):
    if isinstance(image_input, str):
        image = cv2.imread(image_input)
        image_name = os.path.basename(image_input)
    else:
        image = image_input
        image_name = "camera_frame.jpg"

    if image is None:
        print(f"Görüntü yüklenemedi.")
        return None

    stain_score = detect_stains(image)
    cut_score = detect_cuts(image)

    result = {
        "image": image_name,
        "stain_ratio": stain_score,
        "edge_density": cut_score,
        "status": "defective" if stain_score > 0.3 or cut_score < 0.01 else "ok"
    }

    return result
