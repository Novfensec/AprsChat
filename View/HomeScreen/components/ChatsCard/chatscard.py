from kivymd.uix.card import MDCard
from kivy.properties import StringProperty


class ChatsCard(MDCard):
    chatusername = StringProperty()

    def __init__(self, *args, **kwargs):
        super(ChatsCard, self).__init__(*args, **kwargs)
