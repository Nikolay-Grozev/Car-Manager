from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from car_manager.cars.forms import CarRegistrationForm, EditCarForm, DeleteCarForm
from car_manager.cars.models.car_profile import CarsModel


class CreateCarView(auth_mixins.LoginRequiredMixin, views.CreateView):
    form_class = CarRegistrationForm
    template_name = 'cars/create-car.html'
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class CarView(views.ListView):
    model = CarsModel
    template_name = 'common/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = CarsModel.objects.all().filter(user=self.request.user.id)
        return context


class DetailsCarView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = CarsModel
    template_name = 'cars/details-car.html'
    context_object_name = 'cars'

    def dispatch(self, request, *args, **kwargs):
        handler = super(DetailsCarView, self).dispatch(request, *args, **kwargs)
        try:
            owner_user = self.object.user
        except AttributeError:
            return HttpResponseForbidden("403 Forbidden")
        if owner_user != request.user:
            return HttpResponseForbidden("403 Forbidden")
        return handler

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user_id == self.request.user.id
        return context


class EditCarView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = CarsModel
    form_class = EditCarForm
    template_name = 'cars/edit-car.html'
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        handler = super(EditCarView, self).dispatch(request, *args, **kwargs)
        try:
            owner_user = self.object.user
        except AttributeError:
            return HttpResponseForbidden("403 Forbidden")
        if owner_user != request.user:
            return HttpResponseForbidden("403 Forbidden")
        return handler


class DeleteCarView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = CarsModel
    form_class = DeleteCarForm
    template_name = 'cars/delete-car.html'
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        handler = super(DeleteCarView, self).dispatch(request, *args, **kwargs)
        try:
            owner_user = self.object.user
        except AttributeError:
            return HttpResponseForbidden("403 Forbidden")
        if owner_user != request.user:
            return HttpResponseForbidden("403 Forbidden")
        return handler
