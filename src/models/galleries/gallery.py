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
        self.counter = 0

    def json(self):
        return {
            '_id': self._id,
            'code': self.code,
            'date_created': self.date_created,
        }

    def save_to_database(self):
        while self.get_by_id(self._id):
            self._id = uuid.uuid4().hex
        Database.insert(collection='galleries', data=self.json())
        print("Gallery created successfully.")

    def collect_images(self):
        self.stash = Image.from_gallery(self._id)

    def next_image(self):
        if len(self.stash) == 0:
            self.collect_images()
        if self.counter == len(self.stash):
            self.counter = 0

        image = self.stash[self.counter]
        self.counter += 1
        return image

    @classmethod
    def get_by_id(cls, _id):
        gallery_data = Database.find_one(collection='galleries', query={'_id': _id})
        if gallery_data:
            return cls(**gallery_data)

    @classmethod
    def get_by_code(cls, code):
        gallery_data = Database.find_one(collection='galleries', query={'code': code})
        if gallery_data:
            return cls(**gallery_data)
