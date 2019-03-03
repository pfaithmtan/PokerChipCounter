from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Greeting, Room

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    # return render(request, "index.html")
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')

def db(request):

    rooms = Room.objects.all()
    return render(request, "db.html", {"rooms": rooms})
