from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование категории')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/photo', blank=True, null=True, verbose_name='Фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True,
                                 verbose_name='Категория', related_name='products')
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateField(blank=True, null=True, verbose_name='Дата создания')
    updated_at = models.DateField(blank=True, null=True, verbose_name='Дата последнего изменения')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name='Владелец',
        related_name='products',
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category', 'price', 'created_at', 'updated_at']
        permissions = [
            ('can_unpublish_product', 'Может отменять публикацию продукта'),
        ]

    def __str__(self):
        return self.name
