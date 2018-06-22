import uuid
import datetime
from src.common.database import Database


class Entry(object):
    def __init__(self, header, content, _id=None, date_created=datetime.datetime.utcnow()):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.header = header
        self.content = content
        self.date_created = date_created

    def json(self):
        return {
            '_id': self._id,
            'header': self.header,
            'content': self.content,
            'date_created': self.date_created,

        }

    @classmethod
    def get_by_id(cls, _id):
        entry_data = Database.find_one(collection='entries', query={'_id': _id})
        if entry_data:
            return cls(**entry_data)

    def save_to_database(self):
        while self.get_by_id(self._id):
            self._id = uuid.uuid4().hex
        Database.insert(collection='entries', data=self.json())
        print("Entry created successfully.")

    def __repr__(self):
        return str(self.json())