# 🧠 TechGirls - Medikal Ped Kalite Kontrol Sistemi

Bu proje, **Hackathon** kapsamında geliştirilen, **endüstriyel kalite kontrolüne** odaklı, görüntü işleme destekli bir mobil ve simülasyon çözümüdür. Medikal göz pedlerinin **hatalı ya da hatasız** oluşunu tespit eder, sınıflandırır, simülasyon ortamında ayrıştırır ve mobil uygulama ile kullanıcıya raporlar.

---

## 🔧 Kullanılan Teknolojiler

- 🧠 **YOLOv8 (Ultralytics)** → Ped tanıma ve hata tespiti  
- 🎥 **Python & OpenCV** → Görüntü analiz modülü  
- 📱 **Flutter** → Android mobil uygulama  
- 🕹️ **Unity** → Üretim bandı simülasyonu  
- 🌐 **FastAPI / Flask** → API entegrasyonu (opsiyonel)  
- 📋 **GitHub Projects & Issues** → Takım içi görev takibi

---

## 🧩 Proje Modülleri

### 🔍 1. Whole Recognition – Tüm Ped Tanıma
YOLOv8 ile pedler kare içine alınarak tespit edilir.

### 🧷 2. Component Inspection – Parça Bazlı Kontrol
- Kenar kesimi analizi  
- Simetri ve merkez kontrolü  

### 🛡️ 3. Integrity Check – Sağlamlık Tespiti
- Yırtık, eziklik ve şekil bozukluğu tespiti  
- Histogram ve kontur analizi kullanıldı

### 🎨 4. Color/Defect Detection – Renk & Leke Tespiti
- HSV renk uzayında analiz  
- Renk farkı, leke ve üretim hataları

### 📱 5. Mobil Uygulama (Flutter)
- Hata eşiği girilebiliyor (%0 - %100)  
- Hatalar ve oranlar grafikle gösteriliyor  
- Dinamik bilgi mesajları (örn. “%0 hata bulunamadı”)

### 🧪 6. Unity Simülasyonu
- Ürünler üretim bandında ilerler  
- Hatalı ürün ayrılır, sağlam ürün geçer  
- Gerçek zamanlı ayrıştırma görselleştirilir

---

## 🚀 Kurulum Talimatları

### 🐍 Python YOLOv8 Modeli
```bash
pip install -r requirements.txt
python detect.py --source sample.jpg --weights yolov8_eyepad.pt
```

### 📱 Flutter Mobil Uygulama
```bash
flutter pub get
flutter run
```

### 🕹️ Unity Simülasyon
- `unity_simulation/` klasörü Unity Hub ile açılır  
- Çalıştırıldığında sağlam ve hatalı ürün ayrımı izlenebilir

---

## 📦 Bağımlılıklar – `requirements.txt`

```
ultralytics==8.0.20
opencv-python==4.8.0.74
numpy==1.24.3
matplotlib==3.7.1
```

---

## 📷 Demo & Görseller

- 🎞️ `demo.mp4` – 2 dakikalık tanıtım videosu  
- 🖼️ `screenshots/` – Uygulama ve simülasyon görselleri  

---

## 👥 Takım Üyeleri

| İsim                | Sorumluluk                        |
|---------------------|-----------------------------------|
| Serra Baysal        | Flutter Uygulama & UI             |
| Gülce Kıyakkaş      | YOLOv8 Model Eğitimi              |
| Zeynep Nur Bozkurt  | Unity Simülasyonu                 |
| Selda Erdem         | API ve Raporlama Modülü           |

---

## 💡 Yenilikçi Özellikler

- Görsel analiz + simülasyon + mobil raporlama entegrasyonu  
- Dinamik hata eşiği ve anlamlı uyarı mesajları  
- Kullanıcı dostu tasarım ve kolay kullanım  
- Gerçek zamanlı simülasyonla desteklenmiş sonuçlar

---

## 🎤 Sunum İçeriği

- Proje tanıtımı ve çözüm yolu  
- Kullanılan teknolojiler ve iş akışı  
- Karşılaşılan zorluklar  
- 2 dakikalık video ve canlı demo  
- Sonuçlar & gelecek öneriler

---
## 🧠 Kod Karmaşıklığı Analizi

Kodun sürdürülebilirliği ve kalitesini değerlendirmek için radon ile Cyclomatic Complexity analizi yapılmıştır:

- 🔢 *Toplam analiz edilen fonksiyon sayısı:* 22
- 📈 *Ortalama karmaşıklık skoru:* A (3.04) → Kod yapısı oldukça sade ve okunabilir.
- ✅ *Genel Skor Dağılımı:*
  - A (1–5) → 18 fonksiyon
  - B (6–10) → 4 fonksiyon
  - C veya üzeri → Yok

*B seviyesi fonksiyonlar:*  
- analyze_component  
- analyze_integrity  
- run_camera_analysis  

Bu fonksiyonlar da makul seviyede karmaşıktır ve okunabilirliği korumaktadır.

> Kodun modülerliği ve okunabilirliği, uzun vadeli bakım ve entegrasyonlar için uygundur.
> C:\Users\gulce>python -m radon cc -s -a C:/Users/gulce/yolo_pad_project_merged
C:\Users\gulce\yolo_pad_project_merged\app\main.py
    F 33:0 analyze_image - A (3)
C:\Users\gulce\yolo_pad_project_merged\datasets\component_inspection\component_inspection.py
    F 35:0 analyze_component - B (6)
    F 6:0 preprocess_image - A (2)
    F 18:0 compute_symmetry_ssim - A (1)
    F 28:0 compute_contour_score - A (1)
C:\Users\gulce\yolo_pad_project_merged\datasets\defect_detection\defect_detection.py
    F 23:0 analyze_defects - A (5)
    F 5:0 detect_stains - A (1)
    F 16:0 detect_cuts - A (1)
C:\Users\gulce\yolo_pad_project_merged\datasets\integrity_check\integrity_check.py
    F 60:0 analyze_component - B (8)
    F 42:0 contour_integrity - A (3)
    F 5:0 crop_to_pad_area - A (2)
    F 18:0 symmetry_analysis - A (1)
    F 35:0 edge_clarity_analysis - A (1)
C:\Users\gulce\yolo_pad_project_merged\detector\component_inspection\component_inspection.py
    F 28:0 analyze_component - B (6)
    F 6:0 analyze_symmetry - A (1)
    F 23:0 analyze_edge_clarity - A (1)
C:\Users\gulce\yolo_pad_project_merged\detector\defect_detection\defect_detection.py
    F 20:0 analyze_defects - A (5)
    F 5:0 detect_stains - A (1)
    F 14:0 detect_cuts - A (1)
C:\Users\gulce\yolo_pad_project_merged\detector\integrity_check\integrity_check.py
    F 5:0 analyze_integrity - B (6)
C:\Users\gulce\yolo_pad_project_merged\utils\camera_detect.py
    F 10:0 run_camera_analysis - B (8)
C:\Users\gulce\yolo_pad_project_merged\yolov8_detector\yolov8_detector.py
    F 8:0 detect_pad - A (3)

22 blocks (classes, functions, methods) analyzed.
Average complexity: A (3.0454545454545454)

## 📁 Klasör Yapısı

```
TechGirls/
├── yolov8_model/              # YOLO model dosyaları
├── flutter_app/               # Mobil uygulama kodları
├── unity_simulation/          # Unity projesi
├── screenshots/               # Görseller
├── demo.mp4                   # Tanıtım videosu
├── requirements.txt
└── README.md
```

---

🧠 **TechGirls** ile kalite kontrolde geleceği şekillendiriyoruz!
