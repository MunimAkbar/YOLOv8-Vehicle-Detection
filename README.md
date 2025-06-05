# 🚗 Vehicle Detection using YOLOv8

This project detects vehicles in images and videos using a fine-tuned YOLOv8 model.

## 📁 Folder Structure

- `train_model.py`: Script to train YOLOv8 on the custom dataset  
- `predict_images.py`: Script to run detection on images  
- `predict_video.py`: Script to run detection on videos  
- `validate_model.py`: Script to validate the trained model  
- `export_model.py`: Export the model to ONNX format  
- `dataset.yaml`: Dataset configuration file  
- `requirements.txt`: Python dependencies  
- `VehiclesDetectionDataset/`: Directory for your custom dataset (train/val/test)

## 📦 Dataset

The dataset used for training the vehicle detection model can be downloaded from the link below:

🔗 [Download Dataset from Roboflow](https://universe.roboflow.com/roboflow-gw7yv/vehicles-openimages/dataset/1)

After downloading, follow these steps:
# Step 1: Download and unzip the dataset
# (Use your browser or wget if direct download link is available)

# Step 2: Move the extracted folder to the root directory of the project
mv path_to_extracted_folder ./dataset

# Step 3: Ensure dataset.yaml is correctly configured
# Open dataset.yaml and check paths for train, val, and test

## ⚙️ Setup

Make sure you have Python installed. Then, install all required packages:

```bash
pip install -r requirements.txt
