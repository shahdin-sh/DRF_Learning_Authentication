from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        UserAdmin.fieldsets +  (
        ("Addintional informations", {'fields': ('birth_date',),}),
    )
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    

    list_display = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'birth_date', 'get_group_names']
    list_per_page = 10
    ordering = ['username']

    @admin.action(description='groups')
    def get_group_names(self, obj):
        return list([group.name for group in obj.groups.all()])


