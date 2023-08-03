from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from car_manager.accounts.models import ProfileDetails
from car_manager.common.bootstrap_mixin import BootstrapFormControl

UserModel = get_user_model()


class UserRegistrationForm(auth_forms.UserCreationForm, BootstrapFormControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super().apply_class_form_control(self.fields)
        for field in ['email', 'password1', 'password2']:
            self.fields[field].help_text = None

    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2',)
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter email',
                }
            ),

            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(
                attrs={
                    'label': 'Confirm password'
                }
            ),
        }

    # TODO check this method
    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = ProfileDetails(
            user=user,
        )

        if commit:
            profile.save()
        return user


class UserLoginForm(auth_forms.AuthenticationForm, BootstrapFormControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super().apply_class_form_control(self.fields)

    class Meta:
        model = UserModel
        fields = ('email', 'password',)


class EditProfileForm(forms.ModelForm, BootstrapFormControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super().apply_class_form_control(self.fields)
        for placeholder in self.fields:
            self.fields[placeholder].widget.attrs['placeholder'] = "Please enter " + ' '.join(placeholder.split('_'))

    class Meta:
        model = ProfileDetails
        exclude = ('user',)


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        super().save(commit=commit)
        self.instance.delete()
        return self.instance

    class Meta:
        model = ProfileDetails
        fields = ()

class ChangePasswordForm(auth_forms.PasswordChangeForm, BootstrapFormControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super().apply_class_form_control(self.fields)

    class Meta:
        model = UserModel
        fields = "__all__"
