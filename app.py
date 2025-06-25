import gradio as gr
from ultralytics import YOLO
import os

# Load model YOLOv8
model_path = "best.pt"

if not os.path.exists(model_path):
    raise FileNotFoundError("Model YOLO tidak ditemukan. Pastikan best.pt tersedia di direktori yang sama.")

model = YOLO(model_path)

# Fungsi deteksi
def detect_vehicle(image):
    results = model.predict(image)
    result_image = results[0].plot()  # Visualisasi dengan bounding box
    return result_image

# UI Gradio
title = "🚗 Deteksi Gambar Kendaraan"
description = "Unggah gambar kendaraan lalu klik tombol Deteksi untuk menjalankan analisis menggunakan model YOLOv8."

demo = gr.Interface(
    fn=detect_vehicle,
    inputs=gr.Image(type="pil"),
    outputs=gr.Image(type="numpy"),
    title=title,
    description=description,
    allow_flagging="never"
)

# Jalankan aplikasi (saat dijalankan lokal)
if __name__ == "__main__":
    demo.launch()
