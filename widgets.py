from PyQt5 import QtWidgets, QtGui, QtCore
from record import Record


class ThemeWidget(QtWidgets.QFrame):
    '''Виджет темы'''
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
    '''Виджет записи'''
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
        self.deskLab = QtWidgets.QLabel()
        self.deskLab.setWordWrap(True)
        self.textQVBoxLayout.addLayout(self.entryData)
        self.textQVBoxLayout.addWidget(self.deskLab)
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

    def setTextDescription(self, text):
        self.deskLab.setText(text)

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
    '''Виджет записи, связанный с базой данных'''
    def __init__(self, reid):
        super(BindedRecordWidget, self).__init__()
        self.ui = RecordWidget()
        self.datas = Record.from_database(reid)
        self.datas.set_tags()
        self.setTextUp(self.datas.theme)
        self.setTextSource(self.datas.source)
        self.setTextDate(self.datas.date)
        self.setTextDescription(self.datas.description)
        self.setTextTags(self.datas.tags)


class TagsHolder(QtWidgets.QLineEdit):
     def __init__(self, parent = None):
        super(TagsHolder, self).__init__(parent)
        self.label = QtWidgets.QLabel()
