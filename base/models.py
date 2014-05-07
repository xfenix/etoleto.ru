# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from django.core.urlresolvers import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import *

from base.utils import ImagePreviewField, BaseModel


"""
News models
"""
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
        default=datetime.today,
    )
    image = ImagePreviewField(
        upload_to=u'news',
        verbose_name=u'Изображение',
    )
    # preview for news list page
    # and main page
    preview = ImageSpecField(
        source='image',
        processors=[
            ResizeToFit(180, 180, upscale=False),
            ResizeCanvas(180, 180)
        ]
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
        return unicode(self.title)

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-date']
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'


class NewsImages(BaseModel):
    """ Gallery for news model
    """
    parent = models.ForeignKey(
        News,
        related_name='images',
        verbose_name=u'Новость'
    )
    image = ImagePreviewField(
        upload_to=u'newsgal',
        verbose_name=u'Изображение',
    )
    # preview for news detail page
    # where gallery is
    preview = ImageSpecField(
        source='image',
        processors=[
            ResizeToFill(
                81, 80,
                upscale=False
            )
        ]
    )
    order = models.PositiveIntegerField(
        verbose_name=u'Сортировка',
        default=0,
    )

    def __unicode__(self):
        return unicode(self.image)

    class Meta:
        verbose_name = u'Изображение в новость'
        verbose_name_plural = u'Изображения в новости'

"""
Recipes models
"""
class Recipe(BaseModel):
    """ Base recipe model
    """
    title = models.CharField(
        max_length=255,
        verbose_name=u'Название'
    )
    slug = models.SlugField(
        max_length=255,
        verbose_name=u'Алиас для URL'
    )
    date = models.DateTimeField(
        max_length=255,
        verbose_name=u'Дата',
        default=datetime.today,
    )
    short_descr = models.TextField(
        verbose_name=u'Краткий текст рецепта',
        null=True,
        blank=True,
        help_text=u"""Краткий текст для главной страницы и страницы рецептов""",
    )
    image = ImagePreviewField(
        upload_to=u'news',
        verbose_name=u'Изображение',
    )
    # preview for recipe list page
    # and main page
    preview = ImageSpecField(
        source='image',
        processors=[
            ResizeToFit(180, 180, upscale=False),
            ResizeCanvas(180, 180)
        ]
    )
    ingredients_prefix = models.TextField(
        verbose_name=u'Краткий текст перед ингредиентами',
        null=True,
        blank=True,
        help_text=u"""А сами ингредиенты чуть ниже""",
    )
    instruction = models.TextField(
        verbose_name=u'Инструкция',
        null=True,
        blank=True,
    )
    note = models.TextField(
        verbose_name=u'Примечание',
        null=True,
        blank=True,
    )

    def get_absolute_url(self):
        return reverse('recipes-detail', kwargs={'slug': self.slug})

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        ordering = ['-date']
        verbose_name = u'Рецепт'
        verbose_name_plural = u'Рецепты'


class RecipeIngredients(BaseModel):
    """ Ingredients for recipes
    """ 
    parent = models.ForeignKey(
        Recipe,
        related_name='ingridients',
        verbose_name=u'Рецепт'
    )
    title = models.TextField(
        verbose_name=u'Описание'
    )
    order = models.PositiveIntegerField(
        verbose_name=u'Сортировка',
        default=0,
    )

    def __unicode__(self):
        return u"%s" % self.title[:100]

    class Meta:
        ordering = ['-order']
        verbose_name = u'Ингредиент'
        verbose_name_plural = u'Ингредиенты'


class RecipeImages(BaseModel):
    """ Gallery for recipe model
    """
    parent = models.ForeignKey(
        Recipe,
        related_name='images',
        verbose_name=u'Рецепт'
    )
    image = ImagePreviewField(
        upload_to=u'recipe',
        verbose_name=u'Изображение',
    )
    # preview for recipe detail page
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
    # preview for recipe list page
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
    order = models.PositiveIntegerField(
        verbose_name=u'Сортировка',
        default=0,
    )

    def __unicode__(self):
        return u"%s" % self.image

    class Meta:
        verbose_name = u'Изображение в рецепте'
        verbose_name_plural = u'Изображения в рецептах'


"""
Products models
"""
class ProductCategory(BaseModel):
    """ Base product category model
    """
    title = models.CharField(
        max_length=255,
        verbose_name=u'Название'
    )
    slug = models.SlugField(
        max_length=255,
        verbose_name=u'Алиас для URL'
    )
    image = ImagePreviewField(
        upload_to=u'category',
        verbose_name=u'Изображение',
    )
    preview = ImageSpecField(
        source='image',
        processors=[
            ResizeToFill(
                120, 170,
                upscale=False
            )
        ]
    )
    order = models.PositiveIntegerField(
        verbose_name=u'Сортировка',
        default=0,
    )

    def get_absolute_url(self):
        return reverse('products-category', kwargs={'slug': self.slug})

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        ordering = ['order']
        verbose_name = u'Продукты: категория'
        verbose_name_plural = u'Продукты: категории'


class Product(BaseModel):
    """ Base product model
    """
    category = models.ForeignKey(
        ProductCategory,
        verbose_name=u'Категория продукта'
    )
    title = models.CharField(
        max_length=255,
        verbose_name=u'Название'
    )
    slug = models.SlugField(
        max_length=255,
        verbose_name=u'Алиас для URL'
    )
    short_descr = models.TextField(
        verbose_name=u'Краткий текст продукта',
        null=True,
        blank=True,
        help_text=u"""Краткий текст для внутреней страницы продукта""",
    )
    weight = models.CharField(
        max_length=255,
        verbose_name=u'Вес (объём) продукта',
        null=True,
        blank=True,
        help_text=u"""Например: 750 грамм или 500 мл""",
    )
    composition = models.TextField(
        verbose_name=u'Состав',
        null=True,
        blank=True,
        help_text=u"""Например: молоко сухое, молоко цельное, закваска""",
    )
    calories = models.CharField(
        max_length=255,
        verbose_name=u'Энергетическая ценность (на 100 грамм)'
    )
    proteins = models.CharField(
        max_length=255,
        verbose_name=u'Белки (на 100 грамм)'
    )
    fats = models.CharField(
        max_length=255,
        verbose_name=u'Жиры (на 100 грамм)'
    )
    carbs = models.CharField(
        max_length=255,
        verbose_name=u'Углеводы (на 100 грамм)'
    )
    storage = models.TextField(
        verbose_name=u'Хранение',
        null=True,
        blank=True
    )
    recipes = models.ManyToManyField(
        Recipe,
        verbose_name=u'Блюда с этим продуктом',
    )
    image = ImagePreviewField(
        upload_to=u'productlist',
        verbose_name=u'Изображение',
    )
    # preview for news detail page
    # where gallery is
    preview = ImageSpecField(
        source='image',
        processors=[
            ResizeToFit(
                140, 140,
                upscale=False
            ),
            ResizeCanvas(140, 140)
        ]
    )
    order = models.PositiveIntegerField(
        verbose_name=u'Сортировка',
        default=0,
    )

    def get_absolute_url(self):
        return reverse('products-detail', kwargs={'slug': self.slug})

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        ordering = ['order']
        verbose_name = u'Продукт'
        verbose_name_plural = u'Продукты'


class ProductImages(BaseModel):
    """ Gallery for product model
    """
    parent = models.ForeignKey(
        Product,
        related_name='images',
        verbose_name=u'Продукт'
    )
    image = ImagePreviewField(
        upload_to=u'product',
        verbose_name=u'Изображение',
    )
    preview = ImageSpecField(
        source='image',
        processors=[
            ResizeToFill(
                81, 80,
                upscale=False
            )
        ]
    )
    preview_big = ImageSpecField(
        source='image',
        processors=[
            SmartResize(
                360, 400,
                upscale=False
            ),
            ResizeCanvas(360, 400)
        ]
    )
    order = models.PositiveIntegerField(
        verbose_name=u'Сортировка',
        default=0,
    )

    def __unicode__(self):
        return unicode(self.image)

    class Meta:
        ordering = ['order']
        verbose_name = u'Изображение в продукте'
        verbose_name_plural = u'Изображения в продуктах'


"""
And other models
"""
class WhereToBuy(BaseModel):
    """ WhereToBuy model
    """
    POS_TYPES = (
        (0, 'Торговая сеть'),
        (1, 'Интернет-магазин'),
    )
    title = models.CharField(
        max_length=255,
        verbose_name=u'Название',
        help_text=u"""Для торговой сети передаётся google карте в неизменном виде. """
                  u"""Поэтому обязательно проверяйте корректность заполнения этого поля.""",
    )
    pos_type = models.IntegerField(
        default=0,
        choices=POS_TYPES,
        verbose_name=u'Тип магазина'
    )
    image = ImagePreviewField(
        upload_to=u'category',
        verbose_name=u'Изображение',
    )
    link = models.URLField(
        max_length=255,
        verbose_name=u'Ссылка',
        help_text=u"""Ссылка в формате http://somedomain.ru/<br />Если необходимо """
                  u"""поставить ссылку на локальный ресурс, то необходимо внести её """
                  u"""в таком же формате.""",
        null=True,
        blank=True,
    )
    preview = ImageSpecField(
        source='image',
        processors=[
            ResizeToFit(
                177, 94,
                upscale=False
            ),
            ResizeCanvas(177, 94)
        ]
    )
    order = models.PositiveIntegerField(
        verbose_name=u'Сортировка',
        default=0,
    )

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        ordering = ['order']
        verbose_name = u'Точка в "где купить"'
        verbose_name_plural = u'Точки в "где купить"'
