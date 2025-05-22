import cv2
import numpy as np
import os
from skimage.metrics import structural_similarity as ssim

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return None
    largest = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(largest)
    pad = image[y:y+h, x:x+w]
    resized = cv2.resize(pad, (256, 256))
    return resized

def compute_symmetry_ssim(image):
    h, w = image.shape[:2]
    left = image[:, :w//2]
    right = image[:, w//2:]
    right_flipped = cv2.flip(right, 1)
    left_gray = cv2.cvtColor(left, cv2.COLOR_BGR2GRAY)
    right_gray = cv2.cvtColor(right_flipped, cv2.COLOR_BGR2GRAY)
    score = ssim(left_gray, right_gray)
    return score

def compute_contour_score(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    edged = cv2.Canny(blurred, 50, 150)
    contour_density = np.sum(edged > 0) / (edged.shape[0] * edged.shape[1])
    return contour_density

def analyze_component(image_path, save_path=None):
    raw = cv2.imread(image_path)
    if raw is None:
        print(f"Görüntü yüklenemedi: {image_path}")
        return None

    img = preprocess_image(raw)
    if img is None:
        return {"image": os.path.basename(image_path), "status": "unreadable"}

    sym_score = compute_symmetry_ssim(img)
    contour_score = compute_contour_score(img)

    # Karar kriteri: simetri düşükse ya da kenar netliği azsa defective
    status = "defective" if sym_score < 0.3 or contour_score < 0.01 else "ok"

    result = {
        "image": os.path.basename(image_path),
        "symmetry_ssim": round(sym_score, 4),
        "contour_density": round(contour_score, 4),
        "status": status
    }

    if save_path:
        with open(save_path, "a") as f:
            f.write(str(result) + "\n")

    return result

if __name__ == "__main__":
    input_dir = "C:\\Users\\gulce\\yolo_pad_project_merged\\datasets\\component_inspection\\images"
    output_path = "C:\\Users\\gulce\\yolo_pad_project_merged\\datasets\\component_inspection\\results\\component_results.txt"

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    print("Parça Bazlı Kontrol Başladı...\n")

    for filename in os.listdir(input_dir):
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
            path = os.path.join(input_dir, filename)
            result = analyze_component(path, output_path)
            print(result)
