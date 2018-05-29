from rest_framework import serializers
from call_log.models import Call, CallRecord, TYPE

class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = ('id', 'typeCall', 'timestamp', 'call_id', 'source', 'destination')


class CallRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallRecord
        fields = ('id', 'source', 'destination', 'start_time', 'end_time', 'duration', 'price')