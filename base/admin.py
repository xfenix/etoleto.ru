# -*- coding: utf-8 -*-
from suit.admin import SortableModelAdmin
from django.contrib import admin

from base.misc import BaseModelAdmin
from base.models import *


class MenuAdmin(SortableModelAdmin, BaseModelAdmin):
    list_display_over = ('title', 'path', )
    list_display = list_display_over
    list_editable = ('path', )
    sortable = 'order'


class NewsImagesInline(admin.TabularInline):
    list_display = ('image', 'detail_preview', 'list_preview')
    model = NewsImages


class NewsAdmin(BaseModelAdmin):
    inlines = (NewsImagesInline,)
    list_display_over = ('title', 'date')
    list_display = list_display_over
    list_display_links = list_display_over


admin.site.register(Menu, MenuAdmin)
admin.site.register(News, NewsAdmin)
