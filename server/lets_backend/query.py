from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from lets_backend.models \
        import Users, Events, Event_Description, Event_Type, Event_Category
from django.db import models
import datetime

class Query(HttpRequest):

    def create_user(
            self, request, name, last_name, email, passwd, born, sex, *args,
            **kwargs):

        if name != '':
            query = Users(
                    name=name,
                    last_name=last_name,
                    email=email,
                    passwd=passwd,
                    born=born,
                    sex=sex,
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
            data = []
            data.append(query.id)
            data.append(query.name)
            data.append(query.last_name)
            data.append(query.email)
            data.append(query.passwd)
            return data

        return False

    def new_event(
            self, request, id_user, name_event, location, event_date, begin, 
            end, event_type, event_category, *args, **kwargs):

        if name_event != "":
            event = Events(
                    user_id=id_user,
                    event_name=name_event,
                    location=location,
                    date=event_date,
                    time_in=begin,
                    time_end=end,
                    event_type=Event_Type.objects.get(id=event_type),
                    event_category=Event_Category.objects.get(id=event_category),
                    age=False)
            event.save()
            my_event = Events.objects.get(user_id=id_user, 
                    event_name=name_event,
                    date=event_date)
        else:
            pass

        if event != "":
            data = []
            data.append(my_event.id)
            return data

        return False

    def add_description(self, request, id_event, description):

        if description != "":
            event_description = Event_Description(
                    event_id=id_event, 
                    description=description)
            event_description.save()
        else:
            pass

        return True

    def get_user_data(self, request, id_user, passwd, *args, **kwargs):

        user_data = []
        if id_user != "":
            user = Users.objects.get(id=id_user, passwd=passwd)
        else:
            pass

        user_data.append(user.name)
        user_data.append(user.last_name)
        user_data.append(user.email)

        return user_data

    def get_event_type(self, request, *args, **kwargs):

        res_dict = {}
        type_data = []
        event_type = Event_Type.objects.raw(
                'SELECT * FROM lets_backend_event_type')

        for i in event_type:
            res_dict['id'] = i.id
            res_dict['type'] = i.event_type
            type_data.append(res_dict)

        return type_data

