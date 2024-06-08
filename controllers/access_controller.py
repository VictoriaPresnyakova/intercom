from services.user_service import UserService


class AccessController:
    def __init__(self, view, main_window, user):
        self.view = view
        self.main_window = main_window
        self.user = user
        self.load_user_data()
        self.view.save_button.clicked.connect(self.save_user_data)
        self.view.back_button.clicked.connect(lambda: self.main_window.show_main_view())
        self.user_service = UserService()

    def load_user_data(self):
        self.view.profile_checkbox.setChecked(self.user.settings.get('show_profile', True))
        self.view.settings_checkbox.setChecked(self.user.settings.get('show_settings', True))

    def save_user_data(self):
        self.user.settings['show_profile'] = self.view.profile_checkbox.isChecked()
        self.user.settings['show_settings'] = self.view.settings_checkbox.isChecked()

        try:
            self.user = self.user_service.update_user(self.user)
            if self.user:
                self.view.message_label.setText('Profile updated successfully')
            else:
                raise Exception('Error while saving')
        except Exception as e:
            self.view.message_label.setText(f'Error updating profile: {str(e)}')