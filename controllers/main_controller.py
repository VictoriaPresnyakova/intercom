class MainController:
    def __init__(self, view, main_window):
        self.view = view
        self.main_window = main_window
        self.view.profile_button.clicked.connect(self.show_profile)

    def show_profile(self):
        self.main_window.show_profile_view()
