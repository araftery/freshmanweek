from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000, null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    location = models.CharField(max_length=200, null=True, blank=True)
    extra_info = models.CharField(max_length=500, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Auditioner(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    huid = models.IntegerField()
