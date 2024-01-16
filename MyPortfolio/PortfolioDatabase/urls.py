from django.urls import path
from .views import home, hobbies, portfolio, contact, hobby_detail, portfolio_detail, about
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('hobbies/', hobbies, name='hobbies'),
    path('portfolio/', portfolio, name='portfolio'),
    path('contact/', contact, name='contact'),
    path('hobbies/<int:hobby_id>/', hobby_detail, name='hobby_detail'),
    path('portfolio/<int:portfolio_id>/', portfolio_detail, name='portfolio_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
