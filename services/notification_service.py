from copy import deepcopy

from misc.utils import clear_rest_input_parameters
from models.notification import Notification
from repositories.notification_repo import NotificationRepo
import random
import string


class NotificationService:
    def __init__(self):
        self.repository = NotificationRepo()

    def get_all_notifications(self, limit=500, offset=0):
        notification_list = self.repository.get_all_notifications(limit, offset)
        result = []
        for notification in notification_list:
            try:
                result.append(Notification(**notification))
            except Exception as e:
                print(e)
        return result

    def create_notification(self, kwargs):
        try:
            return Notification(**self.repository.create_notification(clear_rest_input_parameters(kwargs)))
        except Exception as e:
            print(e)
            return False

    def find_notification_by_id(self, id: int):
        try:
            return Notification(**self.repository.find_notification_by_id(id))
        except Exception as e:
            print(e)
            return None
