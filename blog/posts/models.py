from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    active = models.BooleanField(verbose_name="aktywny", default=False)
    pub_date = models.DateTimeField(
        verbose_name="data ppublikacji", null=True, blank=True
    )
    title = models.CharField(max_length=25, verbose_name="tytuł")
    slug = models.SlugField()
    lead = models.TextField(verbose_name="wprowadzenie")
    body = models.TextField(verbose_name="treść posta")
    author = models.ForeignKey(
        User, verbose_name="autor", null=True, blank=True, on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "wpis"
        verbose_name_plural = "wpisy"
