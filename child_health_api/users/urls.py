from django.urls import path
from . import views

urlpatterns = [
    # Example endpoint
    path("hello/", views.hello, name="hello"),
]
