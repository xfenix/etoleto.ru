from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from annoying.decorators import render_to

from base.models import News, Recipe, Product, WhereToBuy
from misc.models import MainSlider, custom_settings


try:
    page_size = int(custom_settings.get('PAGE_SIZE'))
except (TypeError, ValueError):
    page_size = 20


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

@render_to('search.html')
def search(request):
    return dict(
        query=request.GET.get('query', '')
    )


"""
Redirect 404 and 500 to flatpages
"""
def error_404(request):
    return redirect('/404/?from=' + request.path)

def error_500(request):
    return redirect('/500/?from=' + request.path)


"""
Class based generic views
"""
class RelatedDetailView(DetailView):
    def get_context_data(self, **kwargs):
        context = super(RelatedDetailView, self).get_context_data(**kwargs)
        context['related'] = self.model.objects\
            .exclude(pk=context['object'].pk)[:2]
        return context

# news
class NewsList(ListView):
    model = News
    template_name = 'news/list.html'
    queryset = News.objects.prefetch_related('images')
    paginate_by = page_size


class NewsDetail(RelatedDetailView):
    model = News
    template_name = 'news/detail.html'


# products
class ProductList(ListView):
    model = Product
    template_name = 'product/list.html'
    paginate_by = page_size


class ProductDetail(DetailView):
    model = Product
    template_name = 'product/detail.html'


# recipes
class RecipeList(ListView):
    model = Recipe
    template_name = 'recipe/list.html'
    paginate_by = page_size


class RecipeDetail(RelatedDetailView):
    model = Recipe
    template_name = 'recipe/detail.html'


# where to buy
class WhereToBuyList(ListView):
    # regroup tag works ONLY with sorted list
    queryset = WhereToBuy.objects.order_by('pos_type')
    template_name = 'wheretobuy/list.html'
