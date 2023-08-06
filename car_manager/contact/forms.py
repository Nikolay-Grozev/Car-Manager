from django import forms
from .models import Contact

select_mode_of_contact = (
    ("email", "E-Mail"),
    ("phone", "Phone"),
)

select_question_categories = (
    ("user_account", "User account"),
    ("vehicle", "Vehicle"),
    ("reminder", "Reminder"),
    ("other", "Others"),
)


class ContactForm(forms.ModelForm):
    phone = forms.CharField(required=False)

    mode_of_contact = forms.CharField(
        required=False,
        widget=forms.RadioSelect(choices=select_mode_of_contact),
    )

    question_categories = forms.CharField(
        required=False,
        widget=forms.Select(choices=select_question_categories),
    )

    class Meta:
        model = Contact
        fields = '__all__'
