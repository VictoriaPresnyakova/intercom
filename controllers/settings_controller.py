from services.user_service import UserService


class SettingsController:
    def __init__(self, view, main_window, user):
        self.view = view
        self.main_window = main_window
        self.user = user
        self.load_user_data()
        self.view.save_button.clicked.connect(self.save_user_data)
        self.view.back_button.clicked.connect(lambda: self.main_window.show_main_view())
        self.user_service = UserService()

    def load_user_data(self):
        self.view.two_factor_checkbox.setChecked(self.user.settings.get('2factor', False))

    def save_user_data(self):
        self.user.settings['2factor'] = self.view.two_factor_checkbox.isChecked()

        try:
            self.user = self.user_service.update_user(self.user)
            if self.user:
                self.view.message_label.setText('Profile updated successfully')
            else:
                raise Exception('Error while saving')
        except Exception as e:
            self.view.message_label.setText(f'Error updating profile: {str(e)}')