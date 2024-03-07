from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from apps.blogs.models  import Blog
from apps.blogs.serializers import BlogSerializer

class blogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticated, IsAuthenticated)
