from .base_serializer import BasePageSerializer
from . import GamePage


class GamePageSerializer(BasePageSerializer):
    class Meta:
        model = GamePage
        fields = BasePageSerializer.Meta.fields + [
            "intro",
            "POS",
            "min_recommended_age",
            "max_recommended_age",
            "language",
            "categories1",
        ]
