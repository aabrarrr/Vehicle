# 🚗 Deteksi Gambar Kendaraan
Projek ini adalah sistem deteksi kendaraan berbasis kecerdasan buatan yang memanfaatkan Computer Vision dan model deep learning Ultralytics YOLOv8 untuk mendeteksi dan mengklasifikasikan kendaraan dari sebuah gambar. Sistem ini mampu mengkategorikan kendaraan ke dalam lima kelas: mobil (car), truk (truck), bus, sepeda motor (motorcycle), dan ambulans (ambulance).

Cukup unggah foto pemandangan jalan atau lalu lintas — dan DriveWatch AI akan secara instan memproses gambar tersebut, memberikan kotak pembatas (bounding box) dan label pada setiap kendaraan yang terdeteksi melalui aplikasi web Gradio yang sederhana dan interaktif.

Sangat cocok untuk analisis lalu lintas secara otomatis, pemantauan keamanan, manajemen transportasi cerdas, dan aplikasi berbasis smart city.

-------
# Technologies 

- YOLOv8
- Ultralytics
- Gradio
- Python 3.10+
- NumPy & Pandas
- Matplotlib

 ------

 # Model Training
                   Class     Images  Instances      Box          R      mAP50      mAP50-95
                   all        250        454      0.777      0.518      0.596      0.456
             Ambulance         50         64      0.854      0.781      0.873      0.737
                   Bus         30         46      0.862      0.652      0.723      0.603
                   Car         90        238      0.654       0.42      0.484      0.346
            Motorcycle         42         46      0.651      0.435      0.443      0.285
                 Truck         38         60      0.863        0.3      0.458      0.307
 ------
  #  Web App
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
