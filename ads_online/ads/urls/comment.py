from django.urls import path

from ads.views import CommentListView, CommentDetailView, CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('', CommentListView.as_view()),
    path('<int:pk>/', CommentDetailView.as_view()),
    path('create/', CommentCreateView.as_view()),
    path('<int:pk>/update/', CommentUpdateView.as_view()),
    path('<int:pk>/delete/', CommentDeleteView.as_view()),
]
