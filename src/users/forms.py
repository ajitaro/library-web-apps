from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from .utils import validate_password


class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    error_messages = {
        'email_exists': 'Email sudah terdaftar.',
        'password_mismatch': 'Password tidak cocok.',
    }
    password1 = forms.CharField(
        initial='',
        label='Password',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Masukkan password'}),
        validators=[validate_password],
        error_messages={
            'required': 'Masukkan password.',
        }
    )
    password2 = forms.CharField(
        initial='',
        label='Password confirmation',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Konfirmasi password'}),
        help_text='Masukkan password di atas kembali untuk verifikasi.',
        error_messages={
            'required': 'Konfirmasi password-mu.',
        }
    )

    class Meta:
        model = User
        fields = ('name', 'email',)
        labels = {
            'name': 'Nama Lengkap',
            'email': 'Email',
        }
        widgets = {
            'name': forms.TextInput(attrs={'value': '', 'class': 'form-control', 'placeholder': 'Masukkan nama lengkap'}),
            'email': forms.EmailInput(attrs={'value': '', 'class': 'form-control', 'placeholder': 'Masukkan email'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                self.error_messages['email_exists'],
                code='email_exists',
            )
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        initial='',
        label='Email',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Masukkan email',
        }),
    )
    password = forms.CharField(
        initial='',
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Masukkan password',
        }),
    )
