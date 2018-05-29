from django.test import TestCase, RequestFactory
from call_log.models import Call, CallRecord
from datetime import datetime

# Create your tests here.
class CallLogTests(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = CallRecord.objects.create(id=1, start_time=datetime.now().strftime('%Y-%m-%d %H:%M'), destination="000", source="000")

    def test_can_post_call_start(self):
        data ={ 
                    "id": 1,
                    "typeCall":  "S",
                    "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M'),
                    "call_id":  1, 
                    "source":  "47 996623579", 
                    "destination":  "47 996615673", 
                }
        response = self.client.post('/calls/', data, format='json')
        self.assertEqual(response.status_code, 201)      
        self.assertTrue(Call.objects.count())

        cr = CallRecord.objects.all()[0]
        assert cr.id, 1
        assert cr.start_time, data["timestamp"]
        assert cr.source, data["source"]
        assert cr.destination, data["destination"]

    def test_post_call_end(self):
        
        
        data = {
                    "id":  2,
                    "typeCall": "E",
                    "timestamp":  datetime.now().strftime('%Y-%m-%d %H:%M'),
                    "call_id":  1,
                }
        response = self.client.post('/calls/', data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Call.objects.count())        


        cr = CallRecord.objects.all()[0]
        assert cr.id, 1
        assert cr.end_time, data["timestamp"]
    
