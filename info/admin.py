from django.contrib import admin
from info.models import Direction, Doctor


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'sort_number')
    list_editable = ('sort_number',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'slug')
    list_per_page = 10


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'birth_date', 'experience', 'sort_number')
    list_editable = ('sort_number',)
    list_filter = ('directions', 'experience', 'birth_date')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'slug', 'description')
    filter_horizontal = ('directions',)
    list_per_page = 10
