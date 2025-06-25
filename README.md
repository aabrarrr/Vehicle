# 🚗 Deteksi Gambar Kendaraan
Projek ini adalah sistem deteksi kendaraan berbasis kecerdasan buatan yang memanfaatkan Computer Vision dan model deep learning Ultralytics YOLOv8 untuk mendeteksi dan mengklasifikasikan kendaraan dari sebuah gambar. Sistem ini mampu mengkategorikan kendaraan ke dalam lima kelas: mobil (car), truk (truck), bus, sepeda motor (motorcycle), dan ambulans (ambulance).

Cukup unggah foto pemandangan jalan atau lalu lintas — dan DriveWatch AI akan secara instan memproses gambar tersebut, memberikan kotak pembatas (bounding box) dan label pada setiap kendaraan yang terdeteksi melalui aplikasi web Gradio yang sederhana dan interaktif.

Sangat cocok untuk analisis lalu lintas secara otomatis, pemantauan keamanan, manajemen transportasi cerdas, dan aplikasi berbasis smart city.

-------
## 🛠️ Technologies 

- YOLOv8
- Ultralytics
- Gradio
- Python 3.10+
- NumPy & Pandas
- Matplotlib

 ------
  # 🌐 Web App
  - Upload gambar
  - Gambar akan dilatih menggunakan model YOLOv8
  - Hasil gambar yang memberikan bounding box dengan label

## How to Run Project

1. Clone this repository.
2. Install the dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```
4. Run the project:
   
   ```bash
   python app.py
