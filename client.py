from routes import Routes
import json
from monitoring import *
from user import *
from note import *
from extern import *


class Client:
    def __init__(self, host: str):
        self.routes = Routes(host)

    def get_authorized_user(self) -> UserInfo:
        result = self.routes.get_me()
        return get_user_info_from_json(result)

    def get_history(self) -> History:
        result = self.routes.get_me_history()
        return get_history_from_json(result)

    def pin_note(self, note: str, pin: bool):
        result = self.routes.put_me_history_note(note, HistoryUpdateObject(pin).to_json())

    def remove_note_from_history(self, note: str):
        result = self.routes.delete_me_history_note(note)

    def create_note(self, text: str, note: str = "") -> Note:
        if note == "":
            response = self.routes.post_notes(text)
        else:
            response = self.routes.post_notes_note(note, text)
        print(response)
        return get_note_from_json(response)

    def read_note_content(self, note: str) -> str:
        return self.routes.get_notes_note_content(note)

    def read_note(self, note: str) -> Note:
        note_json = self.routes.get_notes_note(note)
        return get_note_from_json(note_json)

    def read_note_metadata(self, note: str) -> NoteMetadata:
        metadata_json = self.routes.get_notes_note_metadata(note)
        return get_metadata_from_json(metadata_json)

    def delete_note(self, note: str):
        self.routes.delete_notes_note(note)

    def write_note(self, text: str, note: str) -> Note:
        response = self.routes.put_notes_note(note, text)
        return get_note_from_json(response)

    def get_revisions(self, note: str) -> [NoteRevisionMetadata]:
        response = self.routes.get_notes_note_revisions(note)
        return get_revisions_metadatas_from_json(response)

    def get_revision(self, note: str, revision_id: int) -> NoteRevision:
        response = self.routes.get_notes_note_revisions_revision(note, revision_id)
        return get_revision_from_json(response)

    def get_monitoring(self) -> ServerStatus:
        response = self.routes.get_monitoring()
        return get_serverstatus_from_json(response)

    def get_monitoring_prometheus(self) -> PrometheusData:
        response = self.routes.get_monitoring_prometheus()
        return get_prometheus_from_json(response)

    def upload_media(self, file: str):
        self.routes.post_media_upload(file)
