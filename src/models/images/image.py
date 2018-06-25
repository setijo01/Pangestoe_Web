from src.common.database import Database
import uuid


class Image(object):
    def __init__(self, path, gal_id, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.path = path
        self.name = self.path.split('/')[-1]
        self.gal_id = gal_id

    def json(self):
        return {
            '_id': self._id,
            'path': self.path,
            'name': self.name,
            'gal_id': self.gal_id
        }

    def get_path(self):
        return self.path

    @classmethod
    def get_by_id(cls, _id):
        image_data = Database.find_one(collection='images', query={'_id': _id})
        if image_data:
            return cls(**image_data)

    @classmethod
    def get_by_name(cls, name):
        image_data = Database.find_one(collection='images', query={'name': name})
        if image_data:
            return cls(**image_data)

    def save_to_database(self):
        while self.get_by_id(self._id):
            self._id = uuid.uuid4().hex
        if Database.find_one(collection='images', query={'name': self.name}):
            Database.update(collection='images', query={'name': self.name}, data=self.json())
        else:
            Database.insert(collection='images', data=self.json())
        print("User created successfully.")

    @staticmethod
    def from_gallery(gallery_id):
        return [Image(**image) for image in Database.find(collection='images', query={'gallery_id': gallery_id})]


