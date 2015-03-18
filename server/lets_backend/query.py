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
            data.append(query.id_user)
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
                    event_type=Event_Type.objects.get(
                        id_event_type=event_type),
                    event_category=Event_Category.objects.get(
                        id_event_category=event_category),
                    age=False)
            event.save()
            my_event = Events.objects.get(user_id=id_user, 
                    event_name=name_event,
                    date=event_date)
        else:
            pass

        if event != "":
            data = []
            data.append(my_event.id_event)
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
            user = Users.objects.get(id_user=id_user, passwd=passwd)
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
            res_dict['id'] = i.id_event_type
            res_dict['type'] = i.event_type
            type_data.append(res_dict)

        return type_data

    def get_events(self, request, *args, **kwargs):

        e_dict = {}
        e_data = []
        ids = []
        names = []
        events = Events.objects.raw(
                'SELECT * FROM lets_backend_events')

        for i in events:
            e_data.append({'id': i.id_event, 'name': i.event_name})

        return e_data

    def get_event_data(self, request, id_event, *args, **kwargs):

        data = []
        event = Events.objects.raw(
                '''
                SELECT 
                     e.id_event,
                     e.event_name,
                     e.location,
                     to_char(e.date, 'DD/MM/YYYY') AS event_date,
                     to_char(e.time_in, 'HH24:MI') AS begin_time,
                     to_char(e.time_end, 'HH24:MI') AS end_time,
                     d.description,
                     u.name,
                     u.last_name
                FROM 
                    lets_backend_events e
                        INNER JOIN lets_backend_event_description d ON d.event_id = e.id_event 
                        INNER JOIN lets_backend_users u ON u.id_user = e.user_id
                WHERE 
                    e.id_event = %s
                ''' 
                % (id_event))

        for i in event:
            data.append({'id': i.id_event, 
                'name': i.event_name,
                'location': i.location,
                'date': i.event_date,
                'begin': i.begin_time,
                'end': i.end_time,
                'description': i.description,
                'user_name': i.name,
                'user_last_name': i.last_name})
        
        return data

