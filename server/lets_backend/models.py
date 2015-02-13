from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50, unique=True)
    passwd = models.CharField(max_length=30)
    signup_date = models.DateField()

    def __unicode__(self):
        return self.name


class Event_Type(models.Model):
    event_type = models.CharField(max_length=15)

    def __unicode__(self):
        return self.name


class Event_Category(models.Model):
    event_category = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Events(models.Model):
    user = models.ForeignKey('Users')
    location = models.CharField(max_length=50)
    date = models.DateField()
    time_in = models.TimeField()
    time_end = models.TimeField()
    event_type = models.ForeignKey('Event_Type')
    event_category = models.ForeignKey('Event_Category')
    age = models.BooleanField()

    def __unicode__(self):
        return self.name


class Event_Description(models.Model):
    event = models.ForeignKey('Events')
    description = models.TextField()

    def __unicode__(self):
        return self.name

