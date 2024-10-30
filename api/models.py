from django.db import models


class Article(models.Model):
    # English Fields
    header_en = models.CharField("Header (English)", max_length=355)
    summary_en = models.CharField("Summary (English)", max_length=5000)
    description_en = models.CharField("Description (English)", max_length=5000)

    # Arabic Fields
    header_ar = models.CharField("Header (Arabic)", max_length=355)
    summary_ar = models.CharField("Summary (Arabic)", max_length=5000)
    description_ar = models.CharField("Description (Arabic)", max_length=5000)

    photo = models.ImageField("Photo", upload_to='images/')
    link = models.URLField("Link", blank=True, null=True)
    link_title_en = models.CharField("Link Title (English)", max_length=255, blank=True, null=True)
    link_title_ar = models.CharField("Link Title (Arabic)", max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.header_en} / {self.header_ar}"
