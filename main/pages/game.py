from django.utils.translation import gettext_lazy as _
from wagtail.models import PageManager
from wagtail_headless_preview.models import HeadlessPreviewMixin
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from main.blocks.blocks import GameBlock, SPEECH_TYPES
from modelcluster.fields import ParentalManyToManyField, ParentalKey
from wagtail.core.fields import RichTextField, StreamField
import datetime
from wagtail.search import index
from taggit.models import Tag as TaggitTag
from taggit.models import TaggedItemBase
from modelcluster.models import ClusterableModel
from wagtail.core.models import Orderable, Page, TranslatableMixin, Site
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from modelcluster.contrib.taggit import ClusterTaggableManager
from .base import BasePage
from wagtail.snippets.models import register_snippet
from django.conf import settings
from wagtail.api import APIField
#from .models import PagePostCategory, Categories
from main.models import *  # NOQA: F403

class GamePage(HeadlessPreviewMixin, BasePage):
    extra_panels = BasePage.extra_panels
    serializer_class = "main.pages.GamePageSerializer"

    objects: PageManager

    #template = 'cms/game_page.html'
    #parent_page_types = ['cms.GamesIndexPage']
    #subpage_types = ['cms.CardsPage']
    intro = RichTextField(blank=True, help_text="Describe the game theme")
    POS = models.CharField(
        max_length=20, choices=SPEECH_TYPES,
    )
    tags = ClusterTaggableManager(through="main.PostPageTag", blank=True)
    min_recommended_age = models.IntegerField(null=True, blank=True)
    max_recommended_age = models.IntegerField(null=True, blank=True)
    language = models.CharField(max_length=10,
                                choices=settings.LANGUAGES,
                                default=settings.LANGUAGE_CODE)
    post_date = models.DateTimeField(
        verbose_name="Game date", default=datetime.datetime.today)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('POS'),
        MultiFieldPanel([
            FieldPanel('min_recommended_age'),
            FieldPanel('max_recommended_age'),
        ], heading=("Age Recommendation")),
        FieldPanel('language', help_text='original language of the game'),
        InlinePanel("categories1", label="Linguistic difficulty/level"),
        #InlinePanel("categories", label="Linguistic difficulty/level"),
        FieldPanel("tags"),
    ]

    settings_panels = Page.settings_panels + [
        FieldPanel("post_date"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('POS'),
    ]

    extra_panels = BasePage.extra_panels
    serializer_class = "main.pages.GamePageSerializer"

    class Meta:
        verbose_name = _("Game")


    # Game-author is passed through the USERAuth so no need to FK field


class PostPageGameCategory(models.Model):
    page = ParentalKey(
        "main.GamePage", on_delete=models.CASCADE, related_name="categories1"
    )
    game_category = models.ForeignKey(
        "main.GameCategory", on_delete=models.CASCADE, related_name="post_pages"
    )

    panels = [
        FieldPanel("game_category"),
    ]

    @property
    def category_name(self):
        return self.game_category.name

    api_fields = [
        APIField("game_category"),
        APIField("category_name"),
    ]


    class Meta:
        unique_together = ("page", "game_category")


@register_snippet
class GameCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=80)

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


# Tags
class PostPageTag(TaggedItemBase):
    content_object = ParentalKey("GamePage", related_name="post_tags")


@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True
