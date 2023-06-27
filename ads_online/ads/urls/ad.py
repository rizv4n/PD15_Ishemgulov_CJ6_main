from django.urls import path, include

from ads.views import AdListView, AdDetailView, AdCreateView, AdUpdateView, AdDeleteView
from ads.urls import comment

urlpatterns = [
    path('', AdListView.as_view()),
    path('<int:pk>/', AdDetailView.as_view()),
    path('', AdCreateView.as_view()),
    path('<int:pk>/', AdUpdateView.as_view()),
    path('<int:pk>/', AdDeleteView.as_view()),
    path('<int:pk>/comments/', include(comment))
]
