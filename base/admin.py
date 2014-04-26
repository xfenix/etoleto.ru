# -*- coding: utf-8 -*-
from suit.admin import SortableModelAdmin, SortableTabularInline
from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe

from base.misc import BaseModelAdmin
from base.models import *


class SortableBaseModelAdmin(SortableModelAdmin, BaseModelAdmin):
    pass


class NewsImagesInline(SortableTabularInline):
    list_display = ('image', 'detail_preview', 'list_preview')
    model = NewsImages
    extra = 0


class NewsAdmin(BaseModelAdmin):
    inlines = (NewsImagesInline,)
    list_display_over = ('title', 'date')
    list_display = list_display_over
    list_display_links = list_display_over


class RecipeImagesInline(SortableTabularInline):
    list_display = ('image', 'detail_preview', 'list_preview')
    model = RecipeImages
    suit_classes = 'suit-tab suit-tab-general'
    extra = 0


class RecipeIngredientsInline(SortableTabularInline):
    model = RecipeIngredients
    suit_classes = 'suit-tab suit-tab-ingr'
    extra = 0


class RecipeAdmin(BaseModelAdmin):
    inlines = (RecipeIngredientsInline, RecipeImagesInline, )
    list_display_over = ('title', 'date')
    list_display = list_display_over
    list_display_links = list_display_over
    fieldsets = [
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['title', 'slug', 'date', 'short_descr', 'instruction', 'note']
        }),
        (None, {
            'classes': ('suit-tab suit-tab-ingr',),
            'fields': ['ingredients_prefix']}),
    ]
    suit_form_tabs = (
        ('general', 'Основное'), ('ingr', 'Ингредиенты')
    )


class ProductCategoryAdmin(SortableBaseModelAdmin):
    list_display_over = ('title', 'slug', 'image')
    list_display = list_display_over
    list_display_links = list_display_over


class ProductAdmin(SortableBaseModelAdmin):
    list_display_over = ('category', 'title', 'weight', 'image')
    list_display = list_display_over
    list_display_links = list_display_over


class WhereToBuyAdmin(SortableBaseModelAdmin):
    list_display_over = ('title', 'pos_type', 'image')
    list_display = list_display_over
    list_display_links = list_display_over


admin.site.register(News, NewsAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(WhereToBuy, WhereToBuyAdmin)
