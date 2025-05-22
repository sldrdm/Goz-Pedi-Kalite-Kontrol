
import cv2
import numpy as np
import time
from yolov8_detector.yolov8_detector import detect_pad
from detector.component_inspection.component_inspection import analyze_symmetry, analyze_edge_clarity
from detector.integrity_check.integrity_check import analyze_integrity
from detector.defect_detection.defect_detection import analyze_defects

def run_camera_analysis(model_path="C:\\Users\\gulce\\yolo_pad_project_merged\\runs\\detect\\pad_model_v3\\weights\\best.pt"):
    print("Gerçek zamanlı ped kontrolü başladı...\n")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Kamera açılamadı.")
        return

    model = detect_pad(model_path=model_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Kare alınamadı, çıkılıyor...")
            break

        # YOLO ile ped tespiti
        results = model(frame)

        for result in results:
            boxes = result.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                pad_crop = frame[y1:y2, x1:x2]

                try:
                    cv2.imwrite("camera_frame.jpg", pad_crop)

                    symmetry = analyze_symmetry(pad_crop)
                    edge = analyze_edge_clarity(pad_crop)
                    integrity = analyze_integrity(pad_crop)
                    defects = analyze_defects(pad_crop)

                    print(f"Ped Analizi Sonucu:")
                    print(f"Symmetry Score: {symmetry}")
                    print(f"Edge Clarity: {edge}")
                    print(f"Integrity: {integrity}")
                    print(f"Defects: {defects}\n")
                except Exception as e:
                    print("Hata oluştu:", e)

                # Çerçeve çiz
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        cv2.imshow("Ped Analizi", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_camera_analysis()
