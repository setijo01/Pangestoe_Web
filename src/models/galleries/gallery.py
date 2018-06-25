from src.common.database import Database
import uuid
import datetime
from src.models.images.image import Image


class Gallery(object):
    def __init__(self, code, date_created=datetime.datetime.utcnow(), _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.code = code
        self.date_created = date_created
        self.stash = []

    def collect_images(self):
        return Image.from_gallery(self._id)

    def next_image(self):
        pass
