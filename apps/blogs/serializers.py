from rest_framework.serializers import Serializer
from apps.blogs.models import Blog


class BlogSerializer(Serializer):
    class Meta:
        model = Blog
        fields = '__all__'