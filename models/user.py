from dataclasses import dataclass
from typing import List
from jinja2 import Template


@dataclass
class User:
    name: str
    email: str
    age: str
    gender: str
    interests: List[str]
    industry: str
    purchases: List[str]

    __template__ = Template(open("templates/user.template.txt").read())

    def from_dict(data) -> "User":
        """Create User object from dictionary"""
        return User(
            data["name"],
            data["email"],
            data["age"],
            data["gender"],
            data["interest"],
            data["industry"],
            data["purchases"],
        )

    def __str__(self):
        return self.__template__.render(**self.__dict__)

    def __repr__(self) -> str:
        return self.__str__()
