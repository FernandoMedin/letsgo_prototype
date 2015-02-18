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

    def login(self, request, email, passwd, *args, **kwargs):

        query = ""

        if email != '':
            query = Users.objects.get(email=email, passwd=passwd)
        else:
            pass

        if query != "":
            return query.id

        return False

    def new_event(
            self, request, name_event, description, location, event_date, 
            start, end, event_type, event_category, age, *args, **kwargs):

        if name_event != "":
            event = Events(
                    name_event=name_event,
                    location=location,
                    event_date=event_date,
                    start=start,
                    end=end,
                    event_type_id=event_type,
                    event_category_id=event_category,
                    age=age)

            event.save()
        else:
            pass

        if description != "":
            description = Event_Description(description=description)
            description.save()
        else:
            pass

        return True

    def get_user_data(self, request, id_user, *args, **kwargs):

        user_data = []
        space = " "
        if id_user != "":
            user = Users.objects.get(id=id_user)
        else:
            pass

        user_data.append(user.name)
        user_data.append(user.last_name)
        user_data.append(user.email)

        return user_data

