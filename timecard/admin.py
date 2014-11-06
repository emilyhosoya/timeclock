from django.contrib import admin
from adminsortable.admin import SortableAdminMixin
from timecard.models import Job, User

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    fields = ['job_active', 'job_name']
    list_display = ('job_name', 'job_active')
    list_filter = ['job_active']
    search_fields = ['job_name']
admin.site.register(Job, JobAdmin)


class UserAdmin(admin.ModelAdmin):
    fields = ['user_active', 'first_name', 'last_name']
    list_display = ('first_name', 'last_name', 'user_active')
    list_filter = ['user_active']
    search_fields = ['first_name', 'last_name']
admin.site.register(User, UserAdmin)
