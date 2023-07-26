from django.urls import path

from car_manager.web.views import HomePageView

urlpatterns = (
    path('', HomePageView.as_view(), name='home page'),

)
