from ultralytics import YOLO

# Load a pretrained YOLOv8s model
model = YOLO('yolov8s.pt')

# Train the model
model.train(
    data='dataset.yaml',
    epochs=30,
    imgsz=416,
    batch=5,
    project='TrainingResults',
    name='vehiclesDetection'
)