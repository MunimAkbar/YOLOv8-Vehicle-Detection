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

## 📦 Dataset

The dataset used for training the vehicle detection model can be downloaded from the link below:

🔗 [Download Dataset from Roboflow](https://universe.roboflow.com/roboflow-gw7yv/vehicles-openimages/dataset/1)

After downloading, extract the contents and place them in a folder named `dataset` in the root directory of this repository. Make sure the `dataset.yaml` file is correctly configured to point to the dataset's structure.
