import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from orig import Ui_MainWindow
from reg import Ui_MainWindow as Ui_StartWindow
from user import cur_user
from config import config
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
        self.datas = Record.from_database(reid)
        self.datas.set_tags()
        self.setTextUp(self.datas.theme)
        self.setTextSource(self.datas.source)
        self.setTextDate(self.datas.date)
        self.setTextTags(self.datas.tags)


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(config.app_name)
        self.view = QtWidgets.QListWidget()
        self.view.setSpacing(5)
        self.show_records(cur_user.active)
        self.view.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.ui.stackedWidget.insertWidget(0, self.view)
        self.ui.stackedWidget.insertWidget(1, self.ui.widget)
        self.ui.stackedWidget.insertWidget(2, self.ui.creationWidget)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.themes_view = QtWidgets.QListWidget()
        self.show_themes(cur_user.active)
        self.ui.label.hide()
        self.ui.themesLayout.addWidget(self.themes_view)
        self.view.itemClicked.connect(self.item_clicked)
        self.ui.newLinkButton.clicked.connect(self.new_record)

    def show_records(self, user):
        self.view.clear()
        rows = load_user_records(user)
        for row in rows:
            widg = BindedRecordWidget(row[0])
            item = QtWidgets.QListWidgetItem(self.view)
            item.setSizeHint(widg.sizeHint())
            item.setData(QtCore.Qt.UserRole, widg.datas)
            self.view.addItem(item)
            self.view.setItemWidget(item, widg)

    def show_themes(self, user):
        self.themes_view.clear()
        themes = load_user_themes(user)
        for theme in themes:
            wid = ThemeWidget()
            wid.setThemeName(theme[2])
            item = QtWidgets.QListWidgetItem(self.themes_view)
            item.setSizeHint(wid.sizeHint())
            self.themes_view.addItem(item)
            self.themes_view.setItemWidget(item, wid)


    def item_clicked(self):
        datas = self.view.item(0).data(QtCore.Qt.UserRole)
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.backPushButton.clicked.connect(self.go_back)

    def go_back(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def new_record(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.cancelPushButton.clicked.connect(self.go_back)


class startWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(startWindow, self).__init__()
        self.ui = Ui_StartWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(config.app_name)
        self.ui.registrationPushButton.clicked.connect(self.registration_page)
        self.ui.entrancePushButton.clicked.connect(self.enter)
        self.ui.registrationPushButton_2.clicked.connect(self.register)

    def registration_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def enter(self):
        email = self.ui.emailLineEdit.text()
        password = self.ui.passwordLineEdit.text()
        user = match_user(email, password)
        if user:
            cur_user.set_user(user)

    def register(self):
        name = self.ui.nameLineEdit.text()
        email = self.ui.emailLineEdit_2.text()
        password = self.ui.passwordLineEdit_2.text()
        password_check = self.ui.password2LineEdit.text()

        # ПРОВЕРКА ПОЧТЫ НА ВАЛИДНОСТЬ
        check_email = 0
        count, place, Count_for_letter_1, Count_for_letter_2 = 0, 0, 0, 0
        for i in range(0, len(email)):
            if email[i] == '@':
                count += 1
                place = i
        error = 0
        if count == 1:
            for i in range(0, len(email)):
                if (not ('a' <= email[i] <= 'z')) and (email[i] != '.' and email[i] != '@'):
                    error += 1
                    break
                else:
                    if i < place:
                        Count_for_letter_1 += 1
                        if ((email[i] == '.' or email[i] == '-') and (
                                email[i] == email[i + 1] or i == 0 or i == (place - 1))) and (
                                not ('a' <= email[i] <= 'z')):
                            error += 1
                    if i > place:
                        Count_for_letter_2 += 1
                        if ((not ('a' <= email[i] <= 'z')) and ((email[i] == '.' or email[i] == '-') and (
                                email[i] == email[i + 1] or i == place or i == (place + 1)))):
                            error += 1
        if Count_for_letter_1 != 0 and Count_for_letter_2 != 0 and error == 0:
            check_email = 1

        if password == password_check and 4 <= len(password) <= 16 and check_email == 1:
            user = add_user(name, email, password)
            cur_user.set_user(user)

def open_main(user, application, login):
    if user != 0:
        login.close()
        application.show()

def update_user(user):
    set_active_user(user)

cur_user.register_callback(set_active_user)

def main():
    cur_user.active = get_active_user()
    app = QtWidgets.QApplication([])
    application = Window()
    login = startWindow()
    cur_user.register_callback(application.show_records)
    cur_user.register_callback(application.show_themes)
    cur_user.register_callback(lambda user: open_main(user, application, login))
    if cur_user.active == 0:
        login.show()
    else:
        application.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()