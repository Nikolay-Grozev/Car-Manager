from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views import generic
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from .forms import RemindersRegistrationForm, DeleteReminderForm
from .models import ReminderModel, CarsModel


class CreateRemindersView(LoginRequiredMixin, generic.CreateView):
    form_class = RemindersRegistrationForm
    template_name = 'reminders/create-reminders.html'
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['car'] = CarsModel.objects.filter(id=self.kwargs.get('pk')).first()
        return kwargs


class RemindersView(generic.ListView):
    model = ReminderModel
    template_name = 'reminders/reminders-dashboard.html'

    # def dispatch(self, request, *args, **kwargs):
    #     handler = super(RemindersView, self).dispatch(request, *args, **kwargs)
    #     try:
    #         owner_user = self.
    #     except AttributeError:
    #         return HttpResponseForbidden("403 Forbidden")
    #     if owner_user != request.user:
    #         return HttpResponseForbidden("403 Forbidden")
    #     return handler

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reminders'] = ReminderModel.objects.filter(car_id=self.kwargs.get('pk'))
        context['car_id'] = self.kwargs.get("pk")
        return context


class DeleteReminderView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = ReminderModel
    form_class = DeleteReminderForm
    template_name = 'reminders/reminders-delete.html'
    success_url = reverse_lazy('dashboard')
