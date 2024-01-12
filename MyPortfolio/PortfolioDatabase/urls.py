from django.urls import path
from .views import home, hobbies, portfolio, contact

urlpatterns = [
    path('', home, name='home'),
    path('hobbies/', hobbies, name='hobbies'),
    path('portfolio/', portfolio, name='portfolio'),
    path('contact/', contact, name='contact'),
]