from rest_framework import serializers
from call_log.models import CallRecord, TYPE


class CallRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallRecord
        fields = ('id', 'source', 'destination', 'start_time', 'end_time', 'duration', 'price')