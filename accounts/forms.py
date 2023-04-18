from django.contrib.auth import get_user_model
User = get_user_model()


from django import forms
from django.contrib.auth.forms import UserCreationForm

class Login(forms.Form):
    email = forms.EmailField(label="EMAIL", required=True)
    password = forms.CharField(label="PASSWORD", required=True, widget=forms.PasswordInput())

class Register(UserCreationForm):
    email = forms.EmailField(label="EMAIL", required=True)
    name = forms.CharField(label="USERNAME", max_length=15, required=True)
    password = forms.CharField(label="PASSWORD", required=True, widget=forms.PasswordInput())
    password2 = None
    password1 = None

    class Meta:
        model = get_user_model()
        fields = ('name', 'email', 'password')
