from models.user import User
from repositories.db.enums import UserRole
from services.mail_sender import MailSender
from services.user_service import UserService


class AuthController:
    def __init__(self, view, main_window):
        self.view = view
        self.main_window = main_window
        self.user = None
        self.user_service = UserService()
        self.mail_sender = MailSender()
        self.view.verify_button.clicked.connect(self.verify_token)
        self.view.resend_token_button.clicked.connect(self.resend_token)

    def resend_token(self):
        if self.user:
            token = self.user_service.generate_token()
            self.user.auth_token = token
            self.user_service.update_user(self.user)
            self.mail_sender.send_email(self.user.email, subject="Your Authentication Token",
                                        body=f"Your authentication token is: {token}")
            self.view.message_label.setText('Token was resend')

    def verify_token(self):
        token = self.view.token_input.text()

        if self.user and self.user.auth_token == token:
            self.user.auth_token = None
            self.user_service.update_user(self.user)
            self.main_window.set_current_user(self.user)
            if self.user.role == UserRole.DOORKEEPER:
                self.main_window.show_main_view()
            else:
                self.main_window.show_main_view()
        else:
            self.view.message_label.setText('Invalid token')

    def set_user(self, user):
        self.user = user
