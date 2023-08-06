from django.contrib import admin

from car_manager.contact.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
