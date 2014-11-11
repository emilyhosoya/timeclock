from django.db import models

# Create your models here.
class Job(models.Model):
    job_name = models.CharField("Name", null=True, blank=True, max_length=60)
    job_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    isActive = models.BooleanField("Active", default=True)
    def __unicode__(self):
        return self.job_name
    
    class Meta(object):
        ordering = ('job_order',)

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    isActive = models.BooleanField("Active", default=True)
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

# class Punch(models.Model):
#     employee = models.ForeignKey(User)
#     job = models.ForeignKey(Job)
#     time = models.DateTimeField('punch time', auto_now=False, auto_now_add=False)
#     punch_type = models.CharField(max_length=3, choices=PUNCH_TYPE_CHOICES)
#     log = models.TextField(max_length=600)