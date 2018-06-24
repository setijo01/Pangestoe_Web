import re

from passlib.hash import pbkdf2_sha512


class Utils(object):
    @staticmethod
    def hash_password(password):
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        return pbkdf2_sha512.verify(password, hashed_password)

    @staticmethod
    def email_is_valid(email):
        matcher = re.compile('^[\w-]+@([\w-]+\.)+[\w]+$')
        return True if matcher.match(email) else False