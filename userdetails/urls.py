from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView


from rest_framework.routers import DefaultRouter

from . import views
router = DefaultRouter() 




urlpatterns = [
    
    path('', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', LogoutView.as_view()),

]
