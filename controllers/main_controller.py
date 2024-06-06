from models.user import User


class MainController:
    def __init__(self, view, main_window, user: User):
        self.view = view
        self.main_window = main_window
        self.view.profile_button.clicked.connect(lambda: self.main_window.show_profile_view())
        self.view.settings_button.clicked.connect(lambda: self.main_window.show_settings_view())
        self.view.access_button.clicked.connect(lambda: self.main_window.show_access_view())
        user_settings = user.settings
        self.view.profile_button.setVisible(user_settings.get('show_profile', True))
        self.view.settings_button.setVisible(user_settings.get('show_settings', True))



