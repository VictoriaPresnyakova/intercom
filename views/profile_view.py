from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QComboBox


class ProfileView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.email_label = QLabel('Email', self)
        self.email_input = QLineEdit(self)
        self.email_input.setReadOnly(True)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        self.full_name_label = QLabel('Full Name', self)
        self.full_name_input = QLineEdit(self)
        layout.addWidget(self.full_name_label)
        layout.addWidget(self.full_name_input)

        self.phone_label = QLabel('Phone', self)
        self.phone_input = QLineEdit(self)
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_input)

        self.address_label = QLabel('Address', self)
        self.address_input = QLineEdit(self)
        layout.addWidget(self.address_label)
        layout.addWidget(self.address_input)

        self.notification_input = QComboBox(self)
        self.notification_input.addItems(['all', 'accepted', 'canceled'])
        layout.addWidget(self.notification_input)

        self.save_button = QPushButton('Save', self)
        layout.addWidget(self.save_button)

        self.back_button = QPushButton('Back', self)
        layout.addWidget(self.back_button)

        self.message_label = QLabel('', self)
        layout.addWidget(self.message_label)

        self.setLayout(layout)
        self.setWindowTitle('Profile')
