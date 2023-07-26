from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .forms import RemindersRegistrationForm
from .models import ReminderModel, CarsModel


class CreateRemindersView(LoginRequiredMixin, generic.CreateView):
    form_class = RemindersRegistrationForm
    template_name = 'reminders/create-reminders.html'
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['car'] = self.request.user.id
        return kwargs

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     # Get the car_id from the URL parameters
    #     # car_id = self.kwargs.get('car_id')
    #     # Get the car instance using the car_id
    #     # car = get_object_or_404(CarsModel, id=car_id, user=self.request.user)
    #     # Pass the car instance to the form
    #     kwargs['car'] = self.request.
    #     return kwargs

    # def form_valid(self, form):
    #     return super().form_valid(form)


class RemindersView(generic.ListView):
    model = ReminderModel
    template_name = 'reminders/reminders-dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # car = CarsModel.objects.filter(user=self.request.user)
        context['reminders'] = ReminderModel.objects.filter(car_id=self.request.user.id)
        context['car'] = self.request.user.id
        return context
