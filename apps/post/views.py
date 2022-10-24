from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .permissions import IsOwner
# from rest_framework.generics import (
#     ListAPIView,
#     RetrieveAPIView,
#     DestroyAPIView,
#     UpdateAPIView,
#     CreateAPIView)

from .models import (
    Post,
    Tag,
    Comment
)
from .serializers import (
    PostListSerializer,
    PostSerializer,
    PostCreateSerializer
)

# class PostListView(ListAPIView):
    # # queryset = Post.objects.filter(status='open')
    # queryset = Post.objects.all()
    # serializer_class = PostListSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        elif self.action == 'create':
            return PostCreateSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        elif self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['destroy', 'update', 'partial_update']:
            self.permission_classes = [IsOwner]
        return super().get_permissions()

"""
Actions:

create() - POST
retrieve() - GET /post/1/
list() - GET /post/
destroy() - DELETE /post/1/
partial_update - PATCH /post/1/
update() - PUT /post/1/
"""

# TODO: создание комментариев
# TODO: отображение комментариев в постах
# TODO: создание лайков
# TODO: отображение лайков в постах
# TODO: создать модельку рейтингов
# TODO: создание рейтинга и отображение в постах