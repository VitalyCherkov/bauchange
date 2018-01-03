from django import forms


class LoginForm(forms.Form):
    login = forms.CharField()
    login.required = True
    login.label = 'Логин'
    password = forms.CharField(widget=forms.PasswordInput())
    password.required = True
    password.label = 'Пароль'
