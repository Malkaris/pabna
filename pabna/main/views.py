from django.shortcuts import render
from .models import *


def mixin():
    content = {
        'categories': Category.objects.filter(parent_category_id=None),
        'subcategories': list(
            filter(lambda cat: cat.parent_category_id, Category.objects.all())
        )
    }
    return content


# Create your views here.
def index(request):
    content = mixin()
    return render(request, 'main/index.html', content)


def about(request):
    content = mixin()
    return render(request, 'main/about.html', content)


def blog(request):
    content = mixin()
    return render(request, 'main/blog.html', content)


def shop(request):
    content = mixin()
    return render(request, 'main/shop.html', content)


def contacts(request):
    content = mixin()
    return render(request, 'main/contacts.html', content)


def catalog(request):
    content = mixin()
    return render(request, content)