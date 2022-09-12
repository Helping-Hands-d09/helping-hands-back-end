from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomeUserTests(TestCase):

    def test_create_user(self):
        """
        test create_user 
        """
        User = get_user_model()
        user = User.objects.create_user(email='test@test.com', password='test12345')
        user.save()

        self.assertEqual(user.email, 'test@test.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertEqual(user.username, "John Doe")
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()

    def test_create_superuser(self):
        """
        test create_superuser 
        """
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='super@user.com', password='test12345')

        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertEqual(admin_user.username, "John Doe")
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password='test12345', is_superuser=False)
    
