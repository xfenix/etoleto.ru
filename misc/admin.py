from django.contrib import admin
from suit.admin import SortableModelAdmin, SortableTabularInline

from base.admin import BaseModelAdmin, SortableBaseModelAdmin
from misc.forms import FlatpageForm
from misc.models import *


class MenuAdmin(SortableBaseModelAdmin):
    list_display_over = ('id', 'title', 'path', )
    list_display = list_display_over
    list_editable = ('path', 'title', )
    list_display_links = ('id', )


class SettingAdmin(BaseModelAdmin):
    list_display_over = ('key', 'value')
    list_display = list_display_over


class MainSliderAdmin(SortableBaseModelAdmin):
    list_display_over = ('title', 'image')
    list_display = list_display_over
    list_display_links = list_display_over


class AboutGalleriesImagesInline(SortableTabularInline):
    list_display = ('image', 'detail_preview', 'list_preview')
    model = AboutGalleriesImages
    extra = 0


class AboutGalleriesAdmin(SortableBaseModelAdmin):
    inlines = (AboutGalleriesImagesInline, )
    list_display_over = ('title', 'image')
    list_display = list_display_over
    list_display_links = list_display_over


class PartnersAdmin(SortableBaseModelAdmin):
    list_display_over = ('title', 'logo')
    list_display = list_display_over
    list_display_links = list_display_over


class FlatPageAdmin(BaseModelAdmin):
    form = FlatpageForm
    list_display_over = ('url', 'title', 'template_name')
    list_display = list_display_over
    list_display_links = list_display_over
    search_fields = ('url', 'title')


class FlatBlockAdmin(BaseModelAdmin):
    list_display_over = ('slug', 'header')
    list_display = list_display_over
    list_display_links = list_display_over
    search_fields = ('header', 'content')


admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(MainSlider, MainSliderAdmin)
admin.site.register(AboutGalleries, AboutGalleriesAdmin)
admin.site.register(Partners, PartnersAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(Menu, MenuAdmin)

admin.site.unregister(FlatBlock)
admin.site.register(FlatBlockProxy, FlatBlockAdmin)
