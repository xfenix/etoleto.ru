# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from django_ace import AceWidget
from pilkit.processors import ResizeToFill
from suit.widgets import SuitSplitDateTimeWidget


class BaseModel(models.Model):
    """ An abstract base class model that provides some base stuff
    """
    class Meta:
        abstract = True

    def __unicode__(self):
        return unicode(self.pk)


class BaseModelAdmin(admin.ModelAdmin):
    """ Base admin model class
    """
    def __init__(self, model, admin_site):
        super(BaseModelAdmin, self).__init__(model, admin_site)
        if hasattr(self, 'list_display_over'):
            self.list_display = self.list_display_over
        else:
            self.list_display = [f.name for f in model._meta.fields]
        self.raw_id_fields = [f.name for f in model._meta.fields if isinstance(f, models.ForeignKey)] + \
                             [f.name for f in model._meta.many_to_many if isinstance(f, models.ManyToManyField)]
        self.related_lookup_fields = {
            'fk': [f.name for f in model._meta.fields if isinstance(f, models.ForeignKey)],
            'm2m': [f.name for f in model._meta.many_to_many if isinstance(f, models.ManyToManyField)],
        }
        # see https://github.com/disqus/django-bitfield/issues/28
        #     https://github.com/disqus/django-bitfield/pull/32
        # self.formfield_overrides = {
        #     BitField: {'widget': BitFieldCheckboxSelectMultiple},
        # }
        over = {
            models.DateTimeField: {'widget': SuitSplitDateTimeWidget()},
        }
        ace = True if not hasattr(self, 'ace') else self.ace
        if ace:
            over[models.TextField] = {'widget': AceWidget(mode='html', theme='chrome')}
        self.formfield_overrides = over

    def queryset(self, request):
        return super(BaseModelAdmin, self).queryset(request).select_related(
            *[f.name for f in self.model._meta.fields if isinstance(f, models.ForeignKey)]
        )


class human_app_title(str):
    """ App translation helper
    Usage:
    class Model:
        ...
        class Meta:
            app_label = human_app_title(
                'app_in_lower_case', 'Human title'
            )
    """
    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance

    def title(self):
        return self._title

    __copy__ = lambda self: self
    __deepcopy__ = lambda self, memodict: self


class ImagePreviewWidget(AdminFileWidget):
    """ Image preview field widget
    """
    def __init__(self, thumb_field=None, thumb_size=(100, 100), *args, **kwargs):
        """
        ``thumb_field`` name of field with thumb image. If None will use image itself.
        ``thumb_size`` maximum (width, height) to be displayed. If None original size will be used.
        """
        self.thumb_field = thumb_field
        self.thumb_size = thumb_size
        super(ImagePreviewWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        output = []
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        instance = getattr(value, 'instance', None)
        if instance is not None:
            try:
                field = getattr(instance, value.field.name, None)
                if field:
                    if self.thumb_field is None:
                        thumb_field = field
                    else:
                        thumb_field = getattr(instance, self.thumb_field, None)
                    if self.thumb_size is None:
                        style = ''
                    else:
                        cur_width, cur_height = field.width, field.height
                        thumb_width, thumb_height = self.thumb_size
                        if not thumb_width is None and not thumb_height is None:
                            ratio = min(float(thumb_width) / cur_width,
                                        float(thumb_height) / cur_height)
                        else:
                            if thumb_width is None:
                                ratio = float(thumb_height) / cur_height
                            else:
                                ratio = float(thumb_width) / cur_width
                        new_size = (int(round(cur_width * ratio)), int(round(cur_height * ratio)))
                        if new_size[0] > cur_width or new_size[1] > cur_height:
                            new_size = self.thumb_size
                        style = 'style="width: %spx; height: %spx; "' % new_size
                    output.insert(0, '<div><a target="_blank" href="%s"><img src="%s" alt="%s" %s/></a></div>' % \
                        (field.url, thumb_field.url, field, style))
            except IOError:
                output = ['<div class="errornote">' + _('File access error') + '</div>',] + output
        return mark_safe(u''.join(output))


class ImagePreviewField(models.ImageField):
    """ Image preview model field from django-utilities

    https://github.com/redsolution/django-utilities
    """
    preview_sizes = (100, 100)

    def formfield(self, **kwargs):
        kwargs['widget'] = ImagePreviewWidget
        defaults = {'widget': ImagePreviewWidget(thumb_size=self.preview_sizes)}
        return super(ImagePreviewField, self).formfield(**defaults)

try:
    # add rule for south
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^base\.utils\.ImagePreviewField",])
except ImportError:
    # if we dont have installed south
    # then we dont need to add introspection rule for south
    pass
