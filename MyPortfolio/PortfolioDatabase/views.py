from django.shortcuts import render
from .models import Hobby, Portfolio


# Create your views here.
def home(request):
    return render(request, 'home.html')


def hobbies(request):
    hobbies_list = Hobby.objects.all()
    return render(request, 'hobbies.html', {"hobbies_list": hobbies_list})


def portfolio(request):
    portfolio_list = Portfolio.objects.all()
    return render(request, 'portfolio.html', {"portfolio_list": portfolio_list})


def contact(request):
    return render(request, 'contact.html')
