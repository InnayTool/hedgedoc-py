from jsonserialize import JSONSerializable


class NotePermissions(JSONSerializable):
    def __init__(self, owner: str, sharedToUsers: [str], sharedToGroups: [str]):
        self.owner = owner
        self.sharedToUsers = sharedToUsers
        self.sharedToGroups = sharedToGroups


class NoteRevisionMetadata(JSONSerializable):
    def __init__(self, revision_id: str, createdAt: str, length: int):
        self.id = revision_id
        self.createdAt = createdAt
        self.length = length


class NoteRevision(JSONSerializable):
    def __init__(self, content: str, authorship: str, patch: str):
        self.content = content
        self.authorship = authorship
        self.patch = patch


class NoteMetadata(JSONSerializable):
    def __init__(
            self,
            note_id: str,
            alias: str,
            title: str,
            description: str,
            tags: [str],
            updateTime: str,
            updateUser: str,
            viewCount: int,
            createTime: str,
            editedBy: [str],
            permissions: NotePermissions
    ):
        self.id = note_id
        self.alias = alias
        self.title = title
        self.description = description
        self.tags = tags
        self.updateTime = updateTime
        self.updateUser = updateUser
        self.viewCount = viewCount
        self.createTime = createTime
        self.editedBy = editedBy
        self.permissions = permissions


class HistoryObject(JSONSerializable):
    def __init__(self, metadata: NoteMetadata, pinned: bool):
        self.metadata = metadata
        self.pinned = pinned


class HistoryUpdateObject(JSONSerializable):
    def __init__(self, pin: bool):
        self.pin = pin


class History(JSONSerializable):
    def __init__(self, items: [HistoryObject]):
        self.history = items


class Note(JSONSerializable):
    def __init__(self, content: str, metadata: NoteMetadata, editedByAtPosition: [int]):
        self.content = content
        self.metadata = metadata
        self.editedByAtPosition = editedByAtPosition


def get_permissions_from_json(permissions_json: dict) -> NotePermissions:
    owner = permissions_json['owner']
    sharedToUsers = permissions_json['sharedToUsers']
    sharedToGroups = permissions_json['sharedToGroups']
    return NotePermissions(owner, sharedToUsers, sharedToGroups)


def get_metadata_from_json(metadata_json: dict) -> NoteMetadata:
    note_id = metadata_json['id'],
    alias = metadata_json['alias'],
    title = metadata_json['title'],
    description = metadata_json['description'],
    tags = metadata_json['tags'],
    updateTime = metadata_json['updateTime'],
    updateUser = metadata_json['updateUser'],
    viewCount = metadata_json['viewCount'],
    createTime = metadata_json['createTime'],
    editedBy = metadata_json['editedBy'],
    # TODO: Change to permissions
    permissions = get_permissions_from_json(metadata_json['permission'])
    return NoteMetadata(
        note_id,
        alias,
        title,
        description,
        tags,
        updateTime,
        updateUser,
        viewCount,
        createTime, editedBy,
        permissions
    )


def get_note_from_json(note_json: dict) -> Note:
    content = note_json["content"]
    metadata = get_metadata_from_json(note_json["metadata"])
    editedByAtPosition = note_json["editedByAtPosition"]
    return Note(content, metadata, editedByAtPosition)


def get_revision_from_json(revision: dict) -> NoteRevision:
    content = revision['content']
    authorship = revision['authorship']
    patch = revision['patch']
    return NoteRevision(content, authorship, patch)


def get_revisions_metadatas_from_json(revisions_metadatas_json: [dict]) -> [NoteRevisionMetadata]:
    return map(get_revision_metadata_from_json, revisions_metadatas_json)


def get_revision_metadata_from_json(revision_metadata_json: dict) -> NoteRevisionMetadata:
    revision_id = revision_metadata_json['id']
    createdAt = revision_metadata_json['createdAt']
    length = revision_metadata_json['length']
    return NoteRevisionMetadata(revision_id, createdAt, length)
