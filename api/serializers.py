from rest_framework import serializers
from django.conf import settings
from api.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'

    def get_photo(self, obj):
        # Construct the full URL for the photo field
        return f"{settings.BASE_URL}{obj.photo.url}" if obj.photo else None
