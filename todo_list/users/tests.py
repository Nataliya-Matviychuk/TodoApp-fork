from django.test import TestCase
from .forms import RegisterForm

class FormsTestCase(TestCase):
    VALID_FORM_DATA = {
        'username': 'newuser',
        'email': 'newuser@example.com',
        'password1': 'StrongPassword123',
        'password2': 'StrongPassword123'
    }
    INVALID_FORM_DATA_EMAIL = {
        'username': 'newuser',
        'email': 'not-an-email',
        'password1': 'StrongPassword123',
        'password2': 'StrongPassword123'
    }
    INVALID_FORM_DATA_PASSWORD = {
        'username': 'newuser',
        'email': 'newuser@example.com',
        'password1': 'StrongPassword123',
        'password2': 'WrongPassword123'
    }

    def test_register_form_valid(self):
        form = RegisterForm(data=self.VALID_FORM_DATA)
        self.assertTrue(form.is_valid(), "Form should be valid with correct data.")

    def test_register_form_invalid_email(self):
        form = RegisterForm(data=self.INVALID_FORM_DATA_EMAIL)
        self.assertFalse(form.is_valid(), "Form should be invalid with incorrect email format.")
        self.assertIn('email', form.errors)

    def test_register_form_password_mismatch(self):
        form = RegisterForm(data=self.INVALID_FORM_DATA_PASSWORD)
        self.assertFalse(form.is_valid(), "Form should be invalid when passwords do not match.")
        self.assertIn('password2', form.errors)

