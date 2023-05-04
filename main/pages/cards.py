from django.db import models
from main.blocks.blocks import CardBlock, GameBlock
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail_headless_preview.models import HeadlessPreviewMixin
from wagtail.core.fields import RichTextField, StreamField
import datetime
from django.conf import settings

from .base import BasePage


class CardsPage(HeadlessPreviewMixin, BasePage):
    #parent_page_types = ['pages.GamePage']
    subpage_types = []
    #template = 'cms/cards_page.html'
    intro = RichTextField(blank=True, help_text="Describe the cars group's linguistic theme", verbose_name=_("Intro"))
    # Part of speech could be streanmed with snippetsg? to explore
    cards = StreamField([
        ('card', CardBlock(form_classname="card")),
    ], max_num=4, min_num=4, use_json_field=True)

    card_title = models.CharField(max_length=20, null=True, blank=True, )
    card_subtitle = models.CharField(max_length=20, null=True, blank=True,
                                     help_text="another text string can be used as hint, En translation, etc'")
    min_recommended_age = models.IntegerField(null=True, blank=True)
    max_recommended_age = models.IntegerField(null=True, blank=True)
    language = models.CharField(max_length=10,
                                choices=settings.LANGUAGES,
                                default=settings.LANGUAGE_CODE)
    post_date = models.DateTimeField(
        verbose_name="Game date", default=datetime.datetime.today)

    content_panels = BasePage.content_panels + [
        FieldPanel('intro'),
        FieldPanel('cards'),
        FieldPanel('card_title'),
        FieldPanel('min_recommended_age'),
        FieldPanel('max_recommended_age'),
        FieldPanel('language'),
    ]

    """search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('cards'),
    ]"""

    extra_panels = BasePage.extra_panels
    serializer_class = "main.pages.CardsPageSerializer"

    class Meta:
        verbose_name = _("Cards")
