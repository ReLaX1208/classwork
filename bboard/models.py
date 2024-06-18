from django.db import models


class Rubric(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Imya')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Pobeda'
        verbose_name_plural = 'Pobedi'
        ordering = ['name']


class Bb(models.Model):
    rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT, null=True, verbose_name='Rubrica')
    name = models.CharField(max_length=50, verbose_name='nazvanie')
    content = models.TextField(null=True, blank=True, verbose_name='kontent')
    price = models.FloatField(null=True, blank=True, verbose_name='cena')
    publish = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='pupliш')

    def __str__(self):
        return f'{self.name}({self.price})'

    class Meta:
        verbose_name = 'Yra'
        verbose_name_plural = 'Yrara'
        ordering = ['-publish']
