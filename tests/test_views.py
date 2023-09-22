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

        # Create a Membership type for testing with  actual fields
        self.membership = Membership.objects.create(
            membership_type='Premium',
            # Add other actual fields from  model here
        )

        # Create a test client and log in the user
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_index_view_with_subscription(self):
        # Create a UserMembership and Subscription for the user with actual fields
        user_membership = UserMembership.objects.create(
            user=self.user,
            membership=self.membership,
            start_date='2023-01-01',  # Actual field values
            end_date='2023-01-31',    # Actual field values
            # Add other actual fields from  UserMembership model here
            some_other_field='value',
        )

        # Create a Subscription object associated with the user_membership
        subscription = Subscription.objects.create(
            user_membership=user_membership,
            # Add other actual fields from  Subscription model here
            another_field='value',
        )

        # Test the index view when the user has a subscription
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertEqual(response.context['sub'], subscription)

    def test_index_view_without_subscription(self):
        # Test the index view when the user doesn't have a subscription
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        # Updated template name
        self.assertTemplateUsed(response, 'index.html')
        self.assertIsNone(response.context.get('sub'))
