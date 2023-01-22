from django.contrib import admin
from .models import Opportunity
# Register your models here.

admin.site.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'batch', 'job_id', 'job_link', 'location', 'end_date', 'description', 'stipend', 'added_date', 'active')


