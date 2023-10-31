from django.test import TestCase
from django.contrib.auth.models import User
from .models import TimeOffRequest

# Create your tests here.

class TimeOffRequestTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.request_data = {
            'request_type': 'paid',
            'start_date': '2023-08-20',
            'end_date': '2023-08-25',
            'reason': 'Sick',
        }

    def test_create_time_off_request(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post('/create_time_off_request/', self.request_data)
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(TimeOffRequest.objects.count(), 1)

    def test_view_time_off_requests(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/time_off_requests/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pending Requests')

    def test_approve_time_off_request(self):
        request = TimeOffRequest.objects.create(user=self.user, **self.request_data)
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(f'/approve_time_off_request/{request.id}/')
        self.assertEqual(response.status_code, 302)  # Should redirect after approval
        updated_request = TimeOffRequest.objects.get(id=request.id)
        self.assertEqual(updated_request.status, 'approved')

    def test_reject_time_off_request(self):
        request = TimeOffRequest.objects.create(user=self.user, **self.request_data)
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(f'/reject_time_off_request/{request.id}/')
        self.assertEqual(response.status_code, 302)  # Should redirect after rejection
        updated_request = TimeOffRequest.objects.get(id=request.id)
        self.assertEqual(updated_request.status, 'rejected')
