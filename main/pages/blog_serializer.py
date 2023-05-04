from .base_serializer import BasePageSerializer
from . import BlogPage


class BlogPageSerializer(BasePageSerializer):
    class Meta:
        model = BlogPage
        fields = BasePageSerializer.Meta.fields + [
            "intro",
            "body",
        ]
