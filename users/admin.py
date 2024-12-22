from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        ('Main fields', {'fields': ('email', 'password', 'slug')}),  # Основні поля
        ('Personal info', {
            'fields': (
                'first_name',
                'last_name',
                'description',
                'birth_date',
                'experience',
                'directions',
                'sort_number',
            )
        }),  # Особиста інформація
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),  # Права доступу
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'slug',
                'password1',
                'password2',
                'first_name',
                'last_name',
                'description',
                'birth_date',
                'experience',
                'directions',
                'sort_number',
            )
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'slug', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name', 'slug')
    filter_horizontal = ('directions',)
    ordering = ('sort_number', 'slug')

admin.site.register(User, UserAdmin)
