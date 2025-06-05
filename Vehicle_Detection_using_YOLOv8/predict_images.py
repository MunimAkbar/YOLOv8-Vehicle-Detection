from ultralytics import YOLO

model = YOLO('C:/Users/cowlar/Downloads/Vehicle_Detection_using_YOLOv8/TrainingResults/vehiclesDetection2/weights/best.pt')

model.predict(
    source = 'C:/Users/cowlar/Downloads/Vehicle_Detection_using_YOLOv8/VehiclesDetectionDataset/test/images',
    conf=0.5,
    save=True
)
