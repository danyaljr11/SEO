from django.db import models


# Create your models here.


class Article(models.Model):
    header = models.CharField(max_length=355)
    summary = models.CharField(max_length=5000)
    description = models.CharField(max_length=5000)
    photo = models.ImageField(upload_to='images/')
    link = models.URLField(blank=True, null=True)
    link_title = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.header
