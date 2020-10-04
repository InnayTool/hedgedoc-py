from jsonserialize import JSONSerializable


class ImageProxyRequest(JSONSerializable):
    def __init__(self, src):
        self.src = src


class ImageProxyResponse(JSONSerializable):
    def __init__(self, src):
        self.src = src


class GistLink(JSONSerializable):
    def __init__(self, link: str):
        self.link = link


class DropBoxLink(JSONSerializable):
    def __init__(self, link: str):
        self.link = link
