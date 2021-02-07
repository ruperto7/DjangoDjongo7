from django.contrib import admin
from .models import Notes27Jan

# Register your models here.
@admin.register(Notes27Jan)
class Notes27JanAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'desc',
        'comment',
        'comment1',
        'comment2',
        'comment3',
        'comment4',
        'keywords',
        'id',
        'date',
    )
    list_filter = ('date',)