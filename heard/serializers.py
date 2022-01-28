from rest_framework import serializers
from .models import HeardEvent

class HeardEventSerializer(serializers.ModelSerializer):
    '''Outgoing Event serializer'''

    class Meta:
        model = HeardEvent
        fields= '__all__'