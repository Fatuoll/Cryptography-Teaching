import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Visual.Art import  Ui_MainWindow


class Sluier(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Sluier()
    ex.show()
    sys.exit(app.exec())