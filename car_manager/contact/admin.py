from django.contrib import admin

from car_manager.contact.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'mode_of_contact',
        'question_categories',

    )
