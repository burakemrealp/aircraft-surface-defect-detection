# Aircraft Surface Crack Detection using YOLOv8

This project presents an automated crack detection system for aircraft fuselage surfaces using deep learning–based computer vision. A custom dataset of real aircraft surface images was used to train YOLOv8 models, achieving high accuracy in detecting structural cracks.

## Features
* Custom dataset of aircraft fuselage defects
* YOLOv8n (baseline) and YOLOv8s (improved) models
* High‑accuracy crack detection
* Real‑time inference capability
* Clean and reproducible training pipeline
* Lightweight Python scripts for training and inference

## Project Structure
* data/
  * aircraft_fuselage.yaml
* models/
  * yolov8n_results.txt
  * yolov8s_results.txt
  * readme.md
* results/
  * yolov8n/
  * yolov8s/
  * sample_predictions/
* src/
  * train.py
  * predict.py
  * utils.py
* requirements.txt
* README.md

## Model Performance
| Metric | YOLOv8n | YOLOv8s |
| --- | --- | --- |
| Precision | 0.714 | **0.883** |
| Recall | 0.622 | **0.662** |
| mAP50 | 0.651 | **0.752** |
| mAP50‑95 | 0.329 | **0.390** |

## Sample Predictions
Sample inference results can be found in:
results/sample_predictions/

## Training
yolo detect train model=yolov8s.pt data=data/aircraft_fuselage.yaml epochs=50 imgsz=640

## Inference
yolo detect predict model=models/yolov8s_best.pt source=path/to/images
Or using the included script:
python src/predict.py

## Download Model Weights
Model weights are stored externally due to size limitations.
* YOLOv8n best.pt → https://drive.google.com/file/d/1U-8TitQ87gfdj_KdGLtbc7FlAx7xiVx6/view?usp=drive_link
* YOLOv8s best.pt → https://drive.google.com/file/d/1AoC5-OB08-VVN4kDlpItg_820B_YeulF/view?usp=drive_link

## Requirements
ultralytics
opencv-python
numpy

## License
MIT License
