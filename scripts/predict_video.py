from ultralytics import YOLO

model = YOLO('C:/Users/Downloads/Vehicle_Detection_using_YOLOv8/TrainingResults/vehiclesDetection2/weights/best.pt')

model.predict(
    source='C:/Users/Downloads/Vehicle_Detection_using_YOLOv8/TestVideo',
    conf=0.75,
    save=True
)
