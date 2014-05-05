# -*- coding: utf-8 -*-
from logging import getLogger

from django.test import TestCase
from django.db.models.loading import cache


logger = getLogger( __name__ )


class BaseTest(TestCase):
    """ Simple tests for various views in base app
    """
    pass


class TestUnicodeMethods(TestCase):
    def test_all(self):
        """ Sanity check on unicode methods.
        You catch a surprising number
        of errors (especially in the early stages of development) just by
        calling the unicode method on every object for every model.
        """
        no_unicode_tests = ['MigrationHistory', 'Rule', 'Session', 'LogEntry']
        for model in cache.get_models():
            meta = model._meta
            if meta.object_name not in no_unicode_tests:
                objs = model.objects.all()
                for obj in objs:
                    unic = obj.__unicode__()
                    self.assertTrue(unic)
                    logger.info(unic)
