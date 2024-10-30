from rest_framework import serializers
from django.conf import settings
from api.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'header_en', 'header_ar',
            'summary_en', 'summary_ar',
            'description_en', 'description_ar',
            'photo', 'link',
            'link_title_en', 'link_title_ar'
        ]

    def get_photo(self, obj):
        # Construct the full URL for the photo field
        return f"{settings.BASE_URL}{obj.photo.url}" if obj.photo else None