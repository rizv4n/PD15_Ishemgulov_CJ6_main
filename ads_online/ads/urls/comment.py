from django.urls import path

from ads.views import CommentListView, CommentDetailView, CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('', CommentListView.as_view()),
    path('<int:pk>/', CommentDetailView.as_view()),
    path('', CommentCreateView.as_view()),
    path('<int:pk>', CommentUpdateView.as_view()),
    path('<int:pk>', CommentDeleteView.as_view()),
]
