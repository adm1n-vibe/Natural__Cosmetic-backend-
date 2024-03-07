from rest_framework.routers import DefaultRouter
from apps.users.views import UsertViewSet

router = DefaultRouter()

router.register(
    prefix='users',
    viewset=UsertViewSet
)

urlpatterns = router.urls
