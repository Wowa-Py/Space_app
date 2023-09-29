from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from.models import User

class UserTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_user(self):
        response = self.client.post(reverse('create_user'), {
            'name': 'Test',
            'email': 'test@example.com',
            'birthdate': timezone.now()
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, 'Test')
        self.assertEqual(User.objects.get().email, 'test@example.com')
        self.assertEqual(User.objects.get().birthdate, timezone.now())
