import routes
import json


class JSONSerializable:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class UserInfo(JSONSerializable):
    def __init__(self, username: str, displayName: str, photo: str, email: str):
        self.username = username
        self.displayName = displayName
        self.photo = photo
        self.email = email


class UserPasswordChange(JSONSerializable):
    def __init__(self, password: str):
        self.password = password


class ImageProxyRequest(JSONSerializable):
    def __init__(self, src):
        self.src = src


class ImageProxyResponse(JSONSerializable):
    def __init__(self, src):
        self.src = src


class NotePermissions(JSONSerializable):
    def __init__(self, owner: str, sharedTo: [str]):
        self.owner = owner
        self.sharedTo = owner  # Username, canEdit


class NoteRevisonMetadata(JSONSerializable):
    def __init__(self, id: str, createdAt: str, length: int):
        self.id = id
        self.createdAt = createdAt
        self.length = length


class NoteRevision(JSONSerializable):
    def __init__(self, content: str, authorship: str, patch: str):
        self.content = content
        self.authorship = authorship
        self.patch = patch


class GistLink(JSONSerializable):
    def __init__(self, link: str):
        self.link = link


class DropBoxLink(JSONSerializable):
    def __init__(self, link: str):
        self.link = link


class EmailLogin(JSONSerializable):
    def __init__(self, email: str, password: str):
        self.email = ""
        self.password = ""


class LdapLogin(JSONSerializable):
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password


class OpenIdLogin(JSONSerializable):
    def __init__(self, openId: str):
        self.openId = openId


class ServerVersion(JSONSerializable):
    def __init__(self, major: int, minor: int, patch: int, preRelease: str, commit: str):
        self.major = major
        self.minor = minor
        self.patch = patch
        self.preRelease = preRelease
        self.commit = commit


class ServerStatus(JSONSerializable):
    def __init__(self,
                 serverVersion: ServerVersion,
                 onlineNotes: int,
                 onlineUsers: int,
                 distinctOnlineUsers: int,
                 notesCount: int,
                 registeredUsers: int,
                 onlineRegisteredUsers: int,
                 distinctOnlineRegisteredUsers: int,
                 isConnectionBusy: bool,
                 connectionSocketQueueLength: int,
                 isDisconnectBusy: bool,
                 disconnectSocketQueueLength: int
                 ):
        self.serverVersion = serverVersion
        self.onlineNotes = onlineNotes
        self.onlineUsers = onlineUsers
        self.distinctOnlineUsers = distinctOnlineUsers
        self.notesCount = notesCount
        self.registeredUsers = registeredUsers
        self.onlineRegisteredUsers = onlineRegisteredUsers
        self.distinctOnlineRegisteredUsers = distinctOnlineRegisteredUsers
        self.isConnectionBusy = isConnectionBusy
        self.connectionSocketQueueLength = connectionSocketQueueLength
        self.isDisconnectBusy = isDisconnectBusy
        self.disconnectSocketQueueLength = disconnectSocketQueueLength


class NoteMetadata(JSONSerializable):
    def __init__(self,
                 id: str,
                 alias: str,
                 title: str,
                 description: str,
                 tags: [str],
                 updateTime: str,
                 updateUser: str,
                 viewCount: int,
                 createTime: str,
                 editedBy: [str]
                 ):
        self.id = id
        self.alias = alias
        self.title = title
        self.description = description
        self.tags = tags
        self.updateTime = updateTime
        self.updateUser = updateUser
        self.viewCount = viewCount
        self.createTime = createTime
        self.editedBy = editedBy
        self.permissions = NotePermissions


class HistoryObject(JSONSerializable):
    def __init__(self, metadata: NoteMetadata, pinned: bool):
        self.metadata = metadata
        self.pinned = pinned


class History(JSONSerializable):
    def __init__(self, items: [HistoryObject]):
        self.history = items


class Note(JSONSerializable):
    def __init__(self, content: str, metadata: NoteMetadata, editedByAtPosition: [int]):
        self.content = content
        self.metadata = metadata
        self.editedByAtPosition = editedByAtPosition


def get_metadata_form_json(json) -> NoteMetadata:
    return NoteMetadata(
        json['id'],
        json['alias'],
        json['title'],
        json['description'],
        json['tags'],
        json['updateTime'],
        json['updateUser'],
        json['viewCount'],
        json['createdTime'],
        json['editedBy']
    )


class Client:
    def __init__(self, host: str):
        self.client = routes.Client(host)

    def add_note_to_history(self, note: str, history_object: HistoryObject):
        json_str = json.dumps(history_object)
        self.client.put_me_history_note(note, json_str)

    def create_note(self, text: str, note: str = ""):
        if note == "":
            self.client.post_notes(text)
        else:
            self.client.post_notes_note(note, text)

    def read_note_without_metadata(self, note: str):
        self.client.get_notes_note_content(note)

    def read_note(self, note: str) -> Note:
        json = self.client.get_notes_note(note)
        return Note(json['content'], get_metadata_form_json(json['metadata']), json['editedByAtPosition'])


def main2():
    client = Client("http://localhost")
    history_object = HistoryObject(
        NoteMetadata("test", "test", "test", "test", ["test", "test2"],
                     "2020", "user", 5, "2020", ["test1", "test2"]), True)
    client.add_note_to_history("", history_object)


class SimpleClass(JSONSerializable):
    def __init__(self):
        self.test = 1
        self.yolo = "ghah"
        self.hjz = ["wd", "kl"]


class SimpleClass2(JSONSerializable):
    def __init__(self):
        self.test = SimpleClass()
        self.yolo = "ghah"
        self.hjz = ["wd", "kl"]


def main():
    notemeta = NoteMetadata("test", "test", "test", "test", ["test", "test2"],
                            "2020", "user", 5, "2020", ["test1", "test2"])
    # notemeta2 = json.dumps(notemeta.__dict__)
    notemeta2 = notemeta.toJSON()
    print(str(notemeta2))
    # print(str(get_metadata_form_json(notemeta2)))


# def main():


if __name__ == '__main__':
    main()
