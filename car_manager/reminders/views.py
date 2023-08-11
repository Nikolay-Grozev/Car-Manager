from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views import generic

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

    def get_queryset(self):
        current_queryset = ReminderModel.objects.filter(car_id=self.kwargs.get('pk'))
        return current_queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reminders'] = ReminderModel.objects.filter(car_id=self.kwargs.get('pk'))
        context['car_id'] = self.kwargs.get("pk")
        context['current'] = self.get_queryset().count()
        return context

    def dispatch(self, request, *args, **kwargs):
        car_id = self.kwargs.get("pk")
        # Get the car associated with the reminders
        try:
            car = CarsModel.objects.get(pk=car_id)
        except CarsModel.DoesNotExist:
            return HttpResponseForbidden("403 Forbidden")
        # Check if the current user owns the car associated with the reminders
        if car.user != request.user:
            return HttpResponseForbidden("403 Forbidden")
        return super().dispatch(request, *args, **kwargs)


class DeleteReminderView(LoginRequiredMixin, generic.DeleteView):
    model = ReminderModel
    form_class = DeleteReminderForm
    template_name = 'reminders/reminders-delete.html'
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        # Check if the current user owns the car associated with the reminder
        if self.object.car.user != request.user:
            return HttpResponseForbidden("403 Forbidden")

        return super().dispatch(request, *args, **kwargs)
