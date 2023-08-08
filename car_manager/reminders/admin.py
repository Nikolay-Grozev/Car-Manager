from django import forms
from django.contrib import admin

from car_manager.common.validators import validate_date_range
from car_manager.reminders.models import ReminderModel


@admin.register(ReminderModel)
class ReminderModelAdmin(admin.ModelAdmin):
    list_display = (
        'car',
        'reminder_name',
        'start_date',
        'end_date',
    )

    readonly_fields = ('car',)  # Make the 'car' field read-only

    def save_model(self, request, obj, form, change):
        try:
            validate_date_range(obj.start_date, obj.end_date)
        except forms.ValidationError as ex:
            self.message_user(request, str(ex), level='error')
            return

        if ReminderModel.objects.filter(
                car=obj.car, reminder_name=obj.reminder_name
        ).exclude(pk=obj.pk).exists():
            self.message_user(
                request,
                "You already have this reminder for this car.",
                level='error'
            )
            return

        super().save_model(request, obj, form, change)
