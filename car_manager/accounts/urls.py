from django.urls import path

from car_manager.accounts.views import UserRegisterView, UserLoginView, UserLogoutView, UserDetailsView, UserEditView, \
    UserDeleteView, ChangePasswordView


urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='create profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile_details/<int:pk>/', UserDetailsView.as_view(), name='profile details'),
    path('edit_profile/<int:pk>/', UserEditView.as_view(), name='edit profile'),
    path('delete_profile/<int:pk>/', UserDeleteView.as_view(), name='delete profile'),
    path('change_pass/', ChangePasswordView.as_view(), name='change pass'),

)
