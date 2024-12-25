import cv2
import numpy as np
import torch
from ultralytics import YOLO  # Install YOLOv8 with `pip install ultralytics`


def get_person_mask(image):
    """
    Generate a binary mask for the person using YOLOv8 model.
    Args:
        image (ndarray): Input image.
    Returns:
        ndarray: Binary mask with 255 for the person and 0 elsewhere.
    """
    # Load YOLOv8 model (replace with a path to the model if needed)
    model = YOLO('yolov8n-seg.pt')  # Use YOLOv8 for segmentation
    results = model(image)

    # Extract person masks
    masks = results[0].masks.data.cpu().numpy()  # Get segmentation masks
    person_class = 0  # Class ID for "person"
    person_mask = np.zeros(image.shape[:2], dtype=np.uint8)

    for mask, class_id in zip(masks, results[0].masks.cls.cpu().numpy()):
        if int(class_id) == person_class:
            # Combine masks for all detected persons
            person_mask = cv2.bitwise_or(person_mask, (mask * 255).astype(np.uint8))

    return person_mask
