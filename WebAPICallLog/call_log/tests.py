from django.test import TestCase

# Create your tests here.
class CallLogTests(TestCase):

    def test_post_call_start(self):
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

    def test_post_call_end(self):
        data = {
                    "id":  2,
                    "type": "E",
                    "timestamp":  "",
                    "call_id":  1,
                }
        response = self.client.post('/call/', data)
        self.assertEqual(response.status_code, 201)        