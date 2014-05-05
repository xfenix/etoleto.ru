from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from annoying.decorators import render_to

from base.models import News, Recipe, Product, WhereToBuy
from misc.models import MainSlider, custom_settings


"""
Plain old style views
"""
@render_to('index.html')
def index(request):
    return dict(
        news=News.objects.all()[:1],
        recipes=Recipe.objects.all()[:1],
        slides=MainSlider.objects.all(),
    )


"""
Redirect 404 and 500 to flatpages
"""
def error_404(request):
    return redirect('/404/?from=' + request.path)

def error_500(request):
    return redirect('/500/?from=' + request.path)


"""
CBG views
"""
class NewsList(ListView):
    """ news list page
    """
    model = News
    template_name = 'news/list.html'
    queryset = News.objects.prefetch_related('images')
    paginate_by = 20


class NewsDetailView(DetailView):
    """ detail news page 
    """
    model = News
    template_name = 'news/detail.html'

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['related'] = News.objects.exclude(pk=context['object'].pk)[:2]
        return context


class ProductList(ListView):
    """ news list page
    """
    model = Product
    template_name = 'product/list.html'
    queryset = News.objects.prefetch_related('images')
    paginate_by = 20


class WhereToBuyList(ListView):
    """ news list page
    """
    # regroup tag works ONLY with sorted list
    queryset = WhereToBuy.objects.order_by('pos_type')
    template_name = 'wheretobuy/list.html'
