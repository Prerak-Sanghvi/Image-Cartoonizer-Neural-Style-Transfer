import cv2
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