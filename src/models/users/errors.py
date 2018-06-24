
class UserError(Exception):
    def __init__(self, message):
        self.message = message


class UserNotExistError(UserError):
    pass


class UserAlreadyExistsError(UserError):
    pass


class UserIncorrectPasswordError(UserError):
    pass


class IncorrectEmailFormat(UserError):
    pass