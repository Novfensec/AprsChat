from View.base_screen import BaseScreenView
from kivy.clock import Clock


class HomeScreenView(BaseScreenView):
    def __init__(self, **kwargs):
        super(HomeScreenView, self).__init__(**kwargs)
        Clock.schedule_once(self.model_is_changed, 1)

    def model_is_changed(self, *args) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        if not self.model.data_validation_status:
            self.controller.set_data_validation_status()
            Clock.schedule_once(self.update_grid, 1)
        elif self.model.data_validation_status:
            Clock.schedule_once(self.update_grid, 1)

    def on_enter(self) -> None:
        self.app.current_screen = self.name

    def on_leave(self) -> None:
        self.app.last_used_screen = self.name

    def update_grid(self, *args) -> None:
        if self.model.data_validation_status:
            data = self.model.UserChatsData
            self.ids.HomeScreenContext.ids.ChatsGrid.add_cards(data)
        else:
            pass
