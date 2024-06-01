from enum import IntEnum, Enum


class UserRole(str, Enum):
    USER = "user"
    DOORKEEPER = "doorkeeper"
    CHILD = "child"
