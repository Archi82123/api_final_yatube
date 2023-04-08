from rest_framework import viewsets, serializers, filters
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404
from posts.models import Post, Group, Follow
import api.serializers as ser
from api.permissions import AuthorOrReadOnly, IsAuthenticatedAndNoObject


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = ser.PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = ser.GroupSerializer
    permission_classes = (AuthorOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = ser.CommentSerializer
    permission_classes = (AuthorOrReadOnly, )

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        return post.comments.all()

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = ser.FollowSerializer
    permission_classes = (IsAuthenticatedAndNoObject,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        following = serializer.validated_data['following']
        if following == self.request.user:
            raise serializers.ValidationError(
                "Нельзя подписаться на самого себя!"
            )
        if Follow.objects.filter(
                user=self.request.user, following=following
        ).exists():
            raise serializers.ValidationError(
                "Вы уже подписаны на этого автора."
            )
        serializer.save(user=self.request.user)
