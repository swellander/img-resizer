import sys
from PyQt5.QtWidgets import * 

class TableWidget(QTableWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAcceptDrops(True)
        self.setGeometry(20, 20, 600, 200)
        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(["Filename", "Dimensions", "Size", "New Dimensions"])

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            print("Acceptable files")
            event.accept()
        else:
            print(f'Ignoring file: {event}')
            event.ignore()

    def dropEvent(self, event):
        print("DROPPED")
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            print(f)


class SettingsWidget(QRadioButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setWindowTitle("BDA Resizer")
        self.resize(720, 480)

        self.tableWidget = TableWidget(parent=self)
        # self.settingsWidget = SettingsWidget(parent=self)



def main():
    app = QApplication(sys.argv)
    ui = MainWidget()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()