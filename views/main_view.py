from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout


class MainView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.welcome_label = QLabel('Welcome to the Main Application!', self)
        layout.addWidget(self.welcome_label)

        self.setLayout(layout)
        self.setWindowTitle('Main Application')