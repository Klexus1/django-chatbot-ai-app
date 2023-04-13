from django.urls import path
from .views import chat


urlpatterns = [
    path("", chat, name="chat"),
    path("error_handler/", chat, name="error_handler"),
]