from .base_page import BasePageFactory
from ..pages.game import GamePage


class GamePageFactory(BasePageFactory):
    class Meta:
        model = GamePage
