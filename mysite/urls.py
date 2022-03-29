from django.urls import path
from . views import home
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', csrf_exempt(home), name='home '),
]