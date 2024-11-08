from View.Components.ResponsiveGrid import ResponsiveGrid
from View.HomeScreen.Components.ChatsCard import ChatsCard


class ChatsGrid(ResponsiveGrid):
    def __init__(self, *args, **kwargs):
        super(ChatsGrid, self).__init__(*args, **kwargs)
        self.clear_widgets()

    def add_cards(self, data: list, *args) -> None:
        self.clear_widgets()
        for userdata in data:
            self.add_widget(
                ChatsCard(chatusername=userdata['username'])
            )
