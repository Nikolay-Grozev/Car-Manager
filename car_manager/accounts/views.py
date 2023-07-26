from django.contrib.auth import views as auth_views, login, logout
from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy

from django.views import generic as views

from car_manager.accounts.forms import UserRegistrationForm, UserLoginForm, EditProfileForm, DeleteProfileForm, \
    ChangePasswordForm
from car_manager.accounts.models import ProfileDetails, CarManagerUser


class UserRegisterView(views.CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/create_profile.html'
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home page')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(auth_views.LogoutView):
    redirect_field_name = reverse_lazy('home page')


class UserDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = ProfileDetails
    template_name = 'accounts/details-profile.html'
    context_object_name = 'profile'
    
    # TODO check is owner

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user_id == self.request.user.id
        return context


class UserEditView(views.UpdateView):
    model = ProfileDetails
    template_name = 'accounts/edit-profile.html'
    form_class = EditProfileForm
    context_object_name = 'profile'
    success_url = reverse_lazy('home page')


class UserDeleteView(views.DeleteView):
    model = ProfileDetails
    form_class = DeleteProfileForm
    template_name = 'accounts/delete-profile.html'
    success_url = reverse_lazy('home page')

    def form_valid(self, form_class):
        user = CarManagerUser.objects.get(id=self.object.user_id)
        result = super().form_valid(form_class)
        user.delete()
        logout(self.request)
        return result


class UserChangePassword(auth_views.PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'accounts/change-password.html'
    success_url = reverse_lazy('show home')