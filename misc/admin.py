from django.contrib import admin
from suit.admin import SortableModelAdmin, SortableTabularInline

from base.misc import BaseModelAdmin
from misc.forms import FlatpageForm
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


class FlatPageAdmin(admin.ModelAdmin):
    form = FlatpageForm
    list_display = ('url', 'title')
    search_fields = ('url', 'title')


class FlatBlockAdmin(BaseModelAdmin):
    list_display_over = ('slug', 'header', 'content')
    list_display = list_display_over
    list_display_links = list_display_over
    search_fields = ('header', 'content')


admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(MainSlider, MainSliderAdmin)
admin.site.register(AboutGalleries, AboutGalleriesAdmin)
admin.site.register(Partners, PartnersAdmin)

admin.site.unregister(FlatBlock)
admin.site.register(FlatBlockProxy, FlatBlockAdmin)
