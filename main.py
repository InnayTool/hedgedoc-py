from client import *


test_note_metadata = NoteMetadata(
    "id",
    "alias",
    "title",
    "description",
    ["tag1", "tag2"],
    "updateTime",
    "updateUser",
    0,
    "createTime",
    ["editUser1", "editUser2"],
    NotePermissions("owner", ["user1", "user2"], ["group1", "group2"])
)


def main():
    hd_client = Client("http://localhost:3000")
    note = hd_client.write_note("yolo", "testnote1")
    print(note.content)
    print(note.metadata.title)
    print(note.metadata.tags)
    print(note.editedByAtPosition)
    note = hd_client.read_note("testnote1")
    print(note)
    print(hd_client.read_note_content("testnote1"))
    print(note.metadata.title)
    print(note.metadata.tags)
    print(note.editedByAtPosition)


if __name__ == '__main__':
    main()
