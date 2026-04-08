from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('projects/', views.projects, name="projects"),
    path('Contact/', views.contact_me, name="contact"),
]