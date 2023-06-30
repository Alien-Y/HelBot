from django.urls import path
from . import views


# URL Config
urlpatterns = [
    path('', views.chat, name="home"),
    path('FAQ', views.FAQ_view, name='FAQ')
]
