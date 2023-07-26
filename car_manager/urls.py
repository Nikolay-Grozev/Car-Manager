from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('car_manager.web.urls')),
    path('auth/', include('car_manager.accounts.urls')),
    path('cars/', include('car_manager.cars.urls')),
    path('reminders/', include('car_manager.reminders.urls')),
]
