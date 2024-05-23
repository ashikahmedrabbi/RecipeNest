from django.contrib import admin
from django.urls import path
from recipes.views import RecipeViewSet, CommentViewSet



from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() 

router.register('list', views.RecipeViewSet) # router er antena

router.register('comment', views.CommentViewSet) # router er antena

urlpatterns = [
    path('', include(router.urls)),
]