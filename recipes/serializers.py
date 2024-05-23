from rest_framework import serializers
from .models import Recipe, Comment

class RecipeSerializer(serializers.ModelSerializer):
   user = serializers.StringRelatedField(many=False)
   class Meta:
        model = Recipe
        fields = '__all__'
    
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    recipe = serializers.StringRelatedField(many=False)
    class Meta:
        model = Comment
        fields = '__all__'

