from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_tracker(request):
    return render(request, "tracker.html")

def say_hello(request):
    return HttpResponse('Hello World')