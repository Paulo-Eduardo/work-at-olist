from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from call_log.serializers import CallSerializer, CallRecordSerializer
from call_log.models import CallRecord

# Create your views here.
class CallList(APIView):
    """
    Create and update CallRecords instance
    """

    def get_object(self, pk):
        try:
            return CallRecord.objects.get(pk=pk)
        except CallRecord.DoesNotExist:
            raise Http404

    def save_data_record_start(self, data):
        callRecord = {
            "id" : data["call_id"],
            "source" : data["source"],
            "destination" : data["destination"],
            "start_time" : data["timestamp"],
        }

        serializer = CallRecordSerializer(data=callRecord)
        if(serializer.is_valid()):
            serializer.save()
            return
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

    def save_data_record_end(self, data):
        call_record = self.get_object(data["call_id"])
        call_record_end = {
            "end_time" : data["timestamp"],
        }

        serializer = CallRecordSerializer(call_record, call_record_end)
        if(serializer.is_valid()):
            serializer.save()
            return
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializer = CallSerializer(data=request.data)
        if(serializer.is_valid()):
            if(request.data["typeCall"] == "S"):
                self.save_data_record_start(request.data)
            if(request.data["typeCall"] == "E"):
                self.save_data_record_end(request.data)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
