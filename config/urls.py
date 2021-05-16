from django.conf.urls import url
from . import views

# Create your views here.
urlpatterns = [
    url("", views.home, name="home"),
]
