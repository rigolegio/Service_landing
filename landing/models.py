from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=120)

    def __str__(self):
        return "Пользователь %s" % (self.name)

    class Meta:
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"


