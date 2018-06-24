from src.common.database import Database
from src.common.utils import Utils
import src.models.users.errors as UserErrors
import datetime
import uuid


class User(object):

    def __init__(self, email, hashed_password, date_registered=datetime.datetime.utcnow(), _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.email = email
        self.hashed_password = hashed_password
        self.date_registered = date_registered

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

    @staticmethod
    def is_login_valid(email, sha512_password):
        user_data = Database.find_one(collection='users', query={'email': email})
        if user_data is None:
            raise UserErrors.UserNotExistError("User doesn't exist.")
        if not Utils.check_hashed_password(sha512_password, user_data['hashed_password']):
            raise UserErrors.UserIncorrectPasswordError("Incorrect password.")
        return True

    @staticmethod
    def register(email, sha512_password):
        user_data = Database.find_one(collection='users', query={'email': email})
        if user_data:
            raise UserErrors.UserAlreadyExistsError("User already registered.")
        if not Utils.email_is_valid(email):
            raise UserErrors.IncorrectEmailFormat("Invalid email.")

        User(email, Utils.hash_password(sha512_password)).save_to_database()

        return True
