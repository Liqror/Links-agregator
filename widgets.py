from datetime import datetime
from PyQt5 import QtWidgets, QtGui, QtCore
from record import Record
from manage_db import delete_theme, check_if_theme_empty


class ThemeWidget(QtWidgets.QFrame):
    '''Виджет темы в списке'''
    def __init__(self, theme_id, theme_name, parent = None):
        super(ThemeWidget, self).__init__(parent)
        self.setStyleSheet("border: 1px solid #5E5EEC; \n"
                           "border-color: #5E5EEC;\n"
                           "color: rgb(255, 255, 255);")
        self.textQHBox = QtWidgets.QHBoxLayout()
        self.textTheme = QtWidgets.QLabel()
        self.textQHBox.addWidget(self.textTheme)
        self.setLayout(self.textQHBox)
        self.id = theme_id
        self.name = theme_name
        self.deleteTheme = QtWidgets.QAction("Удалить", self)
        self.deleteTheme.triggered.connect(self.delete_item)
        self.setThemeName(self.name)

    #def contextMenuEvent(self, event):
        #menu = QtWidgets.QMenu(self)
        #menu.addAction(self.deleteTheme)
        #if check_if_theme_empty(self.id):
        #   self.deleteTheme.setEnabled(False)
        #menu.exec(event.globalPos())

    def setThemeName(self, text):
        self.textTheme.setText(text)

    def delete_item(self):
        delete_theme(self.id)


class RecordWidget(QtWidgets.QFrame):
    '''Виджет записи в списке'''
    def __init__ (self, parent = None):
        super(RecordWidget, self).__init__(parent)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.setFont(font)
        self.textQVBoxLayout = QtWidgets.QVBoxLayout()
        self.textUpQLabel = QtWidgets.QLabel()
        self.textTags = QtWidgets.QHBoxLayout()
        self.textSource = QtWidgets.QLabel()
        self.textDate = QtWidgets.QLabel()
        self.entryData = QtWidgets.QHBoxLayout()
        self.entryData.addWidget(self.textUpQLabel)
        self.entryData.addWidget(self.textSource)
        self.entryData.addWidget(self.textDate)
        self.deskLab = QtWidgets.QLineEdit()
        self.deskLab.setEnabled(False)
        self.deskLab.setStyleSheet("color: black")
        for lab in self.deskLab, self.textUpQLabel, self.textSource, self.textDate:
            lab.setFont(self.font())
        font.setPointSize(10)
        self.deskLab.setFont(font)
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
        self.deskLab.setCursorPosition(0)

    def setTextTags(self, tags):
        for tag_text in tags:
            self.labl = QtWidgets.QLabel(self)
            self.labl.setStyleSheet("background: #A2A2E8;\n"
"border-radius: 10px;")
            self.labl.setMinimumWidth(30)
            self.labl.setContentsMargins(2, 2, 2, 2)
            self.labl.setAlignment(QtCore.Qt.AlignCenter)
            self.labl.setText(tag_text[1])
            self.labl.setFont(self.font())
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
        self.datas.date = datetime.strptime(self.datas.date, "%Y-%m-%d %H:%M:%S").strftime("%d.%m.%Y %H:%M")
        self.datas.set_tags()
        self.setTextUp(self.datas.theme)
        self.setTextSource(self.datas.source)
        self.setTextDate(self.datas.date)
        self.setTextDescription(self.datas.description)
        self.setTextTags(self.datas.tags)


def reconnect(signal, newhandler=None, oldhandler=None):        
    try:
        if oldhandler is not None:
            while True:
                signal.disconnect(oldhandler)
        else:
            signal.disconnect()
    except TypeError:
        pass
    if newhandler is not None:
        signal.connect(newhandler)
