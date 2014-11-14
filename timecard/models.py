from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    job_name = models.CharField("Name", null=True, blank=True, max_length=60)
    job_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    is_active = models.BooleanField("Active", default=True)
    def __unicode__(self):
        return self.job_name
    
    class Meta(object):
        ordering = ('job_order',)

class UserProfile(models.Model):
#     user = models.OneToOneField(User)
#     is_cool = models.BooleanField()
#     nickname = models.CharField(max_length=50)

# User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField("Active", default=True)
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Period(models.Model):
    user = models.ForeignKey(UserProfile)
    job = models.ForeignKey(Job)
    punch_in = models.DateTimeField()
    punch_out = models.DateTimeField()
    def __unicode__(self):
        return u'%s %s %s %s' % (self.user, self.job, self.punch_in, self.punch_out)
