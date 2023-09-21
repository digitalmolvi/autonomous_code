from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from subscription.models import Membership, UserMembership, Subscription

User = get_user_model()


class IndexViewTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )

        # Create a Membership type for testing
        self.membership = Membership.objects.create(
            membership_type='Free',
            # Add other required fields here
        )

        # Create a UserMembership and Subscription for the user
        self.user_membership = UserMembership.objects.create(
            user=self.user,
            membership=self.membership,
        )
        self.subscription = Subscription.objects.create(
            user_membership=self.user_membership,
            # Add other required fields here
        )

        # Create a test client and log in the user
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_index_view_with_subscription(self):
        # Test the index view when the user has a subscription
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertEqual(response.context['sub'], self.subscription)

    def test_index_view_without_subscription(self):
        # Delete the subscription to simulate a user without a subscription
        self.subscription.delete()
        response = self.client.get(reverse('index'))
        self.assertRedirects(response, reverse('sub'))
