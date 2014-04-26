# -*- coding: utf-8 -*-
import os
import glob
from django.core.cache import cache
from django.db import models
from django.conf import settings
from django.utils.encoding import iri_to_uri
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill
from flatblocks.models import FlatBlock
from modeldict.models import ModelDict

from base.misc import ImagePreviewField
from base.models import BaseModel


class Setting(BaseModel):
    """ Misc settings
    """
    key = models.CharField(
        max_length=100,
        verbose_name=u'Ключ',
        db_index=True
    )
    value = models.TextField(
        verbose_name=u'Значение'
    )

    def __unicode__(self):
        return unicode(self.key)

    class Meta:
        verbose_name = u'Настройка'
        verbose_name_plural = u'Настройки'

custom_settings = ModelDict(Setting, key='key', value='value', instances=False)


class Menu(BaseModel):
    """ Main site menu
    """
    title = models.CharField(
        max_length=255,
        verbose_name=u'Название'
    )
    path = models.CharField(
        max_length=255,
        verbose_name=u'Путь',
        db_index=True
    )
    order = models.PositiveIntegerField(
        verbose_name=u'Сортировка',
    )

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        ordering = ['order']
        verbose_name = u'Меню'
        verbose_name_plural = u'Меню'


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


def get_avail_tpls():
    """ Scan flatpages directory in template folder
    and then returns list of all available templates
    """
    key = 'flattemplates'
    cached = cache.get(key)
    if cached:
        return cached
    try:
        tpl_dir = settings.TEMPLATE_DIRS[0]
    except IndexError:
        return ()
    try:
        templates = glob.glob(
            os.path.join(
                tpl_dir, settings.FLATPAGE_TPL_DIR, '*.html'
            )
        )
    except TypeError:
        return []
    choices = []
    for tpl in templates:
        choices.append(
            (os.path.split(tpl)[-1], os.path.split(tpl)[-1])
        )
    cache.set(key, choices)
    return choices


class FlatPage(models.Model):
    """ Custom flatPage
    rewrite of https://github.com/django/django/blob/master/django/contrib/flatpages/
    """
    url = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name=u'URL',
    )
    title = models.CharField(
        max_length=255,
        verbose_name=u'Название',
    )
    content = models.TextField(
        verbose_name=u'Содержимое',
        blank=True,
    )
    template_name = models.CharField(
        u'Шаблон', max_length=255,
        help_text=u"Выберите из списка доступных шаблонов (директория /templates/%s/)" % settings.FLATPAGE_TPL_DIR,
        choices=get_avail_tpls(),
        default=dict(get_avail_tpls())[settings.FLATPAGE_DEFAULT_TPL],
    )

    class Meta:
        verbose_name = u'Простая страница'
        verbose_name_plural = u'Простые страницы'
        ordering = ('url',)

    def __unicode__(self):
        return u"%s -- %s" % (self.url, unicode(self.title))

    def get_template(self, default=False):
        """ return relative path to flatpage template
        """
        return os.path.join(
            settings.FLATPAGE_TPL_DIR,
            settings.FLATPAGE_DEFAULT_TPL if default else self.template_name
        )

    def get_absolute_url(self):
        # Handle script prefix manually because we bypass reverse()
        return iri_to_uri(get_script_prefix().rstrip('/') + self.url)
