from django.db import models

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.search import index
from taggit.models import TaggedItemBase


class BlogTagIndexPage(Page):
    def get_context(self, request):
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context


class BlogIndexPage(Page):
    def get_context(self, request):
        """Gets published BlobPage content and orders in reverse chronoglogical order"""
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
        ], heading="Blog information"),
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
    ]
