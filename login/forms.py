from django import forms
from .models import User
from django.core import validators


class UserRegistrationForm(forms.ModelForm):
    rpassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                                label='Password Again')

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'email', 'mobile', 'password', 'rpassword')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mobile'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        }

    def clean(self):
        cleaned_data = super().clean()
        valrpassword = self.cleaned_data['rpassword']
        valpassword = self.cleaned_data['password']

        if valpassword != valrpassword:
            raise forms.ValidationError('Password Does not match')


class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email / Username'}),
                             label='Email / Username')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                               label='Password')

    def clean(self):
        cleaned_data = super().clean()
