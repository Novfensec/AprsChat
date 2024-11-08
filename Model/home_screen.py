from Model.base_model import BaseScreenModel
from kivy.properties import BooleanProperty, ListProperty


class HomeScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.home_screen.HomeScreen.HomeScreenView` class.
    """

    def __init__(self):
        super().__init__()
        self.data_validation_status = None
        self.UserChatsData = []
