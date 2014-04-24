# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings

from misc.models import FlatPage


class FlatpageForm(forms.ModelForm):
    url = forms.RegexField(
        label=u'URL', max_length=255, regex=r'^[-\w/\.~]+$',
        help_text=u"Например: '/about/contact/'. Убедитесь, что вы добавили слеш в начало и конец",
        error_message=u"URL может состоять из букв английского алфавита, цифр, "
                      u"точек, подчёркиваний, дефисов, слешей или тильд"
    )

    class Meta:
        model = FlatPage
        fields = '__all__'

    def clean_url(self):
        url = self.cleaned_data['url']
        if not url.startswith('/'):
            raise forms.ValidationError(
                "URL не имеет завершающего слеша",
                code='missing_leading_slash',
            )
        if (settings.APPEND_SLASH and
                'django.middleware.common.CommonMiddleware' in settings.MIDDLEWARE_CLASSES and
                not url.endswith('/')):
            raise forms.ValidationError(
                ugettext("URL не имеет слеша в начале"),
                code='missing_trailing_slash',
            )
        return url

    def clean(self):
        url = self.cleaned_data.get('url', None)
        sites = self.cleaned_data.get('sites', None)

        same_url = FlatPage.objects.filter(url=url)
        if self.instance.pk:
            same_url = same_url.exclude(pk=self.instance.pk)

        if same_url.exists():
            raise forms.ValidationError(
                'Flatpage with url %(url)s already exists for site %(site)s',
                code='duplicate_url',
                params={'url': url, 'site': site},
            )

        return super(FlatpageForm, self).clean()
