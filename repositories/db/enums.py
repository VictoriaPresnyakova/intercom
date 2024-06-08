from enum import IntEnum, Enum


class UserRole(str, Enum):
    USER = "user"
    DOORKEEPER = "doorkeeper"
    CHILD = "child"


class UserNotification(str, Enum):
    ACCEPTED = "accepted"
    CANCELED = "canceled"
    ALL = "all"
    NONE = "none"


class NotificationType(str, Enum):
    ACCEPTED = "accepted"
    CANCELED = "canceled"
