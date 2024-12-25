from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog, QVBoxLayout, QPushButton, QWidget
import sys
from cartoonizer import cartoonize_image
from utils import load_image, save_image, display_image

class CartoonizerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cartoonizer")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Choose an image to cartoonize!")
        layout.addWidget(self.label)

        load_btn = QPushButton("Load Image")
        load_btn.clicked.connect(self.load_image)
        layout.addWidget(load_btn)

        cartoonize_btn = QPushButton("Cartoonize")
        cartoonize_btn.clicked.connect(self.cartoonize)
        layout.addWidget(cartoonize_btn)

        save_btn = QPushButton("Save Image")
        save_btn.clicked.connect(self.save_image)
        layout.addWidget(save_btn)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_image(self):
        options = QFileDialog.Options()
        self.filepath, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg *.jpeg)", options=options)
        if self.filepath:
            self.image = load_image(self.filepath)
            self.label.setText(f"Loaded: {self.filepath}")

    def cartoonize(self):
        if hasattr(self, 'image'):
            self.cartoon = cartoonize_image(self.image)
            display_image(self.cartoon, title="Cartoonized Image")

    def save_image(self):
        if hasattr(self, 'cartoon'):
            options = QFileDialog.Options()
            filepath, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "Images (*.png *.jpg *.jpeg)", options=options)
            if filepath:
                save_image(filepath, self.cartoon)
                self.label.setText(f"Saved to: {filepath}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CartoonizerApp()
    window.show()
    sys.exit(app.exec_())
