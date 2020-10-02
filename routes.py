import requests


class Client:
    def __init__(self, server_address: str, auth_token: str = ""):
        self.server_address = server_address
        self.auth_token = auth_token

    def get_me(self):
        result = requests.get(self.server_address + "/me")
        if result.status_code != 200:
            return None
        else:
            return result.json()

    def get_me_history(self):
        result = requests.get(self.server_address + "/me/history")
        if result.status_code != 200:
            return None
        else:
            return result.json()

    def get_me_history_note(self, note: str):
        result = requests.get(self.server_address + "/me/history" + note)
        if result.status_code != 200:
            return None
        else:
            return result.json()

    def put_me_history_note(self, note: str, history_object_json):
        result = requests.put(self.server_address + "/me/history/" + note, json=history_object_json)
        if result.status_code != 200:
            return None
        else:
            return result.json()

    def delete_me_history_note(self, note: str):
        result = requests.delete(self.server_address + "/me/history/" + note)
        if result.status_code != 200:
            return None
        else:
            return result.json()

    def remove_note_from_history(self, note: str):
        self.delete_me_history_note(note)

    def get_me_notes(self):
        result = requests.get(self.server_address + "/me/notes")
        if result.status_code != 200:
            return None
        else:
            return result.json()

    def post_notes(self, text: str):
        result = requests.post(self.server_address + "/notes", data=text)
        if result.status_code != 201:  # Documentation and Implementation differ: documentation: 200
            return None
        else:
            return result.json()

    def get_notes_note(self, note: str):
        result = requests.get(self.server_address + "/notes/" + note)
        if result.status_code != 200:
            return None
        else:
            return result.json()

    def post_notes_note(self, note: str, text: str):
        result = requests.post(self.server_address + "/notes/" + note, data=text)
        if result.status_code != 200:
            return None
        else:
            return result.json()

    def delete_notes_note(self, note: str):
        result = requests.delete(self.server_address + "/notes/" + note)
        if result.status_code != 200:
            return None
        else:
            return result.json()

    def put_notes_note(self, note: str, text: str):
        result = requests.put(self.server_address + "/notes/" + note, data=text)
        if result.status_code != 200:
            return None
        else:
            return result.json()

    def put_notes_note_metadata(self, note: str, metadata):
        result = requests.put(self.server_address + "/notes/" + note + "/metadata", json=metadata)
        if result.status_code != 200:
            return None
        else:
            return result.json()

    def get_notes_note_metadata(self, note: str):
        result = requests.get(self.server_address + "/notes/" + note + "/metadata")
        if result.status_code != 200:
            return None
        else:
            return result.json()

    def get_notes_note_revisions(self, note: str):
        result = requests.get(self.server_address + "/notes/" + note + "/revisions")
        if result.status_code != 200:
            return None
        else:
            return result.json()

    def get_notes_note_revisions_revision(self, note: str, revision_id: int):
        result = requests.get(self.server_address + "/notes/" + note + "/revisions/" + str(revision_id))
        if result.status_code != 200:
            return None
        else:
            return result.json()

    def get_notes_note_content(self, note: str):
        result = requests.get(self.server_address + "/notes/" + note + "/content")
        if result.status_code != 200:
            return None
        else:
            return result.text

    def post_media_upload(self, note: str, file):
        result = requests.post(self.server_address + "/notes/" + note + "/content", data=file)
        if result.status_code != 200:
            return None
        else:
            return result.json()

    def get_monitoring(self):
        result = requests.get(self.server_address + "/monitoring")
        if result.status_code != 200:
            return None
        else:
            return result.json()

    def get_monitoring_prometheus(self):
        result = requests.get(self.server_address + "/monitoring/prometheus")
        if result.status_code != 200:
            return None
        else:
            return result.json()
