from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QCheckBox


class AccessView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.profile_checkbox = QCheckBox('Profile', self)
        layout.addWidget(self.profile_checkbox)

        self.settings_checkbox = QCheckBox('Settings', self)
        layout.addWidget(self.settings_checkbox)

        self.save_button = QPushButton('Save', self)
        layout.addWidget(self.save_button)

        self.back_button = QPushButton('Back', self)
        layout.addWidget(self.back_button)

        self.message_label = QLabel('', self)
        layout.addWidget(self.message_label)

        self.setLayout(layout)
        self.setWindowTitle('Settings')
