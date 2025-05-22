from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
import uuid
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from app.yolov8_detector import detect_pad
from detector.component_inspection.component_inspection import analyze_component
from detector.defect_detection.defect_detection import analyze_defects
from detector.integrity_check.integrity_check import analyze_integrity

# FastAPI uygulamasını başlat
app = FastAPI()

# CORS ayarları (mobil cihazdan erişim için)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # üretimde sadece Flutter IP'si olmalı
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Yüklenen görsellerin geçici olarak kaydedileceği klasör
UPLOAD_DIR = "temp_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    try:
        # Görseli geçici dizine kaydet
        filename = f"{uuid.uuid4()}.jpg"
        file_path = os.path.join(UPLOAD_DIR, filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 1. Ped Tespiti (YOLOv8)
        yolo_results = detect_pad(file_path)

        if not yolo_results:
            return JSONResponse({"error": "Ped tespit edilemedi."}, status_code=400)

        # 2. Görsel İşleme Analizleri
        component_result = analyze_component(file_path)
        defect_result = analyze_defects(file_path)
        integrity_result = analyze_integrity(file_path)

        # Sonuçları birleştir
        result = {
            "detection": yolo_results,
            "component_inspection": component_result,
            "defect_detection": defect_result,
            "integrity_check": integrity_result,
        }

        return result

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
