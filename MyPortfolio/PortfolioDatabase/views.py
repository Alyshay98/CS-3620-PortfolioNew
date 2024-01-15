from django.shortcuts import render, get_object_or_404
from .models import Hobby, Portfolio


# Create your views here.
def home(request):
    return render(request, 'PortfolioDatabase/home.html')


def about(request):
    return render(request, 'PortfolioDatabase/about.html')


def hobbies(request):
    hobbies_list = Hobby.objects.all()
    return render(request, 'PortfolioDatabase/hobbies.html', {"hobbies_list": hobbies_list})


def portfolio(request):
    portfolio_list = Portfolio.objects.all()
    return render(request, 'PortfolioDatabase/portfolio.html', {"portfolio_list": portfolio_list})


def contact(request):
    return render(request, 'PortfolioDatabase/contact.html')


def hobby_detail(request, hobby_id):
    hobby = get_object_or_404(Hobby, pk=hobby_id)
    return render(request, 'PortfolioDatabase/hobby_detail.html', {"hobby": hobby})


def portfolio_detail(request, portfolio_id):
    project = get_object_or_404(Portfolio, pk=portfolio_id)
    return render(request, 'PortfolioDatabase/portfolio_detail.html', {'project': project})
