from django.db import models
# Create your models here.


class Favorite(models.Model):
    title = models.CharField('title', max_length=50)
    categoria = models.CharField('categoria', max_length=50)

    def __str__(self):
        return self.title
#    class Meta:
#        verbose_name = 'Избранное'
#        verbose_name_plural = 'Избранные'


class User(models.Model):
    name = models.CharField('name', max_length=50)
    surname = models.CharField('surname', max_length=50)
    numberPhone = models.CharField('numberPhone', max_length=50)
    userEmail = models.CharField('userEmail', max_length=50)
    country = models.CharField('country', max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('name', max_length=100)
    cost = models.CharField('cost', max_length=50)
    description = models.CharField('description', max_length=1000)
    image = models.CharField('image', max_length=250)

    def __str__(self):
        return self.name








