from django.http import HttpResponse, HttpResponseNotFound, Http404
from lets_backend.query import Query
from django.views.generic import View
import datetime
import json

class LetsView(View):

    def new_user(self, request, *args, **kwargs):
        inst_query = Query()
        name = request.POST.get("name", "")
        last_name = request.POST.get("last_name", "")
        email = request.POST.get("email", "")
        passwd = request.POST.get("passwd", "")
        born = request.POST.get("born", "")
        sex = request.POST.get("sex", "")

        if int(sex) == 1:
            sex = "M"
        else:
            sex = "F"

        born = born.replace('/', '')
        born = datetime.datetime.strptime(born, '%d%m%Y').date()
        name = name.capitalize()
        last_name = last_name.capitalize()

        if name == "":
            return HttpResponse("Error")
        elif last_name == "":
            return HttpResponse("Error")
        elif email == "":
            return HttpResponse("Error")
        elif passwd == "":
            return HttpResponse("Error")
        elif born == "":
            return HttpResponse("Error")
        elif sex == "":
            return HttpResponse("Error")
        else:
            inst_query.create_user(
                    self, name, last_name, email, passwd, born, sex)

        return HttpResponse("Account created!")

    def login(self, request, *args, **kwargs):
        inst_query = Query()
        result = False
        email = request.POST.get("email", "")
        passwd = request.POST.get("passwd", "")

        if email == "":
            return HttpResponse("Error")
        elif passwd == "":
            return HttpResponse("Error")
        else:
            result = inst_query.login(self, email, passwd)

        if result != False:
            user_data = {}
            user_data['id_user'] = str(result[0])
            user_data['name'] = result[1]
            user_data['last_name'] = result[2]
            user_data['email'] = result[3]
            user_data['passwd'] = result[4]
            return HttpResponse(json.dumps(user_data))
        else:
            return HttpResponse("Error")

    def new_event(self, request, *args, **kwargs):
        inst_query = Query()
        id_user = request.POST.get("id_user", "")
        event_name = request.POST.get("event_name", "")
        location = request.POST.get("location", "")
        event_date = request.POST.get("event_date", "")
        start = request.POST.get("begin", "")
        end = request.POST.get("end", "")
        event_type = request.POST.get("event_type", "")
        event_category = request.POST.get("event_category", "")
        description = request.POST.get("description", "")

        form_date = event_date.replace('/', '')
        form_date = datetime.datetime.strptime(form_date, '%d%m%Y').date()
        start = datetime.datetime.strptime(start, '%H:%M:%S').time()
        end = datetime.datetime.strptime(end, '%H:%M:%S').time()

        result = inst_query.new_event(self, id_user, event_name, location,
                form_date, start, end, event_type, event_category)

        if result:
            inst_query.add_description(self, int(result[0]), description)

        return HttpResponse(result)

    def get_user_data(self, request, *args, **kwargs):
        inst_query = Query()
        id_user = int(request.POST.get("id_user", ""))
        passwd = request.POST.get("passwd", "")

        if id_user == "":
            return HttpResponse("Error")
        elif passwd == "":
            return HttpResponse("Error")
        else:
            user = inst_query.get_user_data(self, id_user, passwd)

        user_data = {}
        user_data['name'] = user[0]
        user_data['last_name'] = user[1]
        user_data['email'] = user[2]

        return HttpResponse(json.dumps(user_data))

    def get_event_type(self, request, *args, **kwargs):
        inst_query = Query()

        result = inst_query.get_event_type(self)
        data_dict = {}
        data = []
        for i in result:
            data_dict['id'] = i['id']
            data_dict['type'] = i['type']
            data.append(data_dict)

        return HttpResponse(json.dumps(data))

    def show_events(self, request, *args, **kwargs):
        inst_query = Query()

        event_data = inst_query.get_events(self)
        e_data = []
        for i in event_data:
            e_data.append({'id': i['id'], 'name': i['name']})

        return HttpResponse(json.dumps(e_data))

    def test(self, request, *args, **kwargs):
        inst_query = Query()

        id_event = request.GET.get("id_event", "")
        event_data = inst_query.get_event_data(self, id_event)
        e_data = []
        for i in event_data:
            e_data.append({'id': i['id'], 
                'name': i['name'],
                'location': i['location'],
                'date': i['date'],
                'begin': i['begin'],
                'end': i['end'],
                'description': i['description'],
                'user_name': i['user_name'],
                'user_last_name': i['user_last_name']})

        return HttpResponse(json.dumps(e_data))

