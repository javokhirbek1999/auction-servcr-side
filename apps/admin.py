from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models.user import User
from .models.auction import Category, Item, Bid



@admin.register(User)
class UserAdmin(UserAdmin):
    ordering = ['id']
    list_display = ['email', 'user_name', 'date_joined', 'date_updated']
    fieldsets = (
        (None, {'fields': ('email', 'user_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important Dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'password1', 'password2')
        }),
    )


admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Bid)
