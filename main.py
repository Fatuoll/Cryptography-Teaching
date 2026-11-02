import sys
from PyQt6.QtWidgets import QApplication

from src.UI.Connections import Sluier


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Sluier()
    ex.show()
    sys.exit(app.exec())