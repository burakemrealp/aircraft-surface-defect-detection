from ultralytics import YOLO
import os

def run_inference(model_path, source_folder, output_folder="predictions"):
    """
    Runs inference using a YOLOv8 model on all images in a folder.

    Args:
        model_path (str): Path to YOLOv8 .pt weights file.
        source_folder (str): Folder containing input images.
        output_folder (str): Folder where predictions will be saved.
    """

    # Load model
    model = YOLO(model_path)

    # Run prediction
    results = model.predict(
        source=source_folder,
        save=True,
        project=output_folder,
        name="results",
        imgsz=640
    )

    print(f"Inference completed. Results saved to: {output_folder}/results")

if __name__ == "__main__":
    run_inference(
        model_path="models/yolov8s_best.pt",
        source_folder="data/test_images"
    )
