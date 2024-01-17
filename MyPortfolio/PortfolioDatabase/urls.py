from django.urls import path, include
from . import views
from .views import home, hobbies, portfolio, contact, hobby_detail, portfolio_detail, about
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('hobbies/', hobbies, name='hobbies'),
    path('portfolio/', portfolio, name='portfolio'),
    path('contact/', contact, name='contact'),
    path('hobbies/<int:hobby_id>/', hobby_detail, name='hobby_detail'),
    path('portfolio/<int:portfolio_id>/', portfolio_detail, name='portfolio_detail'),
    path('add', views.create_portfolio, name="create_portfolio"),
    path('update/<int:id>', views.update_portfolio, name="update_portfolio"),
    path('delete/<int:id>', views.delete_portfolio, name="delete_portfolio"),
    path('register/', user_views.register, name='register'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
