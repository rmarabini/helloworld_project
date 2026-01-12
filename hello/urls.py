from django.urls import path
from .views import hello_name


urlpatterns = [
    path("<str:name>/", hello_name, name="hello_name"),
]
