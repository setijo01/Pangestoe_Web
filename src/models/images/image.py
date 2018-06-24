from src.common.database import Database
import uuid


class Image(object):
    def __init__(self, path, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.path = path
        self.name = self.path.split('/')[-1]

    def json(self):
        return {
            '_id': self._id,
            'path': self.path,
            'name': self.name,
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


