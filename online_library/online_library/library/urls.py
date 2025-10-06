from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("book/<int:pk>/", views.book_detail, name="book_detail"),
    path("book/<int:pk>/review/", views.add_review, name="add_review"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]