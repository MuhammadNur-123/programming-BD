
from django.contrib import admin
from .models import Instractor

@admin.register(Instractor)
class InstractorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'education', 'instractor_id','excluci', 
            'education', 'phone_number', 'date_of_birth', 
            'bio', 'country', 'possiton', 'linkdlen_id', 'image')
    search_fields = ('name', 'email')
    list_filter = ('country', 'education')
