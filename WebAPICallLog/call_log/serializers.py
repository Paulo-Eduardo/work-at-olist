from rest_framework import serializers
from call_log.models import Call, TYPE

class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = ('id', 'typeCall', 'timestamp', 'call_id', 'source', 'destination')