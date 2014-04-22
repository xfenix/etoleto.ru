# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from modeldict.models import ModelDict
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill
from dbarray import CharArrayField


""" Misc
"""
class BaseModel(models.Model):
    """ An abstract base class model that provides some base stuff
    """
    class Meta:
        abstract = True

    def __unicode__(self):
        return u"%s" % self.pk


""" Misc models
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
    order = models.PositiveIntegerField(
        verbose_name=u'Сортировка',
    )

    class Meta:
        ordering = ['order']
        verbose_name = u'Меню'
        verbose_name_plural = u'Меню'


class Partners(BaseModel):
    """ Base partners model
    eg. partners in footer
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
    order = models.PositiveIntegerField(
        verbose_name=u'Сортировка',
    )

    def __unicode__(self):
        return u"%s" % self.image

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

    def __unicode__(self):
        return u"%s" % self.title

    class Meta:
        ordering = ['-date']
        verbose_name = u'Рецепт'
        verbose_name_plural = u'Рецепты'


class RecipeIngredients(BaseModel):
    """ Ingredients for recipes
    """ 
    parent = models.ForeignKey(
        Recipe,
        verbose_name=u'Рецепт'
    )
    title = models.TextField(
        verbose_name=u'Описание'
    )
    order = models.PositiveIntegerField(
        verbose_name=u'Сортировка',
    )

    def __unicode__(self):
        return u"%s" % self.title

    class Meta:
        ordering = ['-order']
        verbose_name = u'Ингредиент'
        verbose_name_plural = u'Ингредиенты'


class RecipeImages(BaseModel):
    """ Gallery for recipe model
    """
    parent = models.ForeignKey(
        Recipe,
        related_name='recipeimages',
        verbose_name=u'Рецепт'
    )
    image = models.ImageField(
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
        verbose_name=u'Алиас'
    )
    image = models.ImageField(
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
    )

    def __unicode__(self):
        return u"%s" % self.title

    class Meta:
        ordering = ['order']
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'


class Product(BaseModel):
    """ Base product model
    """
    category = models.ForeignKey(
        ProductCategory,
        verbose_name=u'Продукт'
    )
    title = models.CharField(
        max_length=255,
        verbose_name=u'Название'
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
    image = models.ImageField(
        upload_to=u'productlist',
        verbose_name=u'Изображение',
    )
    # preview for news detail page
    # where gallery is
    list_preview = ImageSpecField(
        source='image',
        processors=[
            ResizeToFill(
                140, 190,
                upscale=False
            )
        ]
    )
    order = models.PositiveIntegerField(
        verbose_name=u'Сортировка',
    )

    def __unicode__(self):
        return u"%s" % self.title

    class Meta:
        ordering = ['order']
        verbose_name = u'Продукт'
        verbose_name_plural = u'Продукты'


class ProductImages(BaseModel):
    """ Gallery for product model
    """
    parent = models.ForeignKey(
        Product,
        related_name='productimages',
        verbose_name=u'Продукт'
    )
    image = models.ImageField(
        upload_to=u'product',
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
    order = models.PositiveIntegerField(
        verbose_name=u'Сортировка',
    )

    def __unicode__(self):
        return u"%s" % self.image

    class Meta:
        ordering = ['order']
        verbose_name = u'Изображение в продукте'
        verbose_name_plural = u'Изображения в продуктах'
