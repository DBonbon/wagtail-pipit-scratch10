from django.utils.translation import gettext_lazy as _
from wagtail.models import PageManager
from wagtail_headless_preview.models import HeadlessPreviewMixin
from wagtail.core.fields import RichTextField, StreamField
from main.blocks.blocks import ImageWithTextBlock, CardBlock, GameBlock, CustomImageChooserBlock
from wagtail.admin.panels import FieldPanel

from .base import BasePage
from django.db import models


class BlogPage(HeadlessPreviewMixin, BasePage):
    extra_panels = BasePage.extra_panels
    serializer_class = "main.pages.BlogPageSerializer"
    intro = models.CharField(max_length=20, null=True, blank=True, )
    #date = models.DateField("Post date")
    # summary = RichTextField()
    body = StreamField(
        [
            ("text_and_buttons", ImageWithTextBlock()),
        ]
    )

    content_panels = BasePage.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
    ]

    objects: PageManager

    class Meta:
        verbose_name = _("Blog")
