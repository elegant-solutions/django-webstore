from django import forms

from .models import SignUp


class SignUpForm(forms.ModelForm):
    """ Data validation for user's email and name input on Sign Up Form. """
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name
