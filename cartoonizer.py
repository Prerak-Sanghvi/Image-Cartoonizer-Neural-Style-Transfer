import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image(filepath):
    """Load an image from a file."""
    return cv2.imread(filepath)

def save_image(filepath, image):
    """Save an image to a file."""
    cv2.imwrite(filepath, image)

def display_image(image, title="Image"):
    """Display an image using matplotlib."""
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(10, 10))
    plt.imshow(image_rgb)
    plt.axis('off')
    plt.title(title)
    plt.show()

def edge_detection(image):
    """Perform edge detection with softer, non-grainy edges."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.medianBlur(gray, 7)  # Smooth the grayscale image
    edges = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 2
    )
    return edges

def smooth_image(image):
    """Apply bilateral filtering for detail smoothing."""
    smoothed = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)
    return smoothed

def color_quantization(image, clusters=12):
    """Reduce the number of colors using k-means clustering."""
    data = image.reshape((-1, 3)).astype(np.float32)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    _, labels, centers = cv2.kmeans(data, clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = centers.astype(np.uint8)
    quantized = centers[labels.flatten()].reshape(image.shape)
    return quantized

def cartoonize_image(image):
    """Complete cartoonization pipeline."""
    # Step 1: Edge Detection
    edges = edge_detection(image)

    # Step 2: Smoothing the Image
    smoothed = smooth_image(image)

    # Step 3: Color Quantization
    quantized = color_quantization(smoothed)

    # Step 4: Combine with Edges
    edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    cartoon = cv2.bitwise_and(quantized, edges_colored)

    # Step 5: Avoid Excessive Black Areas
    cartoon = cv2.addWeighted(quantized, 0.9, cartoon, 0.1, 0)

    return cartoon

def main():
    filepath = input("Enter the path to your image: ")
    image = load_image(filepath)
    display_image(image, title="Original Image")

    cartoon = cartoonize_image(image)
    display_image(cartoon, title="Cartoonized Image")

    save_path = input("Enter the path to save the cartoonized image: ")
    save_image(save_path, cartoon)
    print(f"Cartoonized image saved to {save_path}")

if __name__ == "__main__":
    main()