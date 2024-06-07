from models.user import User
from repositories.db.enums import UserRole


class AuthController:
    def __init__(self, view, main_window):
        self.view = view
        self.main_window = main_window
        self.user = None
        self.view.verify_button.clicked.connect(self.verify_token)

    def verify_token(self):
        token = self.view.token_input.text()

        if self.user and self.user.auth_token == token:
            self.view.message_label.setText('Authentication successful')
            self.user.auth_token = None
            self.main_window.set_current_user(self.user)
            if self.user.role == UserRole.DOORKEEPER:
                self.main_window.show_main_view()  # TODO
            else:
                self.main_window.show_main_view()
        else:
            self.view.message_label.setText('Invalid token')

    def set_user(self, user):
        self.user = user
