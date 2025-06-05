# Vehicle Detection using YOLOv8

This project detects vehicles in images and videos using a fine-tuned YOLOv8 model.

## Folder Structure
- `train_model.py`: Train YOLOv8 on custom dataset
- `predict_images.py`: Run detection on images
- `predict_videos.py`: Run detection on videos
- `dataset.yaml`: Dataset configuration
- `VehiclesDetectionDataset/`: Custom dataset (train/val/test)

## Setup
```bash
pip install -r requirements.txt
