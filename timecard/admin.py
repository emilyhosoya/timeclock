from django.contrib import admin
from timecard.models import Job, User

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['job_active', 'job_name']}),
        ('Date information',    {'fields': ['job_created']}),
    ]
    list_display = ('job_name', 'job_active', 'job_created')
    list_filter = ['job_active', 'job_created']
    search_fields = ['job_name']
admin.site.register(Job, JobAdmin)


class UserAdmin(admin.ModelAdmin):
    fields = ['user_active', 'first_name', 'last_name']
    list_display = ('first_name', 'last_name', 'user_active')
    list_filter = ['user_active']
    search_fields = ['first_name', 'last_name']
admin.site.register(User, UserAdmin)
