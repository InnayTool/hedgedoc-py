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
