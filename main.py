import routes


class HistoryObject:
    def __init__(self):
        pass


class UserInfo:
    def __init__(self, username: str, displayName: str, photo: str, email: str):
        self.username = username
        self.displayName = displayName
        self.photo = photo
        self.email = email


class UserPasswordChange:
    def __init__(self, password: str):
        self.password = password


class ImageProxyRequest:
    def __init__(self, src):
        self.src = src


class ImageProxyResponse:
    def __init__(self, src):
        self.src = src


class NotePermissions:
    owner = ""
    sharedTo = []  # Username, canEdit


class NoteRevisonMetadata:
    id = ""
    createdAt = ""
    length = ""


class NoteRevision:
    content = ""
    authorship = []
    patch = []


class GistLink:
    link = ""


class DropBoxLink:
    link = ""


class EmailLogin:
    email = ""
    password = ""


class LdapLogin:
    username = ""
    password = ""


class OpenIdLogin:
    openId = ""


class ServerVersion:
    major = 0
    minor = 0
    patch = 0
    preRelease = ""
    commit = ""


class ServerStatus:
    serverVersion = ServerVersion
    onlineNotes = 0
    onlineUsers = 0
    distinctOnlineUsers = 0
    notesCount = 0
    registeredUsers = 0
    onlineRegisteredUsers = 0
    distinctOnlineRegisteredUsers = 0
    isConnectionBusy = False
    connectionSocketQueueLength = 0
    isDisconnectBusy = False
    disconnectSocketQueueLength = 0


class NoteMetadata:
    id = ""
    alias = ""
    title = ""
    description = ""
    tags = []
    updateTime = ""
    updateUser = UserInfo
    viewCount = 0
    createTime = ""
    editedBy = []
    permissions = NotePermissions


class HistoryObject:
    metadata: NoteMetadata
    pinned: False


class History:
    history = []  # History Objects


class Note:
    content = ""
    metadata = NoteMetadata
    editedByAtPosition = []


class Client:
    def add_note_to_history(self, note: str, history_object: HistoryObject):
        client = routes.Client("http://localhost:3000")
        client.put_me_history_note(note, history_object)

    def create_note(self, text: str, note: str = ""):
        if note == "":
            self.post_notes(text)
        else:
            self.post_notes_note(note, text)
