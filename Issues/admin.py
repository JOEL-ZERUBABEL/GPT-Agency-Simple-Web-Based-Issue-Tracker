from django.contrib import admin
from .models import Issues

# Register your models here.
@admin.register(Issues)
class IssueMethod(admin.ModelAdmin):
    list_display=("title","status","priority","created_at","updated_at")
    list_filter=("status","priority")
    search_fields=("title","description")
#username:gptagency,ps:mygptproject2025