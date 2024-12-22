from django.contrib import admin
from info.models import Direction#, Doctor


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'sort_number')
    list_editable = ('sort_number',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'slug')
