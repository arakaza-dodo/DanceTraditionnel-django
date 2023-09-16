
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import *

class TokenPairView(TokenObtainPairView):
      serializer_class = TokenPairSerializer

class AgendaViewset(viewsets.ModelViewSet):
    queryset =agenda.objects.all()
    serializer_class = AgendaSerializer

class ClubViewset(viewsets.ModelViewSet):
    queryset =Club.objects.all()
    serializer_class = ClubSerializer

class VideoViewset(viewsets.ModelViewSet):
    queryset= Video.objects.all()
    serializer_class = VideoSerializer

    def perform_create(self, serializer):
      serializer.save(User=self.request.user)
      return serializer

