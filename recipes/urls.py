from django.contrib import admin
from django.urls import path
from recipes.views import RecipeViewSet, CommentViewSet



from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() 

router.register('list', views.RecipeViewSet,basename='recipe_list') 
router.register('create', views.RecipeCreateView,basename='recipe_create') 
router.register('update', views.RecipeUpdateView,basename='recipe_update') 
router.register('delete', views.RecipeDeleteView,basename='recipe_delete') 


router.register('comment', views.CommentViewSet,basename='comment_list') 
router.register('commentdelete', views.CommentDeleteView,basename='comment_delete') 
router.register('commentcreate', views.CommentCreateView,basename='comment_create') 
router.register('commentupdate', views.CommentUpdateView,basename='comment_update') 


urlpatterns = [
    path('', include(router.urls)),
]