from typing import Dict
from dataclasses import dataclass,field

@dataclass
class User:
    _id:str
    username:str
    password:str #= field(repr=False)

    def json(self)->Dict:
        return {
            "_id":self._id,
            "username":self.username
        }