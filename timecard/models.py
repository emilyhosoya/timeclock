from django.db import models
import datetime

# Create your models here.
class Job(models.Model):
    job_name = models.CharField("Name", max_length=60)
    job_active = models.BooleanField("Active", default=True)
    job_created = models.DateField("Created", default=datetime.date.today)
    def __unicode__(self):
        return self.job_name

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_active = models.BooleanField("Active", default=True)
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
