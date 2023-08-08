from django.contrib import admin

from car_manager.accounts.models import CarManagerUser, ProfileDetails


@admin.register(CarManagerUser)
class UserAdmin(admin.ModelAdmin):
    class UsersAdmin(admin.ModelAdmin):
        list_display = (
            'email',
            'date_joined',
        )


@admin.register(ProfileDetails)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'phone_number',
        'image_url',
    )

    readonly_fields = ('user',)
