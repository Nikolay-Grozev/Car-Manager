from django.urls import path

from car_manager.web.views import HomePageView, AboutUsView

urlpatterns = (
    path('', HomePageView.as_view(), name='home page'),
    path('about-us', AboutUsView.as_view(), name='about us'),

)
