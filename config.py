class Config():
    def __init__(self):
        self.app_name = "Агрегатор ссылок"
        self.dbase = "source.db"
        self.active_user = 0

    def set_user(self, user):
        self.active_user = user

config = Config()
