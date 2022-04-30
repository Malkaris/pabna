from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField('Название', max_length=20)
    slug = models.SlugField('URL', unique=True)
    parent_category_id = models.ForeignKey('Category', on_delete=models.CASCADE,
                                           verbose_name='Родительская категория',
                                           blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('catalog', kwargs={'slug': self.slug})


class Goods(models.Model):
    name = models.CharField('Название', max_length=30)
    description = models.CharField('Описание', max_length=140)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )
    image = models.ImageField(
        upload_to='goods/',
        verbose_name='Картинка'
    )
    price = models.PositiveIntegerField('Цена')
    slug = models.SlugField('URL', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'