from django import forms


class LoginForm(forms.Form):
    user = forms.CharField(max_length=100)
    passwork = forms.CharField(widget=forms.PasswordInput)
