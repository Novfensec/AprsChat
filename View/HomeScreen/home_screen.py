from View.base_screen import BaseScreenView
from kivy.clock import Clock 


class HomeScreenView(BaseScreenView):
    def __init__(self, **kwargs):
        super(HomeScreenView, self).__init__(**kwargs)
    
    def model_is_changed(self, *args) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        if self.model.data_validation_status:
            self.update_grid(self.model.UserChatsData),
        else:
            self.update_grid([{"username": "No existing chats found."},])

    def on_enter(self) -> None:
        self.app.current_screen = self.name
        if not self.model.data_validation_status:
            Clock.schedule_once(
                self.controller.set_data_validation_status, 0.1
            )
        else:
            self.model_is_changed()

    def on_leave(self) -> None:
        self.app.last_used_screen = self.name

    def update_grid(self, data: list, *args) -> None:
        self.ids.HomeScreenContext.ids.ChatsGrid.add_cards(data)
