# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.http import Http404
from annoying.decorators import render_to

from base.models import News, Recipe, Product, WhereToBuy, ProductCategory
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
        categories=ProductCategory.objects.all()[:6],
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
    paginate_by = page_size


class NewsDetail(RelatedDetailView):
    model = News
    template_name = 'news/detail.html'


# products
class ProductList(ListView):
    model = Product
    template_name = 'product/list.html'
    paginate_by = page_size
    error_text = u'Нет указанной категории'

    def get_queryset(self):
        qset = super(ProductList, self).get_queryset()
        # logic for categories
        # serving urls like /products/category/slug/
        if 'slug' in self.kwargs:
            self.category = self.kwargs['slug']
            qset = qset.filter(category__slug=self.kwargs['slug'])
            if not qset:
                raise Http404(self.error_text)
        return qset

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        category = None
        if hasattr(self, 'category'):
            try:
                category = ProductCategory.objects.get(slug=self.category)
            except ProductCategory.DoesNotExist:
                raise Http404(self.error_text)
        context['category'] = category
        return context


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
