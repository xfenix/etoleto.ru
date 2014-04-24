# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import iri_to_uri
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill
from flatblocks.models import FlatBlock

from base.misc import ImagePreviewField
from base.models import BaseModel


class MainSlider(BaseModel):
    """ Slider for main page
    """
    title = models.CharField(
        max_length=255,
        verbose_name=u'Название (внутреннее)'
    )
    image = ImagePreviewField(
        upload_to=u'mainslider',
        verbose_name=u'Изображение',
    )
    link = models.URLField(
        max_length=255,
        verbose_name=u'Ссылка со слайда',
        null=True,
        blank=True,
    )
    # preview for news detail page
    # where gallery is
    detail_preview = ImageSpecField(
        source='image',
        processors=[
            ResizeToFill(
                width=960,
                upscale=False
            )
        ]
    )
    order = models.PositiveIntegerField(
        verbose_name=u'Сортировка',
    )

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        ordering = ['order']
        verbose_name = u'Слайд на главной странице'
        verbose_name_plural = u'Слайды на главной странице'


class AboutGalleries(BaseModel):
    """ Galleries for about page
    """
    title = models.CharField(
        max_length=255,
        verbose_name=u'Название'
    )
    image = ImagePreviewField(
        upload_to=u'aboutgal',
        verbose_name=u'Превью',
    )
    # preview for news detail page
    # where gallery is
    preview = ImageSpecField(
        source='image',
        processors=[
            ResizeToFill(
                width=270,
                upscale=False
            )
        ]
    )
    order = models.PositiveIntegerField(
        verbose_name=u'Сортировка',
    )

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        ordering = ['order']
        verbose_name = u'Галерея в "о компании"'
        verbose_name_plural = u'Галереи в "о компании"'


class AboutGalleriesImages(BaseModel):
    """ Images for galleries for about page
    """
    parent = models.ForeignKey(
        AboutGalleries,
        verbose_name=u'Галерея'
    )
    title = models.CharField(
        max_length=255,
        verbose_name=u'Название'
    )
    image = ImagePreviewField(
        upload_to=u'about',
        verbose_name=u'Изображение',
    )
    order = models.PositiveIntegerField(
        verbose_name=u'Сортировка',
    )
    # preview for news detail page
    # where gallery is
    preview = ImageSpecField(
        source='image',
        processors=[
            ResizeToFill(
                80, 80,
                upscale=False
            )
        ]
    )

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        ordering = ['order']
        verbose_name = u'Изображение в галерее'
        verbose_name_plural = u'Изображения в галерее'


class Partners(BaseModel):
    """ Base partners model eg. partners in footer
    """
    title = models.CharField(
        max_length=255,
        verbose_name=u'Название'
    )
    logo = ImagePreviewField(
        upload_to=u'partners',
        verbose_name=u'Изображение',
    )
    link = models.URLField(
        max_length=255,
        verbose_name=u'Ссылка с логотипа',
        null=True,
        blank=True,
    )
    # preview for news detail page
    # where gallery is
    preview = ImageSpecField(
        source='logo',
        processors=[
            ResizeToFit(
                height=60,
                upscale=False
            )
        ]
    )
    order = models.PositiveIntegerField(
        verbose_name=u'Сортировка',
        default=0,
    )

    def __unicode__(self):
        return unicode(self.logo)

    class Meta:
        verbose_name = u'Партнёр'
        verbose_name_plural = u'Партнёры'


class FlatBlockProxy(FlatBlock):
    """ Proxying flatblocks model to experience better admin ui
    """
    class Meta:
        proxy = True
        verbose_name = u'Блок текста'
        verbose_name_plural = u'Блоки текста'


class FlatPage(models.Model):
    """ Custom flatPage
    rewrite of https://github.com/django/django/blob/master/django/contrib/flatpages/
    """
    url = models.CharField(u'URL', max_length=255, db_index=True)
    title = models.CharField(u'Название', max_length=255)
    content = models.TextField(u'Содержимое', blank=True)
    template_name = models.CharField(
        u'Шаблон', max_length=70, blank=True,
        help_text=u"Например: 'flatpages/contact_page.html'. Если оставить пустым, используется 'flatpages/default.html'."
    )

    class Meta:
        verbose_name = u'Простая страница'
        verbose_name_plural = u'Простые страницы'
        ordering = ('url',)

    def __str__(self):
        return "%s -- %s" % (self.url, self.title)

    def get_absolute_url(self):
        # Handle script prefix manually because we bypass reverse()
        return iri_to_uri(get_script_prefix().rstrip('/') + self.url)
