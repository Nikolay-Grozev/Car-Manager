from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('car_manager.web.urls')),
    path('auth/', include('car_manager.accounts.urls')),
    path('cars/', include('car_manager.cars.urls')),
    path('reminders/', include('car_manager.reminders.urls')),
    path('contact/', include('car_manager.contact.urls')),
]

handler400 = TemplateView.as_view(template_name='error-pages/error-400.html')
handler404 = TemplateView.as_view(template_name='error-pages/error-404.html')
