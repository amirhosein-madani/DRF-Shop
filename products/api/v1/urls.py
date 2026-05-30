from rest_framework.routers import DefaultRouter
from .views import (
    ProductModelViewSet,
    CategoryModelViewSet,
    ColorModelViewSet,
    SizeModelViewSet,
)

router = DefaultRouter()
router.register(r"product", ProductModelViewSet, basename="product")
router.register(r"category", CategoryModelViewSet, basename="category")
router.register(r"color", ColorModelViewSet, basename="color")
router.register(r"size", SizeModelViewSet, basename="size")

urlpatterns = router.urls
