from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CommentCreateDeleteView, PostViewSet


router = DefaultRouter()
router.register('post', PostViewSet, 'post')
router.register('comment', CommentCreateDeleteView, 'comment')
urlpatterns = [

]
urlpatterns += router.urls