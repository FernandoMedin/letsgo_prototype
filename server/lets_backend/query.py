from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from lets_backend.models import Users, Events, Event_Description
from django.db import models
import datetime

class Query(HttpRequest):

    def create_user(
            self, request, name, last_name, email, passwd, *args, **kwargs):

        if name != '':
            query = Users(
                    name=name,
                    last_name=last_name,
                    email=email,
                    passwd=passwd,
                    signup_date=datetime.datetime.now())

            query.save()
        else:
            pass

        return True


    def name(self, test, request, *args, **kwargs):
        name = test

        return name

