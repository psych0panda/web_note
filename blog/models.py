from django.db import models
from tinymce import HTMLField
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'categories'

    def __str__(self):
        return self.name


class Article(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    text = HTMLField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = ['-date_created']

    def __str__(self):
        return self.title
