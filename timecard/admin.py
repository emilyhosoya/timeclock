from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from adminsortable.admin import SortableAdminMixin
from timecard.models import Job, Employee

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
			return queryset.filter(isActive=True)
		elif self.value() == 'no':
			return queryset.filter(isActive=False)

# Register your models here.
class JobAdmin(SortableAdminMixin, admin.ModelAdmin):
    fields = ['isActive', 'job_name']
    list_display = ('job_name', 'isActive')
    list_filter = (IsActiveFilter,)
    search_fields = ['job_name']
admin.site.register(Job, JobAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    fields = ['isActive', 'first_name', 'last_name']
    list_display = ('first_name', 'last_name', 'isActive')
    list_filter = (IsActiveFilter,)
    search_fields = ['first_name', 'last_name']
admin.site.register(Employee, EmployeeAdmin)
