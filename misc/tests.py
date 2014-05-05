# -*- coding: utf-8 -*-
from logging import getLogger
from django.test import TestCase

from misc.factories import FlatPageFactory


logger = getLogger( __name__ )


class MiscTest(TestCase):
    """ Simple tests for various views in misc app
    """
    def test_simple_flatpage(self):
        page = FlatPageFactory()
        self.assertTrue(
            page.title in unicode(self.client.get(page.url))
        )

    def test_failed_url_flatpage(self):
        self.assertTrue(
            u'404' in unicode(self.client.get('/failed/').url)
        )

    def test_non_existing_template_flatpage(self):
        page = FlatPageFactory(template_name='non-existing-template.html')
        self.assertTrue(
            page.title in unicode(self.client.get(page.url))
        )

    def test_url_without_starting_flash_flatpage(self):
        page = FlatPageFactory()
        print unicode(self.client.get(page.url[1:]))
        self.assertTrue(
            page.title in unicode(self.client.get(page.url))
        )
