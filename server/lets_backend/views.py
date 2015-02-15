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

        if result == True:
            return HttpResponse("Login!")
        else:
            return HttpResponse("Error")
