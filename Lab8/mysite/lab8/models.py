from django.db import models


class Team(models.Model):
    title = models.CharField('Название', max_length=50)
    chassis = models.CharField('Шасси', max_length=50)
    engine = models.CharField('Мотор', max_length=50)
    head = models.CharField('Руководитель', max_length=50)
    base = models.CharField('База', max_length=50)
    img = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.title
