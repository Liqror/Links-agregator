from datetime import datetime
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from passlib.hash import pbkdf2_sha256
from orig import Ui_MainWindow
from reg import Ui_MainWindow as Ui_StartWindow
from user import cur_user
from config import config
from manage_db import *
from widgets import ThemeWidget, BindedRecordWidget, reconnect


def show_error(text):
    """Shows popup error window"""
    err = QtWidgets.QMessageBox()
    err.setIcon(QtWidgets.QMessageBox.Warning)
    err.setText("Ошибка ввода")
    err.setInformativeText(text)
    err.setWindowTitle("Предупреждение")
    err.exec_()


class Window(QtWidgets.QMainWindow):
    '''
    Главное окно.

    Аттрибуты:
    view: список записей;
    themes_view: список тем;
    all_records_shown: булево значение, показывающее, должны ли сейчас отображаться все записи или избранные (тема, поиск);
    cur_theme: заголовок, сообщающий, откуда показываются записи (все, из темы, результаты поиска);
    datas: данные последней открытой записи, используются для обновления данных;


    Методы:
    show_records: показать список определённых записей аккаунта;
    show_all_records: показать список всех записей аккаунта;
    show_themes: показать список всех тем аккаунта;
    add_theme_frame: показать поле добавления темы;
    add_new_theme: добавить тему;
    hide_add_theme: спрятать поле добавления темы;
    theme_clicked: показать записи в теме при нажатии на неё;
    refresh_theme_combobox: обновить список доступных при сохранении записи тем;
    item_clicked: показать подробную информацию о записи;
    update_record: обновить данные записи;
    apply_search: выполнить поиск;
    clear_search: очистить поля поиска;
    go_back: вернуться на главную;
    save_new_record: сохранить новую запись;
    new_record: перейти к созданию записи;
    back_from_theme: вернуться к списку всех записей;
    exit_account: выйти из аккаунта;
    '''
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(config.app_name)
        self.view = QtWidgets.QListWidget()
        self.view.setSpacing(5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.view.setStyleSheet("font-family: Arial; font-style: normal; font-size: 15pt;")
        self.show_all_records(cur_user.active)
        self.all_records_shown = True
        self.cur_theme = config.library_name
        self.datas = None
        self.view.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.ui.stackedWidget.insertWidget(0, self.view)
        self.ui.stackedWidget.insertWidget(1, self.ui.widget)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.themes_view = QtWidgets.QListWidget()
        self.show_themes(cur_user.active)
        self.ui.deleteButton.hide()
        self.ui.label.hide()
        self.ui.addThemeFrame.hide()
        self.types_button = {"link": self.ui.linkButton, "doc": self.ui.dockButton, "image": self.ui.imgButton}
        self.types_search = {"Тип ресурса": None, "Ссылка": "link", "Документ": "doc", "Изображение": "image"}
        self.ui.userName.setText(get_active_user_name())
        cur_user.register_callback(lambda user: self.ui.userName.setText(get_user_name(user)))
        self.ui.themesLayout.addWidget(self.themes_view)
        self.view.itemClicked.connect(self.item_clicked)
        self.themes_view.itemClicked.connect(self.theme_clicked)
        self.ui.newLinkButton.clicked.connect(self.new_record)
        self.ui.exitAccButton.clicked.connect(self.exit_account)
        self.ui.plus.clicked.connect(self.add_theme_frame)
        self.ui.label.clicked.connect(self.back_from_theme)
        self.ui.applyButton.clicked.connect(self.apply_search)
        self.ui.pushButton.clicked.connect(self.clear_search)
        self.ui.backPushButton.clicked.connect(self.go_back)
        self.ui.cancelThemeButton.clicked.connect(self.hide_add_theme)
        self.ui.saveThemeButton.clicked.connect(self.add_new_theme)
        self.ui.descriptionTextEdit.setAcceptDrops(True)
        self.ui.linkLineEdit.setAcceptDrops(True)
        self.ui.deleteButton.clicked.connect(self.delete_item)

    def show_records(self, rows):
        self.view.clear()
        self.ui.nameOfLayout.setText(self.cur_theme)
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
        for row in rows:
            widg = BindedRecordWidget(row[0])
            item = QtWidgets.QListWidgetItem(self.view)
            item.setSizeHint(widg.sizeHint())
            item.setData(QtCore.Qt.UserRole, widg.datas)
            self.view.addItem(item)
            self.view.setItemWidget(item, widg)

    def show_all_records(self, user):
        self.cur_theme = config.library_name
        self.all_records_shown = True
        rows = load_user_records(user)
        self.show_records(rows)

    def show_themes(self, user):
        self.themes_view.clear()
        themes = load_user_themes(user)
        self.themes_view.setStyleSheet("""
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
        for theme in themes:
            wid = ThemeWidget()
            wid.setThemeName(theme[2])
            item = QtWidgets.QListWidgetItem(self.themes_view)
            item.setSizeHint(wid.sizeHint())
            item.setData(QtCore.Qt.UserRole, theme)
            self.themes_view.addItem(item)
            self.themes_view.setItemWidget(item, wid)

    def add_theme_frame(self):
        self.ui.addThemeFrame.show()
    
    def add_new_theme(self):
        theme = self.ui.lineEdit.text()
        add_theme(cur_user.active, theme)
        self.show_themes(cur_user.active)
        self.refresh_theme_combobox()

    def hide_add_theme(self):
        self.ui.addThemeFrame.hide()

    def theme_clicked(self):
        cur_row = self.themes_view.currentRow()
        theme_data = self.themes_view.item(cur_row).data(QtCore.Qt.UserRole)
        self.cur_theme = theme_data[2]
        rows = load_theme_records(theme_data[0])
        self.show_records(rows)
        self.ui.label.show()
        self.all_records_shown = False

    def refresh_theme_combobox(self):
        self.ui.themeComboBox.clear()
        themes = [theme[2] for theme in load_user_themes(cur_user.active)]
        self.ui.themeComboBox.addItems(themes)

    def item_clicked(self):
        self.ui.label.hide()
        self.ui.deleteButton.show()
        cur_row = self.view.currentRow()
        self.datas = self.view.item(cur_row).data(QtCore.Qt.UserRole)
        self.types_button[self.datas.type].setChecked(True)
        self.refresh_theme_combobox()
        self.ui.themeComboBox.setCurrentText(self.datas.theme)
        self.ui.linkLineEdit.setText(self.datas.path)
        self.ui.descriptionTextEdit.setText(self.datas.description)
        self.ui.nameOfLayout.setText(self.datas.date)
        tags = ""
        for tag in self.datas.tags:
            tags = tags + tag[1] + " "
        self.ui.tagsLineEdit.setText(tags)
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.savePushButton.clicked.connect(self.update_record)

    def go_back(self):
        self.ui.deleteButton.hide()
        if not self.all_records_shown:
            self.ui.label.show()
        self.ui.nameOfLayout.setText(self.cur_theme)
        self.ui.stackedWidget.setCurrentIndex(0)
        for type_button in self.types_button.values():
            type_button.setChecked(False)
        self.ui.themeComboBox.clear()
        self.ui.linkLineEdit.clear()
        self.ui.descriptionTextEdit.clear()
        self.ui.tagsLineEdit.clear()
        reconnect(self.ui.savePushButton, None, None)

    def save_new_record(self):
        path = self.ui.linkLineEdit.text()
        description = self.ui.descriptionTextEdit.toPlainText()
        theme = get_theme_id(cur_user.active, self.ui.themeComboBox.currentText())
        tags = self.ui.tagsLineEdit.text().split()
        for res, button in self.types_button.items():
            if button.isChecked():
                res_type = res
        seps = [".", "://", ":/", ":\\",  "|", "/", ":", "\\", " "]
        source_path = path
        for sep in seps[1:]:
            source_path = source_path.replace(sep, seps[0])
        #TODO: проверить, что ссылка path валидна (файл существует на компьютере, ссылка может куда-то вести в интернете)
        #Если нет, то вывести сообщение об ошибке и выйти из функции
        #Если да, то следующие четыре строки кода (выделить источник, добавить запись, вернуться к списку записей)
        source_p = source_path.split(seps[0])
        try:
            add_record(res_type, path, description, theme, source_p[1], tags)
        except (UnboundLocalError, IndexError):
            show_error("Убедитесь, что вы выбрали тип ресурса и верно заполнили поле для ссылки.")
        else:
            self.show_all_records(cur_user.active)
            self.go_back()

    def new_record(self):
        self.ui.label.hide()
        self.refresh_theme_combobox()
        if not self.all_records_shown:
            self.ui.themeComboBox.setCurrentText(self.ui.nameOfLayout.text())
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.savePushButton.clicked.connect(self.save_new_record)

    def update_record(self):
        old_tags = [old_tag[1] for old_tag in self.datas.tags]
        res_id = self.datas.id
        path = self.ui.linkLineEdit.text()
        description = self.ui.descriptionTextEdit.toPlainText()
        theme = get_theme_id(cur_user.active, self.ui.themeComboBox.currentText())
        tags = self.ui.tagsLineEdit.text().split()
        for res, button in self.types_button.items():
            if button.isChecked():
                res_type = res
                break
        seps = [".", "://", ":/", ":\\",  "|", "/", ":", "\\", " "]
        source_path = path
        for sep in seps[1:]:
            source_path = source_path.replace(sep, seps[0])
        #TODO: проверить, что ссылка path валидна (файл существует на компьютере, ссылка может куда-то вести в интернете)
        #Если нет, то вывести сообщение об ошибке и выйти из функции
        #Если да, то следующие четыре строки кода (выделить источник, обновить запись, вернуться к списку записей)
        source_p = source_path.split(seps[0])
        try:
            update_record(res_id, res_type, path, description, theme, source_p[1], old_tags, tags)
        except (UnboundLocalError, IndexError):
            show_error("Убедитесь, что вы выбрали тип ресурса и верно заполнили поле для ссылки.")
        else:
            self.show_all_records(cur_user.active)
            self.go_back()

    def delete_item(self):
        delete_record(self.datas.id)
        self.show_all_records(cur_user.active)
        self.go_back()

    def apply_search(self):
        res_type = self.types_search[self.ui.resourceType.currentText()]
        theme = self.ui.themeSearch.text()
        tags = get_tags_id(self.ui.tagSearch.text().split())
        desc = self.ui.descriptionSearch.text()
        source = self.ui.sourceSearch.text()
        res_date = datetime.strptime(self.ui.dateSearch.text(), "%d.%m.%Y").strftime("%Y-%m-%d")
        if not theme: theme = None
        else: theme = get_theme_id(cur_user.active, theme)
        if not desc: desc = None
        if not source: source = None
        if res_date == "2000-01-01": res_date = None
        rows = search(cur_user.active, res_type, theme, desc, source, res_date, tags)
        self.cur_theme = config.search_name
        self.show_records(rows)

    def clear_search(self):
        self.ui.resourceType.setCurrentIndex(0)
        self.ui.themeSearch.clear()
        self.ui.tagSearch.clear()
        self.ui.descriptionSearch.clear()
        self.ui.sourceSearch.clear()
        qdate = QtCore.QDate.fromString("01.01.2000", "dd.MM.yyyy")
        self.ui.dateSearch.setDate(qdate)
        self.show_all_records(cur_user.active)

    def back_from_theme(self):
        self.ui.label.hide()
        self.show_all_records(cur_user.active)
        self.ui.nameOfLayout.setText(config.library_name)

    def pictureDropped(self, l):
        for url in l:
            if os.path.exists(url):
                self.ui.linkLineEdit.setText(url)

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
        self.ui.signUpButton.clicked.connect(self.register)
        self.ui.pushButton.clicked.connect(self.go_back)

    def registration_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.clear_login_page()

    def show_signup_error(self):
        self.ui.messageLabel_2.setText("Для успешной регистрации ваш пароль должен содержать от 4 до 16 символов и быть одинаковым в обоих полях. " +
            "Почтовый адрес должен быть похожим на реальный и не должен быть уже зарегистрированным в системе.")

    def show_login_error(self):
        self.ui.messageLabel.setText("Неверный логин или пароль.")

    def clear_registration_page(self):
        self.ui.emailLineEditReg.clear()
        self.ui.nameLineEdit.clear()
        self.ui.passwordLineEditReg.clear()
        self.ui.passwordCheckReg.clear()
        self.ui.messageLabel_2.clear()

    def clear_login_page(self):
        self.ui.emailLineEdit.clear()
        self.ui.passwordLineEdit.clear()
        self.ui.messageLabel.clear()

    def go_back(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.clear_registration_page()

    def enter(self):
        email = self.ui.emailLineEdit.text()
        password = self.ui.passwordLineEdit.text()
        user = get_user_by_email(email)
        orig_hash = get_pass_hash(user)
        try:
            pbkdf2_sha256.verify(password, orig_hash)
        except ValueError:
            self.show_login_error()
        else:
            if pbkdf2_sha256.verify(password, orig_hash): 
                cur_user.set_user(user)
                self.clear_login_page()
            else: self.show_login_error()

    def register(self):
        name = self.ui.nameLineEdit.text()
        email = self.ui.emailLineEditReg.text()
        password = self.ui.passwordLineEditReg.text()
        password_check = self.ui.passwordCheckReg.text()

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

        if password == password_check and 4 <= len(password) <= 16 and check_email == 1 and get_user_by_email(email) == 0:
            pass_hash = pbkdf2_sha256.hash(password)
            user = add_user(name, email, pass_hash)
            cur_user.set_user(user)
        else:
            self.show_signup_error()
            self.ui.emailLineEditReg.clear()
            self.ui.nameLineEdit.clear()
            self.ui.passwordLineEditReg.clear()
            self.ui.passwordCheckReg.clear()
