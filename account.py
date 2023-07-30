class Account:
    def __init__(self, full_name, gender: bool, username, password) -> None:
        self._full_name = full_name
        self._gender = gender
        self._username = username
        self._password = password

    def get_full_name(self):
        return self._full_name

    def get_gender(self):
        return self._gender

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def set_full_name(self, name):
        self._full_name = name

    def set_gender(self, gender: bool):
        self._gender = gender

    def set_username(self, username):
        self._username = username

    def set_password(self, password):
        self._password = password


