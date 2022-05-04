class User():
    '''Класс для отслеживания активного пользовательского аккаунта'''
    def __init__(self):
        self._active = 0
        self._callbacks = []

    def set_user(self, user):
        self.active = user
    
    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, new_value):
        self._active = new_value
        self._notify(new_value)

    def _notify(self, new_value):
        for callback in self._callbacks:
            callback(new_value)

    def register_callback(self, callback):
        self._callbacks.append(callback)


cur_user = User()
