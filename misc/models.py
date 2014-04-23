# -*- coding: utf-8 -*-
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill

from base.models import BaseModel


class MainSlider(BaseModel):
    """ Slider for main page
    """
    title = models.CharField(
        max_length=255,
        verbose_name=u'Название (внутреннее)'
    )
    image = models.ImageField(
        upload_to=u'news',
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
    image = models.ImageField(
        upload_to=u'aboutgal',
        verbose_name=u'Изображение',
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
    image = models.ImageField(
        upload_to=u'aboutgal',
        verbose_name=u'Изображение',
    )
    order = models.PositiveIntegerField(
        verbose_name=u'Сортировка',
    )

    class Meta:
        ordering = ['order']
        verbose_name = u'Изображение в галерее'
        verbose_name_plural = u'Изображения в галерее'
