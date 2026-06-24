# main.py
import sys
from PyQt6.QtWidgets import QApplication

from navegador.browser import Browser

def main():
    app = QApplication(sys.argv)

    browser = Browser()
    browser.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()