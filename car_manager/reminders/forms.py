from django import forms
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

    class Meta:
        model = ReminderModel
        exclude = ('car',)
        widgets = {
            'start_date': forms.DateInput(attrs={'placeholder': 'mm/dd/yyyy', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'placeholder': 'mm/dd/yyyy', 'type': 'date'})
        }
