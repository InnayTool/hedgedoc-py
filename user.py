from jsonserialize import JSONSerializable


class EmailLogin(JSONSerializable):
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password


class LdapLogin(JSONSerializable):
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password


class OpenIdLogin(JSONSerializable):
    def __init__(self, openId: str):
        self.openId = openId


class UserInfo(JSONSerializable):
    def __init__(self, username: str, displayName: str, photo: str, email: str):
        self.username = username
        self.displayName = displayName
        self.photo = photo
        self.email = email


class UserPasswordChange(JSONSerializable):
    def __init__(self, password: str):
        self.password = password
