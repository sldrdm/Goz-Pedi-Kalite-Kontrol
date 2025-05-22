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

| İsim                 | Sorumluluk                        |
|----------------------|-----------------------------------|
| Serra Baysal         | Flutter Uygulama & UI             |
| Gülce Kiyakkaş       | YOLOv8 Model Eğitimi              |
| Zeynepnur Bozkurt    | Unity Simülasyonu                 |
| Selda  Erdem         | API ve Raporlama Modülü           |

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
