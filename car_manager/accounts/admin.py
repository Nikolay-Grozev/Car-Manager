from django.contrib import admin

from car_manager.accounts.models import CarManagerUser, ProfileDetails


@admin.register(CarManagerUser)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(ProfileDetails)
class ProfileAdmin(admin.ModelAdmin):
    pass
