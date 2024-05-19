from rest_framework import serializers
from User.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=User
        fields="__all__"