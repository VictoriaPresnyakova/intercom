from repositories.db.enums import NotificationType


class Notification:

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'type':
                value = NotificationType(value)
            setattr(self, key, value)

    def __repr__(self):
        return f'<Notification(text={self.text}, type={self.type}, user_id={self.user_id})>'
