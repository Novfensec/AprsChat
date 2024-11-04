from View.base_screen import BaseScreenView


class SettingsScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def on_enter(self) -> None:
        self.app.current_screen = self.name

    def on_leave(self) -> None:
        self.app.last_used_screen = self.name
