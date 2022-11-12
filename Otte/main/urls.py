from django.urls import include, path
from rest_framework import routers
from main.views import CommentViewSet, HomeViewSet,CategoryViewSet,RatingtViewSet

router = routers.DefaultRouter()
router.register(r'comment', CommentViewSet)
router.register(r'home', HomeViewSet)
router.register(r'cate', CategoryViewSet)
router.register(r'rating', RatingtViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ]