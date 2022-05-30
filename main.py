import sys
from PyQt5 import QtWidgets
from user import cur_user
from gui import Window, StartWindow
from manage_db import set_active_user, get_active_user


def open_main(user, application, login):
    if user != 0:
        login.close()
        application.show()
    else:
        application.close()
        login.show()


cur_user.register_callback(set_active_user)


def main():
    cur_user.active = get_active_user()
    app = QtWidgets.QApplication([])
    application = Window()
    login = StartWindow()
    cur_user.register_callback(application.show_all_records)
    cur_user.register_callback(application.show_themes)
    cur_user.register_callback(lambda user: open_main(user, application, login))
    if cur_user.active == 0:
        login.show()
    else:
        application.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()