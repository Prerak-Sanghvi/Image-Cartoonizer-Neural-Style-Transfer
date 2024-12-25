# main.py
from gui import CartoonizerApp
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CartoonizerApp()
    window.show()
    sys.exit(app.exec_())
