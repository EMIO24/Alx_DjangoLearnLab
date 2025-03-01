from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(UserProfile)

# Register your models here.
