from django.shortcuts import render, get_object_or_404
from .models import *


def mixin():
    content = {
        'categories': Category.objects.filter(parent_category_id=None),
        'subcategories': list(
            filter(lambda cat: cat.parent_category_id, Category.objects.all())
        )
    }
    return content


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


def contact(request):
    content = mixin()
    return render(request, 'main/contact.html', content)


def catalog(request, slug):
    content = mixin()
    content['category'] = get_object_or_404(Category, slug=slug)
    return render(request, 'main/shop.html', content)


def subcategory(request, category_slug, subcategory_slug):
    content = mixin()
    category = get_object_or_404(Category, slug=subcategory_slug)
    content['category'] = category
    content['goods'] = Goods.objects.filter(category_id=category.id)
    return render(request, 'main/shop.html', content)
