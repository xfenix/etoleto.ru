from django import template
from django.utils.http import urlquote

from misc.models import custom_settings, AboutGalleries


register = template.Library()


# eval tag and class
class EvaluateNode(template.Node):
    def __init__(self, variable):
        self.variable = template.Variable(variable)

    def render(self, context):
        try:
            content = self.variable.resolve(context)
            t = template.Template(content)
            return t.render(context)
        except template.VariableDoesNotExist, template.TemplateSyntaxError:
            return u'Error rendering', self.variable


@register.tag(name='eval')
def do_eval(parser, token):
    """Evals some text like django template
    i'm not sure about good perfomance, that's why
    do not use it often

    tag usage:
    {% eval object.textfield %}
    """
    try:
        tag_name, variable = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, u"%r tag requires a single argument" % token.contents.split()[0]
    return EvaluateNode(variable)


# map link filter
@register.filter(name='map_link')
def map_link(value):
    link = custom_settings.get('SHOW_ON_MAP_LINK', '')
    try:
        return link % dict(shop=urlquote(value))
    except:
        return ''


# about gallery loader
class GalleryNode(template.Node):
    def render(self, context):
        context['about_gals'] = AboutGalleries.objects.prefetch_related('images')
        return ''


@register.tag
def about_gals(parser, token):
    return GalleryNode()
