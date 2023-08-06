from django.urls import path

from car_manager.contact.views import ContactFormView, SuccessView

urlpatterns = (
    path("", ContactFormView.as_view(), name="contact"),
    path("success/", SuccessView.as_view(), name='success'),
)
