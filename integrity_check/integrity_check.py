import cv2
import numpy as np
import os

def crop_to_pad_area(image):
    """Pad’in olduğu alanı bul ve kırp."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 180, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if not contours:
        return image
    c = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(c)
    return image[y:y+h, x:x+w]

def symmetry_analysis(pad):
    """Simetriyi sadece pad merkezinden ölç."""
    h, w = pad.shape[:2]
    mid = w // 2
    left = pad[:, :mid]
    right = pad[:, mid:]
    right_flipped = cv2.flip(right, 1)

    h = min(left.shape[0], right_flipped.shape[0])
    w = min(left.shape[1], right_flipped.shape[1])
    left = left[:h, :w]
    right_flipped = right_flipped[:h, :w]

    diff = cv2.absdiff(left, right_flipped)
    score = np.mean(diff)
    return score

def edge_clarity_analysis(pad):
    """Canny edge yoğunluğu (kesik varsa düşük olur)."""
    gray = cv2.cvtColor(pad, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    density = np.sum(edges > 0) / (gray.shape[0] * gray.shape[1])
    return density

def contour_integrity(pad):
    """Konturun düzgünlüğü: Kesik varsa kontur bozulur."""
    gray = cv2.cvtColor(pad, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if not contours:
        return 0.0

    c = max(contours, key=cv2.contourArea)
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c, True)

    if perimeter == 0:
        return 0.0
    solidity = 4 * np.pi * area / (perimeter ** 2)
    return solidity

def analyze_component(image_path, save_path=None):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Görüntü yüklenemedi: {image_path}")
        return None

    pad = crop_to_pad_area(image)

    symmetry = symmetry_analysis(pad)
    edge_density = edge_clarity_analysis(pad)
    integrity = contour_integrity(pad)

    # Durum analizi
    reasons = []
    if symmetry > 42:
        reasons.append("low symmetry")
    if edge_density < 0.007:
        reasons.append("low edge density (possible cut)")
    if integrity < 0.61:
        reasons.append("contour irregular")

    result = {
        "image": os.path.basename(image_path),
        "symmetry": round(symmetry, 2),
        "edge_density": round(edge_density, 4),
        "contour_integrity": round(integrity, 3),
        "status": "defective" if reasons else "ok",
        "reasons": reasons or "none"
    }

    if save_path:
        with open(save_path, "a") as f:
            f.write(str(result) + "\n")

    return result

# Ana çalıştırıcı
if __name__ == "__main__":
    input_dir = "C:\\Users\\gulce\\yolo_pad_project_merged\\datasets\\component_inspection\\images"
    output_path = "C:\\Users\\gulce\\yolo_pad_project_merged\\datasets\\component_inspection\\results\\component_results.txt"

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    print("Parça Bazlı Kontrol Başladı...\n")

    for filename in os.listdir(input_dir):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            image_path = os.path.join(input_dir, filename)
            result = analyze_component(image_path, save_path=output_path)
            print(result)
