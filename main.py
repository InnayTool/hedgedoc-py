import routes
import json
from monitoring import *
from user import *
from note import *
from extern import *


class Client:
    def __init__(self, host: str):
        self.client = routes.Client(host)

    def add_note_to_history(self, note: str, history_object: HistoryObject):
        json_str = json.dumps(history_object)
        self.client.put_me_history_note(note, json_str)

    def create_note(self, text: str, note: str = "") -> Note:
        if note == "":
            response = self.client.post_notes(text)
        else:
            response = self.client.post_notes_note(note, text)
        print(response)
        return get_note_from_json(response)

    def read_note_content(self, note: str):
        return self.client.get_notes_note_content(note)

    def read_note(self, note: str) -> Note:
        note_json = self.client.get_notes_note(note)
        return get_note_from_json(note_json)

    def read_note_metadata(self, note: str):
        metadata_json = self.client.get_notes_note_metadata(note)
        return get_metadata_from_json(metadata_json)

    def delete_note(self, note: str):
        self.client.delete_notes_note(note)

    def write_note(self, text: str, note: str):
        response = self.client.put_notes_note(note, text)
        return get_note_from_json(response)

    def get_revisions(self, note: str):
        response = self.client.get_notes_note_revisions(note)
        return get_revisions_from_json(response)

    def get_revision(self, note: str, revision_id: int):
        response = self.client.get_notes_note_revisions_revision(note, revision_id)
        return get_revision_from_json(response)

    def get_monitoring(self):
        response = self.client.get_monitoring()
        return get_serverstatus_from_json(response)

    def get_monitoring_prometheus(self):
        response = self.client.get_monitoring_prometheus()
        return get_prometheus_from_json(response)


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
    client = Client("http://localhost:3000")
    note = client.write_note("yolo", "testnote1")
    print(note.content)
    print(note.metadata.title)
    print(note.metadata.tags)
    print(note.editedByAtPosition)
    note = client.read_note("testnote1")
    print(note)
    print(client.read_note_content("testnote1"))
    print(note.metadata.title)
    print(note.metadata.tags)
    print(note.editedByAtPosition)


if __name__ == '__main__':
    main()
