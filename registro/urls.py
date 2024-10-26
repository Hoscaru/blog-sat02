from django.urls import path, include
# from .views import SignUpView
from registro import views

urlpatterns=[
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/",views.SignUpView.as_view(), name="signup"),
    path("", views.FirstPage, name="home"),
]