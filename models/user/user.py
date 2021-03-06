import uuid
from dataclasses import dataclass,field
from typing import Dict

from models.model import Model
from common.utils import Utils
import models.user.errors as errors
@dataclass
class User(Model):
    collection: str = field(init=False,default='users')
    email: str
    password: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    @classmethod
    def find_by_email(cls, email:str)-> "User":
        try:
            return cls.find_one_by('email',email)
        except TypeError:
            raise errors.UserNotFoundError('A user with this e-mail was not found.')

    @classmethod
    def register_user(cls, email: str, password: str) -> bool:
        if not Utils.email_is_valid(email):
            raise errors.InvalidEmailError('The email does not have the right format')

        try:
            cls.find_by_email(email)
            raise errors.UserAlreadyRegisteredError('The email you used to register already exists.')
        except errors.UserNotFoundError:
            User(email,password).save_to_mongo()
        
        return True
    
    def json(self) -> Dict:
        return {
            '_id': self._id,
            'email': self.email,
            'password': self.password
        }