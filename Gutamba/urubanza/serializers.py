from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class TokenPairSerializer(TokenObtainPairSerializer):
      def validate(self, attrs):
         data = super(TokenPairSerializer, self).validate(attrs)
         data['groups'] = [group.name for group in self.user.groups.all()]
         data ['username'] = self.user.username
         data ['id'] = self.user.id
         data ['first_name_'] = self.user.first_name
         data ['last_name'] = self.user.last_name
         return data
      
class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = agenda
        fields = "__all__"  

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
         model = Club
         fields = "__all__"
         
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['Club'] = ClubSerializer(instance.Club, many = False).data
        data["client"] = instance.client.username
        return data
       

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__" 
        read_only_fields = "client",  



       
        
