from django.test import TestCase

# Create your tests here.
class CallLogTests(TestCase):

    def test_post_call_start(self):
        data = {
                    "id":  1,
                    "type":  "start",
                    "timestamp":  "",
                    "call_id":  1,
                    "source":  "47 996623579",
                    "destination":  "47 996615673",
                }
        response = self.client.get('/calls/', data=data)
        self.assertEqual(response.status_code, 201)