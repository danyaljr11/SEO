from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Article
from api.serializers import ArticleSerializer


def format_response(success, message, data=None, status_code=status.HTTP_200_OK):
    return Response({
        "success": success,
        "message": message,
        "data": data if data else {}
    }, status=status_code)


class ArticleListView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)

        # Check if there are articles
        if not serializer.data:
            return format_response(
                success=True,
                message="No articles found.",
                data=[],
                status_code=status.HTTP_200_OK
            )

        return format_response(
            success=True,
            message="List of articles retrieved successfully.",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )
