from abc import ABC, abstractmethod


class NotificationRepoABC(ABC):

    @abstractmethod
    def get_all_notifications(self, limit, offset):
        pass

    @abstractmethod
    def create_notification(self, kwargs):
        pass

    @abstractmethod
    def find_notification_by_id(self, id: int):
        pass

