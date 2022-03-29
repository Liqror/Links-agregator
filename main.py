import sys
from PyQt5 import QtWidgets
from orig import Ui_MainWindow
from manage_db import *


class ThemeWidget(QtWidgets.QFrame):
    def __init__(self, parent = None):
        super(ThemeWidget, self).__init__(parent)
        self.setStyleSheet("border: 1px solid #5E5EEC; \n"
                           "border-color: #5E5EEC;\n"
                           "color: rgb(255, 255, 255);")
        self.textQHBox = QtWidgets.QHBoxLayout()
        self.textTheme = QtWidgets.QLabel()
        self.textQHBox.addWidget(self.textTheme)
        self.setLayout(self.textQHBox)

    def setThemeName(self, text):
        self.textTheme.setText(str(text))


class RecordWidget(QtWidgets.QFrame):
    def __init__ (self, parent = None):
        super(RecordWidget, self).__init__(parent)
        self.setStyleSheet("background: #5E5EEC;\n"
                           "border-radius: 20px;")
        self.textQVBoxLayout = QtWidgets.QVBoxLayout()
        self.textUpQLabel = QtWidgets.QLabel()
        self.textDownQLabel = QtWidgets.QLabel()
        self.textSource = QtWidgets.QLabel()
        self.textDate = QtWidgets.QLabel()
        self.entryData = QtWidgets.QHBoxLayout()
        self.entryData.addWidget(self.textUpQLabel)
        self.entryData.addWidget(self.textSource)
        self.entryData.addWidget(self.textDate)
        self.textQVBoxLayout.addLayout(self.entryData)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)
        self.allQHBoxLayout = QtWidgets.QHBoxLayout()
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout)
        self.textUpQLabel.setStyleSheet('color: rgb(0, 0, 255)')
        self.textDownQLabel.setStyleSheet('color: rgb(255, 0, 0);')
        self.setLayout(self.allQHBoxLayout)

    def setTextUp(self, text):
        self.textUpQLabel.setText(str(text))

    def setTextDown(self, text):
        self.textDownQLabel.setText(text)

    def setTextSource(self, text):
        self.textSource.setText(str(text))

    def setTextDate(self, text):
        self.textDate.setText(text)


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.rows = load_table("RESOURCES")
        self.view = QtWidgets.QListWidget(self.ui.libraryView)
        self.view.setSpacing(5)
        for row in self.rows:
            self.wid = RecordWidget()
            self.wid.setTextUp(row[4])
            self.wid.setTextSource(row[5])
            self.wid.setTextDate(row[6])
            self.wid.setTextDown(row[3])
            self.item = QtWidgets.QListWidgetItem(self.view)
            self.item.setSizeHint(self.wid.sizeHint())
            self.view.addItem(self.item)
            self.view.setItemWidget(self.item, self.wid)

 
def main():
    app = QtWidgets.QApplication([])
    application = Window()
    application.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()