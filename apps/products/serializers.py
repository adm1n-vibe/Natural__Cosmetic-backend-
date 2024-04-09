from rest_framework.serializers import Serializer
from apps.products.models import Product


class ProductSerializer(Serializer):
    class Meta:
        model = Product
        fields = [
        "id",
        "title",
        "description",
        "price",
        ]

