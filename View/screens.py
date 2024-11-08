# The screen's dictionary contains the objects of the models and controllers
# of the screens of the application.

from Model.home_screen import HomeScreenModel
from Controller.home_screen import HomeScreenController
from Model.settings_screen import SettingsScreenModel
from Controller.settings_screen import SettingsScreenController
from Model.chat_screen import ChatScreenModel
from Controller.chat_screen import ChatScreenController

screens = {
    'home screen': {
        'model': HomeScreenModel,
        'controller': HomeScreenController,
    },
    'chat screen': {
        'model': ChatScreenModel,
        'controller': ChatScreenController,
    },
    'settings screen': {
        'model': SettingsScreenModel,
        'controller': SettingsScreenController,
    },
}