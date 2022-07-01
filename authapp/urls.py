from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginView, CreateUser
from knox.views import LogoutView, LogoutAllView


router = DefaultRouter()
router.register(r'signup', CreateUser, basename='signup')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('logallout/', LogoutAllView.as_view()),
]