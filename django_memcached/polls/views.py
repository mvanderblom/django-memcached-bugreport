from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)
def index(request):
    print('rendering view')
    return HttpResponse("Hello, world. You're at the polls index.")