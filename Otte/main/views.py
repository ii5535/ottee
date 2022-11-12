from django.shortcuts import render
from rest_framework import viewsets
from main.serializers import CommentSerializer, HomeSerializer , CategorySerializer,RatingSerializer
from main.models import Comment, Home , Category ,Rating
from rest_framework import generics
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['home']


class HomeViewSet(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['id']
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RatingtViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    # filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ['homes']
