from django.contrib import admin
from suit.admin import SortableModelAdmin, SortableTabularInline

from base.misc import BaseModelAdmin
from misc.models import *


class SortableBaseModelAdmin(SortableModelAdmin, BaseModelAdmin):
    pass


class MainSliderAdmin(SortableBaseModelAdmin):
    list_display_over = ('title', 'image')
    list_display = list_display_over
    list_display_links = list_display_over


class AboutGalleriesImagesInline(SortableTabularInline):
    list_display = ('image', 'detail_preview', 'list_preview')
    model = AboutGalleriesImages


class AboutGalleriesAdmin(SortableBaseModelAdmin):
    inline = (AboutGalleriesImagesInline, )
    list_display_over = ('title', 'image')
    list_display = list_display_over
    list_display_links = list_display_over


admin.site.register(MainSlider, MainSliderAdmin)
