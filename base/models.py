# -*- coding: utf-8 -*-
from django.db import models
from modeldict.models import ModelDict
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill

from base.misc import get_now_tz


""" Misc
"""
class BaseModel(models.Model):
    """ An abstract base class model that provides some base stuff
    """
    class Meta:
        abstract = True

    def __unicode__(self):
        return u"%s" % self.pk


""" All models
"""
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
    order = models.IntegerField(
        verbose_name=u'Сортировка',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['order']
        verbose_name = u'Меню'
        verbose_name_plural = u'Меню'


class News(BaseModel):
    """ Base news model
    """
    title = models.CharField(
        max_length=255,
        verbose_name=u'Название'
    )
    date = models.DateTimeField(
        max_length=255,
        verbose_name=u'Дата',
        default=get_now_tz,
    )
    short_descr = models.TextField(
        verbose_name=u'Краткий текст новости',
        null=True,
        blank=True,
        help_text=u"""Краткий текст для главной страницы и страницы новостей""",
    )
    descr = models.TextField(
        verbose_name=u'Текст новости',
    )

    def __unicode__(self):
        return u"%s" % self.title

    class Meta:
        ordering = ['-date']
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'


class NewsImages(BaseModel):
    """ Gallery for news model
    """
    parent = models.ForeignKey(
        News,
        related_name='newsimages',
        verbose_name=u'Новость'
    )
    image = models.ImageField(
        upload_to=u'news',
        verbose_name=u'Изображение',
    )
    # preview for news detail page
    # where gallery is
    detail_preview = ImageSpecField(
        source='image',
        processors=[
            ResizeToFill(
                81, 80,
                upscale=False
            )
        ]
    )
    # preview for news list page
    # and main page
    list_preview = ImageSpecField(
        source='image',
        processors=[
            ResizeToFill(
                190, 180,
                upscale=False
            )
        ]
    )

    def __unicode__(self):
        return u"%s" % self.image

    class Meta:
        verbose_name = u'Изображение в новость'
        verbose_name_plural = u'Изображения в новости'


class Recipe(BaseModel):
    """ Base news model
    """
    title = models.CharField(
        max_length=255,
        verbose_name=u'Название'
    )
    date = models.DateTimeField(
        max_length=255,
        verbose_name=u'Дата',
        default=get_now_tz,
    )
    short_descr = models.TextField(
        verbose_name=u'Краткий текст новости',
        null=True,
        blank=True,
        help_text=u"""Краткий текст для главной страницы и страницы новостей""",
    )
    descr = models.TextField(
        verbose_name=u'Текст новости',
    )

    def __unicode__(self):
        return u"%s" % self.title

    class Meta:
        ordering = ['-date']
        verbose_name = u'Рецепт'
        verbose_name_plural = u'Рецепты'


class RecipeImages(BaseModel):
    """ Gallery for news model
    """
    parent = models.ForeignKey(
        Recipe,
        related_name='recipeimages',
        verbose_name=u'Рецепт'
    )
    image = models.ImageField(
        upload_to=u'news',
        verbose_name=u'Изображение',
    )
    # preview for news detail page
    # where gallery is
    detail_preview = ImageSpecField(
        source='image',
        processors=[
            ResizeToFill(
                81, 80,
                upscale=False
            )
        ]
    )
    # preview for news list page
    # and main page
    list_preview = ImageSpecField(
        source='image',
        processors=[
            ResizeToFill(
                190, 180,
                upscale=False
            )
        ]
    )

    def __unicode__(self):
        return u"%s" % self.image

    class Meta:
        verbose_name = u'Изображение в новость'
        verbose_name_plural = u'Изображения в новости'


class Partners(BaseModel):
    """ Base partners model
    """
    logo = models.ImageField(
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

    def __unicode__(self):
        return u"%s" % self.image

    class Meta:
        verbose_name = u'Партнёр'
        verbose_name_plural = u'Партнёры'
