from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton


class DoorkeeperView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.profile_button = QPushButton('Profile', self)
        layout.addWidget(self.profile_button)

        self.settings_button = QPushButton('Settings', self)
        layout.addWidget(self.settings_button)

        self.welcome_label = QLabel('Welcome to the Doorkeeper Application!', self)
        layout.addWidget(self.welcome_label)

        self.setLayout(layout)
        self.setWindowTitle('Main Application')