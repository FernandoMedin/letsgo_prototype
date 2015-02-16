from django.http import HttpResponse, HttpResponseNotFound
from lets_backend.query import Query
from django.views.generic import View
import datetime

class LetsView(View):

    def new_user(self, request, *args, **kwargs):
        inst_query = Query()
        name = request.POST.get("name", "")
        last_name = request.POST.get("last_name", "")
        email = request.POST.get("email", "")
        passwd = request.POST.get("passwd", "")

        if name == "":
            return HttpResponse("Error")
        elif last_name == "":
            return HttpResponse("Error")
        elif email == "":
            return HttpResponse("Error")
        elif passwd == "":
            return HttpResponse("Error")
        else:
            inst_query.create_user(self, name, last_name, email, passwd)

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
            return HttpResponse(result)
        else:
            return HttpResponse("Error")

    def new_event(self, request, *args, **kwargs):
        inst_query = Query()
        event_name = request.POST.get("event_name", "")
        description = request.POST.get("description", "")
        location = request.POST.get("location", "")
        event_date = request.POST.get("event_date", "")
        start = request.POST.get("start", "")
        end = request.POST.get("end", "")
        event_type = request.POST.get("event_type", "")
        event_category = request.POST.get("event_category", "")
        age = request.POST.get("age", "")

        event_date = event_date.replace('/', '')
        event_date = datetime.datetime.strptime(event_date, '%d%m%Y').date()
        start = datetime.datetime.strptime(start, '%H:%M').time()
        end = datetime.datetime.strptime(end, '%H:%M').time()

        if event_name == "":
            return HttpResponse("Error")
        elif location == "":
            return HttpResponse("Error")
        elif event_date == "":
            return HttpResponse("Error")
        elif start == "":
            return HttpResponse("Error")
        elif event_type == "":
            return HttpResponse("Error")
        elif event_category == "":
            return HttpResponse("Error")
        elif age == "":
            return HttpResponse("Error")
        else:
            inst_query.new_event(self,
                    event_name, description, location, event_date, start, end, 
                    event_type, event_category, age)

        return HttpResponse("Event created!")

    def debug(self, request, *args, **kwargs):
        inst_query = Query()
        event_name = request.POST.get("event_name", "")
        description = request.POST.get("description", "")
        location = request.POST.get("location", "")
        event_date = request.POST.get("event_date", "")
        start = request.POST.get("start", "")
        end = request.POST.get("end", "")
        event_type = request.POST.get("event_type", "")
        event_category = request.POST.get("event_category", "")
        age = request.POST.get("age", "")

        event_date = event_date.replace('/', '')
        event_date = datetime.datetime.strptime(event_date, '%d%m%Y').date()
        start = datetime.datetime.strptime(start, '%H:%M').time()
        end = datetime.datetime.strptime(end, '%H:%M').time()

        return HttpResponse(event_date)

