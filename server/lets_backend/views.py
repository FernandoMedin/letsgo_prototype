from django.http import HttpResponse, HttpResponseRedirect
from lets_backend.query import Query
from django.views.generic import View
import datetime

class LetsView(View):

    def name(self, request, *args, **kwargs):
        inst_query = Query()
        test = request.GET.get("name", "")
        another = request.GET.get("an", "")
        name = inst_query.name(self, test, another)

        return HttpResponse(test)

    def new_user(self, request, *args, **kwargs):
        inst_query = Query()
        name = request.GET.get("name", "")
        last_name = request.GET.get("last_name", "")
        email = request.GET.get("email", "")
        passwd = request.GET.get("passwd", "")

        inst_query.create_user(self, name, last_name, email, passwd)

        return HttpResponseRedirect("Created!")

