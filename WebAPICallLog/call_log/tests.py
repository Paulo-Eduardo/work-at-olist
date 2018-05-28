from django.test import TestCase
from call_log.models import Call

# Create your tests here.
class CallLogTests(TestCase):

    def test_can_post_call_start(self):
        data = { 
                    "id":  1, 
                    "type":  "S", 
                    "timestamp":  "", 
                    "call_id":  1, 
                    "source":  "47 996623579", 
                    "destination":  "47 996615673", 
                }
        response = self.client.post('/calls/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Call.objects.count(), 1)

    def test_post_call_end(self):
        data = {
                    "id":  2,
                    "type": "E",
                    "timestamp":  "",
                    "call_id":  1,
                }
        response = self.client.put('/calls/', data)
        self.assertEqual(response.status_code, 200)

    