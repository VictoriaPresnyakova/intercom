import random
from time import sleep

from repositories.db.enums import NotificationType, UserNotification
from services.mail_sender import MailSender
from services.notification_service import NotificationService
from services.user_service import UserService


def create_and_send_notifications():
    mail_sender = MailSender()
    notification_service = NotificationService()
    user_service = UserService()
    notifications = [e.value for e in NotificationType]
    while True:
        user_list = user_service.get_all_users()
        for user in user_list:
            notification = notification_service.create_notification(
                {'type': random.choice(notifications), 'text': 'some_text', 'user_id': user.id})
            print(notification)
            if user.notification_settings == UserNotification.ALL or \
                    user.notification_settings.value == notification.type.value:
                mail_sender.send_email(user.email, notification.type, notification.text)
            print()
        sleep(20 * 60)
