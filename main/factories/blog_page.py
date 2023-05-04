from .base_page import BasePageFactory
from ..pages.blog import BlogPage


class BlogPageFactory(BasePageFactory):
    class Meta:
        model = BlogPage
