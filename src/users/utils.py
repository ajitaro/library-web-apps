from django.core.exceptions import ValidationError


def validate_password(value):
    """Custom password validation."""
    if len(value) < 8:
        raise ValidationError('Password minimal 8 karakter.')

    if not any(char.isdigit() for char in value):
        raise ValidationError('Password harus mengandung angka.')

    if not any(char.isupper() for char in value):
        raise ValidationError(
            'Password harus mengandung huruf kapital.')

    if not value.isalnum():
        raise ValidationError(
            'Password tidak boleh mengandung special karakter.')
