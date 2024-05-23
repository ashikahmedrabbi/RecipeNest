from django.shortcuts import render
from .models import Recipe, Comment
from .serializers import RecipeSerializer, CommentSerializer
from rest_framework import viewsets
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
