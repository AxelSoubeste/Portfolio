from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'Portfolio_app/home.html')

def projects(request):
    return render(request, 'Portfolio_app/projects.html')

def contact_me(request):
    return render(request, 'Portfolio_app/contact.html')