from django.db import models
from django.utils import timezone


class OwnUser(models.Model):
    SEX_ITEMS = (
        ('male', '男'),
        ('female', '女')
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=6, choices=SEX_ITEMS)
    address = models.TextField()
    create_time = models.DateTimeField(auto_now_add=timezone.now)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
