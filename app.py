import sys
from PyQt5.QtWidgets import * 

class TableWidget(QTableWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

        self.setRowCount(4)
        self.setColumnCount(2)
        self.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
        self.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
        self.setItem(1,0, QTableWidgetItem("Cell (2,1)"))
        self.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
        self.setItem(2,0, QTableWidgetItem("Cell (3,1)"))
        self.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
        self.setItem(3,0, QTableWidgetItem("Cell (4,1)"))
        self.setItem(3,1, QTableWidgetItem("Cell (4,2)"))
        self.move(0,0)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            print(f)

class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BDA Resizer")
        self.resize(720, 480)
        self.tableWidget = TableWidget()
        self.setCentralWidget(self.tableWidget)


    def _createList(self):
        self.listWidget = QListWidget(self)
        self.listWidget.addItem(QListWidgetItem("First Item"))
        self.listWidget.addItem(QListWidgetItem("Second Item"))
        self.listWidget.addItem(QListWidgetItem("Third Item"))


def main():
    app = QApplication(sys.argv)
    ui = MainWidget()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()