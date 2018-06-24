from src.common.database import Database
import datetime
import uuid


class User(object):

    def __init__(self, email, hashed_password, date_registered=datetime.datetime.utcnow(), _id=None):
        self.email = email
        self.hashed_password = hashed_password
        self.date_registered = date_registered
        self._id = uuid.uuid4().hex if _id is None else _id

    def json(self):
        return {
            '_id': self._id,
            'email': self.email,
            'hashed_password': self.hashed_password,
            'date_registered': self.date_registered
        }

    @classmethod
    def get_by_id(cls, _id):
        user_data = Database.find_one(collection='users', query={'_id': _id})
        if user_data:
            return cls(**user_data)

    @classmethod
    def get_by_email(cls, email):
        user_data = Database.find_one(collection='users', query={'email': email})
        if user_data:
            return cls(**user_data)

    def save_to_database(self):
        while self.get_by_id(self._id):
            self._id = uuid.uuid4().hex
        Database.insert(collection='users', data=self.json())
        print("User created successfully.")

    def update_to_database(self):
        Database.update(collection='users', query_id=self._id, data=self.json())

    def is_login_valid(self):
        pass

    def is_register_valid(self):
        pass
