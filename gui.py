from posixpath import split
from sys import set_asyncgen_hooks
from PyQt5 import QtWidgets, QtCore
from sympy import source
from orig import Ui_MainWindow
from reg import Ui_MainWindow as Ui_StartWindow
from user import cur_user
from config import config
from manage_db import *
from widgets import ThemeWidget, BindedRecordWidget


class Window(QtWidgets.QMainWindow):
    '''
    Главное окно:

    Аттрибуты:
    view: список записей;
    themes_view: список тем;

    Методы:
    show_records: показать список всех записей аккаунта;
    show_themes: показать список всех тем аккаунта;
    item_clicked: показать подробную информацию о записи;
    go_back: вернуться на главную;
    new_record: перейти к созданию записи;
    '''
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
        self.ui.stackedWidget.setCurrentIndex(0)
        self.themes_view = QtWidgets.QListWidget()
        self.show_themes(cur_user.active)
        self.ui.label.hide()
        self.types_button = {"link": self.ui.linkButton, "doc": self.ui.dockButton, "image": self.ui.imgButton}
        self.ui.userName.setText(get_active_user_name())
        self.ui.themesLayout.addWidget(self.themes_view)
        self.view.itemClicked.connect(self.item_clicked)
        self.ui.newLinkButton.clicked.connect(self.new_record)
        self.ui.exitAccButton.clicked.connect(self.exit_account)

    def show_records(self, user):
        self.view.clear()
        self.view.setStyleSheet("""
        QScrollBar:vertical {
            border-radius:5px;
            background: #A2A2E8;
            width:7px;
            margin: 0px 0px 0px 0px;
        }
        QScrollBar::handle:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0  rgb(42, 42, 68), stop: 0.5  rgb(42, 42, 68), stop:1  rgb(42, 42, 68));
            min-height: 0px;
        }
        QScrollBar::add-line:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0  rgb(42, 42, 68), stop: 0.5  rgb(42, 42, 68), stop:1  rgb(42, 42, 68));
            height: 0px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }
        QScrollBar::sub-line:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0  rgb(42, 42, 68), stop: 0.5  rgb(42, 42, 68), stop:1  rgb(42, 42, 68));
            height: 0 px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }
        """)
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
        cur_row = self.view.currentRow()
        themes = [theme[2] for theme in load_user_themes(cur_user.active)]
        datas = self.view.item(cur_row).data(QtCore.Qt.UserRole)
        self.types_button[datas.type].setChecked(True)
        self.ui.themeComboBox.addItems(themes)
        self.ui.themeComboBox.setCurrentText(datas.theme)
        self.ui.linkLineEdit.setText(datas.path)
        self.ui.descriptionTextEdit.setText(datas.description)
        tags = ""
        for tag in datas.tags:
            tags = tags + tag[1] + " "
        self.ui.tagsLineEdit.setText(tags)
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.backPushButton.clicked.connect(self.go_back)

    def go_back(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def save_new_record(self):
        path = self.ui.linkLineEdit.text()
        description = self.ui.descriptionTextEdit.toPlainText()
        theme = get_theme_id(cur_user.active, self.ui.themeComboBox.currentText())
        tags = self.ui.tagsLineEdit.text().split()
        for res, button in self.types_button.items():
            if button.isChecked():
                res_type = res
        source_path = path.split(sep="/")[0]
        add_record(res_type, path, description, theme, source_path, tags)
        self.show_records(cur_user.active)
        self.go_back()

    def new_record(self):
        self.ui.themeComboBox.clear()
        for type_button in self.types_button.values():
            type_button.setChecked(False)
        themes = [theme[2] for theme in load_user_themes(cur_user.active)]
        self.ui.themeComboBox.addItems(themes)
        self.ui.linkLineEdit.clear()
        self.ui.descriptionTextEdit.clear()
        self.ui.tagsLineEdit.clear()
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.backPushButton.clicked.connect(self.go_back)
        self.ui.savePushButton.clicked.connect(self.save_new_record)

    def exit_account(self):
        cur_user.set_user(0)
        self.ui.stackedWidget.setCurrentIndex(0)


class StartWindow(QtWidgets.QMainWindow):
    '''
    Окно входа и регистрации

    Методы:
    registration_page: перейти к странице регистрации;
    enter: войти в аккаунт;
    register: зарегистрировать аккаунт
    '''
    def __init__(self) -> None:
        super(StartWindow, self).__init__()
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
            self.ui.emailLineEdit.clear()
            self.ui.passwordLineEdit.clear()

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
