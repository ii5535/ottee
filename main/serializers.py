from rest_framework import serializers
from main.models import Comment, Home,Category,Rating

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        
        fields = ('id', 'home', 'user', 'created_at','comment','clean','hit','noise','optionrate','secu','day_light')

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ('id', 'name', 'deposit','images', 'Monthly_rent', 'administration_cost','room','floor','hitter','parking','Veranda','address','number','distance','option')
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')
        
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id','homes','ave')