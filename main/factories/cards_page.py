from .base_page import BasePageFactory
from ..pages.cards import CardsPage


class CardsPageFactory(BasePageFactory):
    class Meta:
        model = CardsPage
