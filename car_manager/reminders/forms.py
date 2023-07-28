from django import forms

from car_manager.common.validators import validate_date_range
from car_manager.reminders.models import ReminderModel
from car_manager.common.bootstrap_mixin import BootstrapFormControl


class RemindersRegistrationForm(forms.ModelForm, BootstrapFormControl):
    def __init__(self, car, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.car = car
        super().apply_class_form_control(self.fields)

    def save(self, commit=True):
        reminder = super().save(commit=False)
        reminder.car = self.car  # Set the car for the reminder
        if commit:
            reminder.save()
        return reminder

    # def clean_choice_field(self):
    #     choice_field_value = self.cleaned_data['reminder_name']
    #
    #     # Check if the selected option has been used before
    #     if ReminderModel.objects.filter(reminder_name=choice_field_value).exists():
    #         raise forms.ValidationError("This option has already been selected.")
    #
    #     return choice_field_value

    def clean(self):
        cleaned_data = super().clean()

        # Check if start date is less than end date
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        validate_date_range(start_date, end_date)

        return cleaned_data

    class Meta:
        model = ReminderModel
        exclude = ('car',)
        widgets = {
            'start_date': forms.DateInput(attrs={'placeholder': 'mm/dd/yyyy', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'placeholder': 'mm/dd/yyyy', 'type': 'date'})
        }
