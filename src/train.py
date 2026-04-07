from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.pt")

    model.train(
        data="data/aircraft_fuselage.yaml",
        epochs=50,
        imgsz=640,
        batch=16,
        project="runs/aircraft_fuselage",
        name="yolov8n-baseline",
    )

if __name__ == "__main__":
    main()
