from django.urls import path

from car_manager.cars.views import CreateCarView, CarView, DetailsCarView, EditCarView, DeleteCarView

urlpatterns = (
    path('create/', CreateCarView.as_view(), name='create car'),
    path('dashboard/', CarView.as_view(), name='dashboard'),
    path('car_details/<int:pk>/', DetailsCarView.as_view(), name='car details'),
    path('car_edit/<int:pk>/', EditCarView.as_view(), name='car edit'),
    path('car_delete/<int:pk>/', DeleteCarView.as_view(), name='car delete'),
)
