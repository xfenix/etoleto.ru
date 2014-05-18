# vim:fileencoding=utf-8
from hashlib import sha1
from django.core.cache import cache
from django.conf import settings
from cache_utils.decorators import cached

from misc.models import Menu, Partners, custom_settings


# @cached(86400)
def process(request):
    """ default context processor
    add menu, partners and other wide site data
    """
    return dict(
        menu=Menu.objects.all(),
        partners=Partners.objects.all(),
        request=request,
        debug=settings.DEBUG,
        ismain=False if request.path.strip('/') else True,
        counter_yandex=custom_settings.get('COUNTER_YANDEX', ''),
        counter_google=custom_settings.get('COUNTER_GOOGLE', ''),
    )
