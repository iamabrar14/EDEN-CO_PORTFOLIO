from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_view, name="landing"),
    path("landing/", views.landing_view, name="landing-alt"),
    path("home/", views.home_view, name="home"),
    path("about/", views.about_view, name="about"),
    path("projects/", views.projects_view, name="projects"),
    path("services/", views.services_view, name="services"),
    path("contact/", views.contact_view, name="contact"),
]
