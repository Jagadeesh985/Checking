from rest_framework import serializers

from django.contrib.auth.models import User

class Data(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password']
        
