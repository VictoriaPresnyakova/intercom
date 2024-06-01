# views/signup_view.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QComboBox

class SignUpView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText('Email')
        layout.addWidget(self.email_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText('Password')
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.role_input = QComboBox(self)
        self.role_input.addItems(['user', 'doorkeeper', 'child'])
        layout.addWidget(self.role_input)

        self.full_name_input = QLineEdit(self)
        self.full_name_input.setPlaceholderText('Full Name')
        layout.addWidget(self.full_name_input)

        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText('Phone')
        layout.addWidget(self.phone_input)

        self.address_input = QLineEdit(self)
        self.address_input.setPlaceholderText('Address')
        layout.addWidget(self.address_input)

        self.key_input = QLineEdit(self)
        self.key_input.setPlaceholderText('Key')
        layout.addWidget(self.key_input)

        self.signup_button = QPushButton('Sign Up', self)
        layout.addWidget(self.signup_button)

        self.message_label = QLabel('', self)
        layout.addWidget(self.message_label)

        self.setLayout(layout)
        self.setWindowTitle('Sign Up')
