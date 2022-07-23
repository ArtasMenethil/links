from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class UsersLink(models.Model):
    link = models.CharField('Короткая ссылка', max_length=50, unique=True)
    link_url = models.URLField('Длинная ссылка', max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.link

    class Meta:
        verbose_name_plural = 'Ссылки'
        verbose_name = 'Ссылка'

    def get_absolute_url(self):
        return reverse('links', kwargs={'link': self.link})
