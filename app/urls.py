from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("home/", views.home, name="blog-home"),
    path("about/", views.about, name="blog-about"),
    path("profile/", user_views.profile, name="profile"),
    path("", user_views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("logout/", LogoutView.as_view(next_page="users:logout_page"), name="logout"),

]