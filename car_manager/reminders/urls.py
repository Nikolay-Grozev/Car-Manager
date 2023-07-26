from django.urls import path

from car_manager.reminders.views import CreateRemindersView, RemindersView

urlpatterns = (
    path('create/<int:pk>/', CreateRemindersView.as_view(), name='create reminders'),
    path('car-dashboard/<int:pk>/', RemindersView.as_view(), name='reminders dashboard')
)
