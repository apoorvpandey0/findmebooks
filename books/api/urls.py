from django.urls import path
from .views import *

urlpatterns = [
      path('list/',UserBookListAPIView.as_view(),name = 'api-userbook-list'),
      path('create/',UserBookCreateAPIView.as_view(),name = 'api-userbook-create'),
      path("detail/<int:pk>/",UserBookDetailAPIView.as_view(),name="api-userbook-detail"),
      path("update/<int:pk>/",UserBookUpdateAPIView.as_view(),name="api-userbook-update"),
      path("delete/<int:pk>/",UserBookDeleteAPIView,name="api-userbook-delete"),
]