from django.urls import path

from . import views
from apps.cars.views import CarAPIView, CarCreateAPIView, CarUpdateAPIView, CarDestroyAPIView, IndexView, search

urlpatterns = [
    path('cars/', CarAPIView.as_view(), name="api_cars"),
    path("", IndexView.as_view(), name="index-page"),
    path("search", views.search, name="search-page"),
    path('cars/create', CarCreateAPIView.as_view(), name="api_cars_craete"),
    path('cars/update/<int:pk>/', CarUpdateAPIView.as_view(), name="api_cars_update"),
    path('cars/destroy/<int:pk>/', CarDestroyAPIView.as_view(), name="api_cars_update"),
]