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

    def clean(self):
        cleaned_data = super().clean()

        # Check if current reminder is already exists in car reminders
        current_reminder = cleaned_data.get('reminder_name')
        if self.car.remindermodel_set.filter(reminder_name=current_reminder):
            raise forms.ValidationError("You already have this reminder for this car.")

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


class DeleteReminderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        super().save(commit=commit)
        self.instance.delete()
        return self.instance

    class Meta:
        model = ReminderModel
        fields = ()
