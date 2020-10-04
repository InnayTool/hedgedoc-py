from jsonserialize import JSONSerializable
from note import History, HistoryObject, HistoryUpdateObject, get_metadata_from_json

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


def get_user_info_from_json(user_info_json: dict):
    username = user_info_json['username']
    displayName = user_info_json['displayName']
    photo = user_info_json['photo']
    email = user_info_json['email']
    return UserInfo(username, displayName, photo, email)


def get_history_object_from_json(history_object_json: dict) -> HistoryObject:
    metadata = get_metadata_from_json(history_object_json['metadata'])
    pinned = history_object_json['pinned']
    HistoryObject(metadata, pinned)


def get_history_from_json(history_object_json: [dict]) -> History:
    history_objects = map(get_history_object_from_json, history_object_json)
    return History(history_objects)
