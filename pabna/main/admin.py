from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ('name', )


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'price', 'category')
    ordering = ('-price', 'name',)

#если без декоратора то так:
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Goods, GoodsAdmin)



