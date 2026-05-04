from django.db import models

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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True,verbose_name='Категория', related_name='products')
    price = models.IntegerField(verbose_name='Цена за покупку')
    created_at = models.DateField(blank=True, null=True, verbose_name='Дата создания')
    updated_at = models.DateField(blank=True, null=True, verbose_name='Дата последнего изменения')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category', 'price', 'created_at', 'updated_at']

    def __str__(self):
        return self.name
