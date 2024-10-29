from django.urls import path
from api.views import ArticleListView

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article-list'),
]