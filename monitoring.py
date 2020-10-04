from jsonserialize import JSONSerializable


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


class PrometheusData(JSONSerializable):
    def __init__(self, data: str):
        self.data = data


def get_serverversion_from_json(serverversion_json: dict) -> ServerVersion:
    major = serverversion_json['major']
    minor = serverversion_json['minor']
    patch = serverversion_json['patch']
    preRelease = serverversion_json['preRelease']
    commit = serverversion_json['commit']
    return ServerVersion(major, minor, patch, preRelease, commit)


def get_serverstatus_from_json(serverstatus_json: dict) -> ServerStatus:
    serverversion = get_serverversion_from_json(serverstatus_json['serverVersion'])
    onlineNotes = serverstatus_json['onlineNotes']
    onlineUsers = serverstatus_json['onlineUsers']
    distinctOnlineUsers = serverstatus_json['distinctOnlineUsers']
    notesCount = serverstatus_json['notesCount']
    registeredUsers = serverstatus_json['registeredUsers']
    onlineRegisteredUsers = serverstatus_json['onlineRegisteredUsers']
    distinctOnlineRegisteredUsers = serverstatus_json['distinctOnlineRegisteredUsers']
    isConnectionBusy = serverstatus_json['isConnectionBusy']
    connectionSocketQueueLength = serverstatus_json['connectionSocketQueueLength']
    isDisconnectBusy = serverstatus_json['isDisconnectBusy']
    disconnectSocketQueueLength = serverstatus_json['disconnectSocketQueueLength']
    return ServerStatus(
        serverversion,
        onlineNotes,
        onlineUsers,
        distinctOnlineUsers,
        notesCount,
        registeredUsers,
        onlineRegisteredUsers,
        distinctOnlineRegisteredUsers,
        isConnectionBusy,
        connectionSocketQueueLength,
        isDisconnectBusy,
        disconnectSocketQueueLength
    )


def get_prometheus_from_json(prometheus_json) -> PrometheusData:
    # TODO: return PrometheusData(prometheus_json['']
    return prometheus_json
