from django.contrib import admin
from .models import Researchers

from import_export.admin import ImportExportMixin

# Register your models here.
class ResearchersAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('number', 'name', 'sch_output', 'year', 'citations', 'h_index')


admin.site.register(Researchers, ResearchersAdmin)

