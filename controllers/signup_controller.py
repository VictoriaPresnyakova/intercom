from models.user import User, UserRole
import hashlib

from repositories.db.common import insert_new_record
from services.user_service import UserService


class SignUpController:
    def __init__(self, view, main_window):
        self.view = view
        self.main_window = main_window
        self.view.signup_button.clicked.connect(self.handle_signup)
        self.user_service = UserService()

    def handle_signup(self):
        if self.view.email_input.text() == '':
            self.view.message_label.setText('Empty email')
            return
        if self.view.email_input.text().count('@') != 1:
            self.view.message_label.setText('Incorrect email')
            return
        if self.user_service.get_user_by_email(self.view.email_input.text()).__dict__:
            self.view.message_label.setText('User with such email already exists')
            return
        if self.view.password_input.text() == '':
            self.view.message_label.setText('Empty password')
            return
        if self.view.full_name_input.text() == '':
            self.view.message_label.setText('Empty full_name')
            return
        if self.view.phone_input.text() == '':
            self.view.message_label.setText('Empty phone')
            return
        if not self.view.phone_input.text().replace('+', '').replace('-', '').replace('(', '').replase(')', '').replace(' ', '').isdigit():
            self.view.message_label.setText('Incorrect phone')
            return
        if self.view.address_input.text() == '':
            self.view.message_label.setText('Empty flat number')
            return
        if not self.view.address_input.text().isdigit():
            self.view.message_label.setText('Flat number must be digit')
            return
        kwargs = {
            'email': self.view.email_input.text(),
            'password': hashlib.sha256(self.view.password_input.text().encode()).hexdigest(),
            'role': self.view.role_input.currentText(),
            'full_name': self.view.full_name_input.text(),
            'phone': self.view.phone_input.text(),
            'address': int(self.view.address_input.text()),
        }
        try:
            user = self.user_service.create_user(kwargs)
            if not user:
                raise Exception('Error while save user')
            self.view.message_label.setText('Sign up successful')
            self.main_window.show_login_view()
        except Exception as e:
            self.view.message_label.setText(f'Sign up failed: {str(e)}')

