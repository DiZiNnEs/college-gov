from django.db import models


class College(models.Model):
    COLLEGE_TYPE = [
        ('NAT', 'National'),
        ('PRV', 'Private'),
    ]

    title = models.CharField(max_length=256, verbose_name='название')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    street = models.CharField(max_length=128)
    email = models.EmailField()
    type = models.CharField(max_length=3, choices=COLLEGE_TYPE, default='NAT')
    country = models.ForeignKey('Country', on_delete=models.PROTECT)
    city = models.ForeignKey('City', on_delete=models.PROTECT)
    budget = models.DecimalField(max_digits=19, decimal_places=10)


class Country(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название страны')
    code = models.SmallIntegerField(default='+', verbose_name='Код страны')

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название города')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='категория колледжа')

    def __str__(self):
        return self.name
