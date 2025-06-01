from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as djangoUserAdmin
from .models import User
from .forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
# Register your models here.

class UserAdmin(djangoUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_superuser','date_joined','last_login')
    list_filter = ('email', 'is_staff', 'date_joined')
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active','is_superuser')}
        ),
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, UserAdmin)