from django.contrib import admin
from django.urls import path
from recipes.views import RecipeViewSet, CommentViewSet



from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() 

router.register('list', views.RecipeViewSet) # router er antena
router.register('create', views.RecipeCreateView) # router er antena
router.register('update', views.RecipeUpdateView) # router er antena
router.register('delete', views.RecipeDeleteView) # router er antena


router.register('comment', views.CommentViewSet) # router er antena
router.register('commentdelete', views.CommentDeleteView) # router er antena
router.register('commentcreate', views.CommentCreateView) # router er antena
router.register('commentupdate', views.CommentUpdateView) # router er antena


urlpatterns = [
    path('', include(router.urls)),
]