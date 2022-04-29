from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('<slug:slug>/', catalog, name='catalog'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('shop/', shop, name='shop'),
    path('contacts/', contacts, name='contacts'),

]