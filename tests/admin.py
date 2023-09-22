from django.test import TestCase, Client
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch
from subscription.models import Membership, UserMembership, Subscription, User


class AdminTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword',
            first_name='John',        # Add first_name
            last_name='Doe'           # Add last_name
        )

        # Create a Membership type for testing
        self.membership = Membership.objects.create(
            membership_type='Free',
            description='A free membership',  # Add description
            price=0.0                         # Add price
        )

        # Create a test client
        self.client = Client()

    def test_user_model_registered(self):
        # Test if the User model is registered in the admin site
        try:
            reverse('admin:auth_user_change', args=(self.user.pk,))
        except NoReverseMatch:
            self.fail("admin:auth_user_change URL does not exist")

    def test_usermembership_model_registered(self):
        # Test if the UserMembership model is registered in the admin site
        try:
            reverse('admin:subscription_usermembership_change_list')
        except NoReverseMatch:
            self.fail(
                "admin:subscription_usermembership_change_list URL does not exist")

    def test_membership_model_registered(self):
        # Test if the Membership model is registered in the admin site
        try:
            reverse('admin:subscription_membership_change_list')
        except NoReverseMatch:
            self.fail(
                "admin:subscription_membership_change_list URL does not exist")

    def test_subscription_model_registered(self):
        # Test if the Subscription model is registered in the admin site
        try:
            reverse('admin:subscription_subscription_change_list')
        except NoReverseMatch:
            self.fail(
                "admin:subscription_subscription_change_list URL does not exist")
