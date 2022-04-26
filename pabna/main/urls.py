from django.urls import path
from .views import about, blog, shop, contacts, index


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('shop/', shop, name='shop'),
    path('contacts/', contacts, name='contacts'),

]