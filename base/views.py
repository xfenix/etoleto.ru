from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from annoying.decorators import render_to
from base.models import News


"""
Plain old style views
"""
@render_to('index.html')
def index(request):
    return dict(
    )

@render_to('index.html')
def base(request):
    return dict(
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
class NewsList(ListView):
    model = News
    queryset = News.objects.prefetch_related('images')


class NewsDetailView(DetailView):
    model = News
