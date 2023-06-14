from rest_framework import serializers
from dashboard.models import Header

class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = '__all__'