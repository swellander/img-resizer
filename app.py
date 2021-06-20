import sys
from PyQt5.QtWidgets import * 




class SettingsWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.maxHeightField = QLineEdit()


# class MainWidget(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("BDA Resizer")
#         self.resize(720, 480)

#         layout = QGridLayout()
#         layout.addWidget(TableWidget())
#         layout.addWidget(QPushButton("Select", parent=self))



# def main():
#     app = QApplication(sys.argv)
#     ui = MainWidget()
#     ui.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()


class TableWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.files = []
        # self.setAcceptDrops(True)
        # self.setGeometry(20, 20, 600, 200)
        # self.setColumnCount(4)
        # self.setHorizontalHeaderLabels(["Filename", "Dimensions", "Size", "New Dimensions"])

        # item = QTableWidgetItem("/first/file/path.txt")
        # print(item)
        # self.setItem(1, 1, item)

    # def dragEnterEvent(self, event):
    #     if event.mimeData().hasUrls():
    #         print("Acceptable files")
    #         event.accept()
    #     else:
    #         print(f'Ignoring file: {event}')
    #         event.ignore()

    # def dropEvent(self, event):
    #     print("DROPPING")
    #     files = [u.toLocalFile() for u in event.mimeData().urls()]

    def setFiles(self, files=[]):
        for f in files:
            self.addItem(f)



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BDA Image Resizer")
        self.resize(720, 480)

        self.fileTable = TableWidget()

        self.selectImagesBtn = QPushButton("Select Images") 
        self.selectImagesBtn.clicked.connect(self.selectImages)

        self.maxHeightField = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.fileTable)
        layout.addWidget(self.selectImagesBtn)
        layout.addWidget(self.maxHeightField)
        self.setLayout(layout)
    
    def selectImages(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Pick some goodies")
        self.fileTable.setFiles(files)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
