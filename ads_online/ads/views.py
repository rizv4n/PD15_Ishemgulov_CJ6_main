from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView

from ads.serializers.ad import *
from ads.serializers.comment import *
from rest_framework.permissions import IsAuthenticated

from ads.permissions import ChangePermission


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer
    permission_classes = [IsAuthenticated]


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    permission_classes = [IsAuthenticated]


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer
    permission_classes = [IsAuthenticated, ChangePermission]


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDeleteSerializer
    permission_classes = [IsAuthenticated, ChangePermission]


class CommentListView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    permission_classes = [IsAuthenticated]


class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]


class CommentDetailView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes = [IsAuthenticated]


class CommentUpdateView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateSerializer
    permission_classes = [IsAuthenticated, ChangePermission]


class CommentDeleteView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteSerializer
    permission_classes = [IsAuthenticated, ChangePermission]
