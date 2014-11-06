from django.db import models

# Create your models here.
class Job(models.Model):
    job_name = models.CharField("Name", null=True, blank=True, max_length=60)
    job_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    job_active = models.BooleanField("Active", default=True)
    def __unicode__(self):
        return self.job_name
    
    class Meta(object):
        ordering = ('job_order',)

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_active = models.BooleanField("Active", default=True)
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
