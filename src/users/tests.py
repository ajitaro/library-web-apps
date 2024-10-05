from django.test import TestCase
from django.core.exceptions import ValidationError
from .utils import validate_password


class ValidatePasswordTests(TestCase):

    def test_password_too_short(self):
        """Test that password shorter than 8 characters raises ValidationError."""
        with self.assertRaisesMessage(ValidationError, 'Password minimal 8 karakter.'):
            validate_password('coba')

    def test_password_without_digit(self):
        """Test that password without a digit raises ValidationError."""
        with self.assertRaisesMessage(ValidationError, 'Password harus mengandung angka.'):
            validate_password('tidakAdaAngka')

    def test_password_without_uppercase(self):
        """Test that password without an uppercase letter raises ValidationError."""
        with self.assertRaisesMessage(ValidationError, 'Password harus mengandung huruf kapital.'):
            validate_password('inikecilsemuase7')

    def test_password_with_special_characters(self):
        """Test that password with special characters raises ValidationError."""
        with self.assertRaisesMessage(ValidationError, 'Password tidak boleh mengandung special karakter.'):
            validate_password('5p3c1al<4rAkTer')

    def test_valid_password(self):
        """Test that a valid password passes the validation."""
        try:
            validate_password('inibaruSe7')
        except ValidationError:
            self.fail('validate_password() raised ValidationError unexpectedly!')
