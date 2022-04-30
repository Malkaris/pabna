from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('shop/', shop, name='shop'),
    path('contact/', contact, name='contact'),
    path('<slug:slug>/', catalog, name='catalog'),
    path('<slug:category_slug>/<slug:subcategory_slug>/', subcategory, name='subcategory'),

]
