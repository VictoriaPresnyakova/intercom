from repositories.db.enums import UserRole


class User:

    def __init__(self, **kwargs):
        self.auth_token = None
        for key, value in kwargs.items():
            if key == 'role':
                value = UserRole(value)
            setattr(self, key, value)

    def __repr__(self):
        return f'<User(email={self.email}, role={self.role})>'
