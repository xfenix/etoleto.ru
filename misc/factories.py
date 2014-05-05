# -*- coding: utf-8 -*-
import factory
from factory import fuzzy

from misc import models


""" Misc data factories for test purposes
"""
class FuzzyUrl(fuzzy.BaseFuzzyAttribute):
    factory_name = fuzzy.FuzzyText(length=100)

    def fuzz(self):
        return '/%s/' % self.factory_name.fuzz()


class FlatPageFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = models.FlatPage
    url = FuzzyUrl()
    title = fuzzy.FuzzyText(length=50)
    content = fuzzy.FuzzyText(length=300)
    template_name = 'default.html'
