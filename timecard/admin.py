from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from adminsortable.admin import SortableAdminMixin
from timecard.models import Job, UserProfile, Period

class IsActiveFilter(admin.SimpleListFilter):
	title = _('Status')

	parameter_name = 'active'

	def lookups(self, request, model_admin):
		return (
			(None, _('Active')),
			('no', _('Not Active')),
			('all', _('All')),
		)

	def choices(self, cl):
		for lookup, title in self.lookup_choices:
			yield {
				'selected': self.value() == lookup,
				'query_string': cl.get_query_string({
					self.parameter_name: lookup,
				}, []),
				'display': title,
			}

	def queryset(self, request, queryset):
		if self.value() == None:
			return queryset.filter(is_active=True)
		elif self.value() == 'no':
			return queryset.filter(is_active=False)

# Register your models here.
class JobAdmin(SortableAdminMixin, admin.ModelAdmin):
    fields = ['is_active', 'job_name']
    list_display = ('job_name', 'is_active')
    list_filter = (IsActiveFilter,)
    search_fields = ['job_name']
admin.site.register(Job, JobAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    fields = ['is_active', 'first_name', 'last_name']
    list_display = ('first_name', 'last_name', 'is_active')
    list_filter = (IsActiveFilter,)
    search_fields = ['first_name', 'last_name']
admin.site.register(UserProfile, UserProfileAdmin)

class PeriodAdmin(admin.ModelAdmin):
	fields = ['user', 'job', 'punch_in', 'punch_out']
	list_display = ('user', 'job', 'punch_in', 'punch_out')
	search_fields = ['user', 'job']
admin.site.register(Period, PeriodAdmin)
