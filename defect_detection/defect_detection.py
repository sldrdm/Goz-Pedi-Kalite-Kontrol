import cv2
import numpy as np
import os

def detect_stains(image, threshold=40):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    saturation = hsv[:, :, 1]  # Doygunluk kanalı

    mean_sat = np.mean(saturation)
    diff = cv2.absdiff(saturation, np.full_like(saturation, mean_sat, dtype=np.uint8))
    _, binary = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)

    stain_ratio = np.sum(binary > 0) / binary.size
    return round(stain_ratio, 4)

def detect_cuts(image, low_threshold=100, high_threshold=200):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, low_threshold, high_threshold)

    edge_density = np.sum(edges > 0) / edges.size
    return round(edge_density, 4)

def analyze_defects(image_path, save_path=None):
    image = cv2.imread(image_path)
    if image is None:
        print(f" Görüntü yüklenemedi: {image_path}")
        return None

    stain_ratio = detect_stains(image)
    edge_density = detect_cuts(image)

    #  Yeni, daha doğru eşikler:
    if stain_ratio > 0.2 or edge_density < 0.005:
        status = "defective"
    else:
        status = "ok"

    result = {
        "image": os.path.basename(image_path),
        "stain_ratio": stain_ratio,
        "edge_density": edge_density,
        "status": status
    }

    if save_path:
        with open(save_path, "a") as f:
            f.write(str(result) + "\n")

    return result

if __name__ == "__main__":
    input_dir = "C:\\Users\\gulce\\yolo_pad_project_merged\\datasets\\defect_detection\\images"
    output_path = "C:\\Users\\gulce\\yolo_pad_project_merged\\datasets\\defect_detection\\results\\defect_results.txt"

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print(" Defect Detection Başladı...\n")
    for filename in os.listdir(input_dir):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(input_dir, filename)
            result = analyze_defects(image_path, save_path=output_path)
            print(result)
