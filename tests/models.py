
from django.test import TestCase
from django.contrib.auth import get_user_model
from subscription.models import Membership, UserMembership, Subscription
from datetime import date, timedelta


class UserModelTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='test@example.com',
            password='password123',
            first_name='John',
            last_name='Doe'
        )
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('password123'))
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email='admin@example.com',
            password='adminpassword123'
        )
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertTrue(admin_user.check_password('adminpassword123'))
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_active)


class MembershipModelTest(TestCase):
    def test_membership_str_representation(self):
        membership = Membership.objects.create(
            membership_type='Pro',
            duration=30,
            duration_period='Days',
            price=99.99
        )
        self.assertEqual(str(membership), 'Pro')


# Update the test case
class UserMembershipModelTest(TestCase):
    def test_user_membership_str_representation(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='test@example.com',
            password='password123',
            first_name='John',
            last_name='Doe'
        )
        membership = Membership.objects.create(
            membership_type='Pro',
            duration=30,
            duration_period='Days',
            price=99.99
        )
        user_membership = UserMembership.objects.create(
            user=user,
            membership=membership,
            reference_code='REF123'
        )
        expected_str = f'{user.first_name} {user.last_name} (Pro)'
        self.assertEqual(str(user_membership), expected_str)


class SubscriptionModelTest(TestCase):
    def test_subscription_update_active(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='test@example.com',
            password='password123',
            first_name='John',
            last_name='Doe'
        )
        membership = Membership.objects.create(
            membership_type='Pro',
            duration=30,
            duration_period='Days',
            price=99.99
        )
        user_membership = UserMembership.objects.create(
            user=user,
            membership=membership,
            reference_code='REF123'
        )

        # Set expires_in to a date in the past to simulate an expired subscription
        past_date = date.today() - timedelta(days=1)
        subscription = Subscription.objects.create(
            user_membership=user_membership,
            expires_in=past_date,  # Set it to a past date
            active=True
        )
        subscription.update_active()  # Call the update_active method here
        self.assertFalse(subscription.active)  # Check that it's now inactive
