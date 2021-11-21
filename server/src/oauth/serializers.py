from rest_framework import serializers
from .models import AuthUser

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthUser
        fields = ('display_name', 'bio', 'email', 'city','country','join_date','avatar')