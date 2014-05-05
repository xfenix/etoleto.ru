# -*- coding: utf-8 -*-
import os
from logging import getLogger
from django.conf import settings
from django.core.cache import cache
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404
from django.template import loader, RequestContext, TemplateDoesNotExist
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from misc.models import FlatPage


logger = getLogger( __name__ )


def flatpage(request, url):
    """ Public interface to the flat page view.

    Models: `flatpages.flatpages`
    Templates: Uses the template defined by the ``template_name`` field,
        or :template:`flatpages/default.html` if template_name is not defined.
    Context:
        flatpage
            `flatpages.flatpages` object
    """
    if not url.startswith('/'):
        url = '/' + url
    try:
        flatpage = get_object_or_404(FlatPage, url=url)
    except Http404:
        if not url.endswith('/') and settings.APPEND_SLASH:
            url += '/'
            flatpage = get_object_or_404(FlatPage, url=url)
            return HttpResponsePermanentRedirect('%s/' % request.path)
        else:
            raise
    try:
        template = loader.get_template(flatpage.get_template())
    except TemplateDoesNotExist:
        logger.error(
            u'Template %s doesnt exists, loaded default' % flatpage.get_template()
        )
        template = loader.get_template(flatpage.get_template(True))
    # To avoid having to always use the "|safe" filter in flatpage templates,
    # mark the title and content as already safe (since they are raw HTML
    # content in the first place).
    flatpage.title = mark_safe(flatpage.title)
    flatpage.content = mark_safe(flatpage.content)
    c = RequestContext(request, {'flatpage': flatpage,})
    response = HttpResponse(template.render(c))
    return response


""" Other views
"""
@login_required
@never_cache
def clear_cache(request):
    """ special admin view for cache clearing
    """
    cache.clear()
    return HttpResponse('ok', content_type='text/plain')
