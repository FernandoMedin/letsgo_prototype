from django.db import models

class Users(models.Model):
    id_user = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    passwd = models.CharField(max_length=30)
    born = models.DateField()
    sex = models.CharField(max_length=1)
    signup_date = models.DateField()

    def __unicode__(self):
        return self.name


class Event_Type(models.Model):
    id_event_type = models.AutoField(primary_key=True)
    event_type = models.CharField(max_length=15)

    def __unicode__(self):
        return self.name


class Event_Category(models.Model):
    id_event_category = models.AutoField(primary_key=True)
    event_category = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Events(models.Model):
    id_event = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users')
    event_name = models.CharField(max_length=100)
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
    id_event_description = models.AutoField(primary_key=True)
    event = models.ForeignKey('Events')
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Event_Confirmed(models.Model):
    id_event_confirmed = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users')
    event = models.ForeignKey('Events')

    def __unicode__(self):
        return self.name


class Users_Pics(models.Model):
    id_user_pic = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users')
    path = models.FilePathField()

    def __unicode__(self):
        return self.name


class User_Friends(models.Model):
    # Remeber to change this for somethin more... Light
    id_friendship = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users')
    friend = models.IntegerField()
    add = models.BooleanField()

    def __unicode__(self):
        return self.name

