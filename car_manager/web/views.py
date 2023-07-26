from django.contrib.auth import views
from django.shortcuts import render

from car_manager.web.models import Dashboard


class HomePageView(views.TemplateView):
    template_name = 'common/home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_user_signed_in'] = self.request.user.is_authenticated
        context['user'] = self.request.user
        return context
