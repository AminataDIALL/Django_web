from django.contrib import admin
from .models import User
from .forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin

class UserAdmin(UserAdmin):
    model = User
    add_form = UserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User role',
            {
                'fields':
                (
                    'is_director',
                    'is_producer',
                )
            }

        )
    )

admin.site.register(User, UserAdmin )
