
import cv2
import numpy as np
import os

def analyze_symmetry(image):
    h, w = image.shape[:2]
    left = image[:, :w // 2]
    right = image[:, w - (w // 2):]
    right_flipped = cv2.flip(right, 1)

    # Boyut uyuşmazlığına karşı kırp
    min_h = min(left.shape[0], right_flipped.shape[0])
    min_w = min(left.shape[1], right_flipped.shape[1])
    left = left[:min_h, :min_w]
    right_flipped = right_flipped[:min_h, :min_w]

    diff = cv2.absdiff(left, right_flipped)
    score = np.mean(diff)
    return round(score, 2)


def analyze_edge_clarity(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    return round(np.sum(edges > 0) / (edges.shape[0] * edges.shape[1]), 4)

def analyze_component(image_path_or_image, save_path=None):
    if isinstance(image_path_or_image, str):
        image = cv2.imread(image_path_or_image)
        image_name = os.path.basename(image_path_or_image)
    else:
        image = image_path_or_image
        image_name = "from_camera.jpg"

    if image is None:
        print(f"Görüntü yüklenemedi: {image_path_or_image}")
        return None

    symmetry_score = analyze_symmetry(image)
    edge_score = analyze_edge_clarity(image)

    result = {
        "image": image_name,
        "symmetry": symmetry_score,
        "edge_clarity": edge_score,
        "status": "defective" if symmetry_score > 30 or edge_score < 0.01 else "ok"
    }

    if save_path:
        with open(save_path, "a") as f:
            f.write(str(result) + "\n")

    return result
