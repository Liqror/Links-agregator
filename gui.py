from PyQt5 import QtWidgets, QtCore
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
        self.ui.stackedWidget.insertWidget(2, self.ui.creationWidget)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.themes_view = QtWidgets.QListWidget()
        self.show_themes(cur_user.active)
        self.ui.label.hide()
        self.ui.userName.setText(get_active_user_name())
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
        cur_row = self.view.currentRow()
        themes = [theme[2] for theme in load_user_themes(cur_user.active)]
        datas = self.view.item(cur_row).data(QtCore.Qt.UserRole)
        self.ui.themeComboBox.addItems(themes)
        self.ui.themeComboBox.setCurrentText(datas.theme)
        self.ui.linkLineEdit.setText(datas.path)
        self.ui.descriptionTextEdit.setText(datas.description)
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.backPushButton.clicked.connect(self.go_back)

    def go_back(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def new_record(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.cancelPushButton.clicked.connect(self.go_back)


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
