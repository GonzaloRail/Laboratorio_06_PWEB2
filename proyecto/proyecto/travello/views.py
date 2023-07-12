from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = "Peru"
    dest1.desc = "Peru"
    dest1.price = 700
    dest1.img = 'destination_1.jpg'
    dest2 = Destination()
    dest2.name = "Peru"
    dest2.desc = "Peru"
    dest2.price = 700
    dest2.img = 'destination_2.jpg'
    dest3 = Destination()
    dest3.name = "Peru"
    dest3.desc = "Peru"
    dest3.price = 700
    dest3.img = 'destination_3.jpg'

    dests = [dest1,dest2,dest3]


    return render(request, "index.html",{'dests':dests})