from django.db import models
from django.urls import reverse

class Collect(models.Model):

    def get_absolute_url(self):
        return reverse('picture:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name + '-' + self.nick_name

    name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100)
    about = models.CharField(max_length=1000)
    image = models.CharField(max_length=1000)
    caption = models.CharField(max_length=1000)
    description = models.CharField(max_length=3000)
