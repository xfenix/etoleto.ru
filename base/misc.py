from django.contrib import admin
from django.db import models
from django.utils import timezone


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


def get_now_tz():
    """ Simple date.now with tz support
    """
    return timezone.now().astimezone(timezone.get_default_timezone())
