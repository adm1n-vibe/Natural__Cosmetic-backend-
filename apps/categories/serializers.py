from rest_framework.serializers import Serializer
from apps.categories.models import Category

class CategorySerializer(Serializer):
    class Meta:
        model = Category
        fields = '__all__'