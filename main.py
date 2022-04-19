import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from orig import Ui_MainWindow
from manage_db import *
from record import Record


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
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.setFont(font)
        self.textQVBoxLayout = QtWidgets.QVBoxLayout()
        self.textUpQLabel = QtWidgets.QLabel()
        self.textDownQLabel = QtWidgets.QLabel()
        self.textTags = QtWidgets.QHBoxLayout()
        self.textSource = QtWidgets.QLabel()
        self.textDate = QtWidgets.QLabel()
        self.entryData = QtWidgets.QHBoxLayout()
        self.entryData.addWidget(self.textUpQLabel)
        self.entryData.addWidget(self.textSource)
        self.entryData.addWidget(self.textDate)
        self.textQVBoxLayout.addLayout(self.entryData)
        self.textQVBoxLayout.addLayout(self.textTags)
        self.allQHBoxLayout = QtWidgets.QHBoxLayout()
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout)
        self.labl = QtWidgets.QLabel(self)
        self.setLayout(self.allQHBoxLayout)
        self.setStyleSheet("background: #5E5EEC;\n"
                           "border-radius: 15px;")

    def setTextUp(self, text):
        self.textUpQLabel.setText(text)

    def setTextSource(self, text):
        self.textSource.setText(str(text))

    def setTextDate(self, text):
        self.textDate.setText(text)

    def setTextTags(self, tags):
        for tag_text in tags:
            self.labl = QtWidgets.QLabel(self)
            self.labl.setStyleSheet("background: #A2A2E8;\n"
"border-radius: 10px;")
            self.labl.setMinimumWidth(30)
            self.labl.setContentsMargins(2, 2, 2, 2)
            self.labl.setAlignment(QtCore.Qt.AlignCenter)
            self.labl.setText(tag_text[1])
            self.textTags.addWidget(self.labl)
        if not tags:
            labl = QtWidgets.QLabel()
            labl.setText(" ")
            self.textTags.addWidget(labl)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.textTags.addItem(spacerItem1)


class BindedRecordWidget(RecordWidget):
    def __init__(self, reid):
        super(BindedRecordWidget, self).__init__()
        self.ui = RecordWidget()
        self.data = Record.from_database(reid)
        self.data.set_tags()
        self.setTextUp(self.data.theme)
        self.setTextSource(self.data.source)
        self.setTextDate(self.data.date)
        self.setTextTags(self.data.tags)


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.stack = QtWidgets.QStackedWidget()
        self.rows = load_table("RESOURCES")
        self.view = QtWidgets.QListWidget()
        self.view.setSpacing(5)
        self.view.setBaseSize(self.ui.centralLayout.sizeHint())
        for row in self.rows:
            self.wid = BindedRecordWidget(row[0])
            self.item = QtWidgets.QListWidgetItem(self.view)
            self.item.setSizeHint(self.wid.sizeHint())
            self.view.addItem(self.item)
            self.view.setItemWidget(self.item, self.wid)
        self.ui.centralLayout.addWidget(self.view)
        self.ui.centralLayout.addStretch()
        self.themes = load_table("THEMES")
        self.themes_view = QtWidgets.QListWidget()
        for theme in self.themes:
            wid = ThemeWidget()
            wid.setThemeName(theme[1])
            item = QtWidgets.QListWidgetItem(self.themes_view)
            item.setSizeHint(self.wid.sizeHint())
            self.themes_view.addItem(item)
            self.themes_view.setItemWidget(item, wid)
        self.ui.themesLayout.addWidget(self.themes_view)

 
def main():
    app = QtWidgets.QApplication([])
    application = Window()
    application.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()