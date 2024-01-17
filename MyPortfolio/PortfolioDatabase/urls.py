from django.urls import path, include
from .views import home, hobbies, portfolio, contact, hobby_detail, portfolio_detail, about
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('hobbies/', hobbies, name='hobbies'),
    path('portfolio/', portfolio, name='portfolio'),
    path('contact/', contact, name='contact'),
    path('hobbies/<int:hobby_id>/', hobby_detail, name='hobby_detail'),
    path('portfolio/<int:portfolio_id>/', portfolio_detail, name='portfolio_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='PortfolioDatabase/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
