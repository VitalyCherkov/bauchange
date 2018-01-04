from django import forms

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from userprofile.models import UserProfile


class SignUpForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SignUpForm, self).__init__(*args, **kwargs)

    email = forms.EmailField()
    email.label = _('Email')

    password = forms.CharField(widget=forms.PasswordInput())
    password.label = _('Пароль')

    password_repeat = forms.CharField(widget=forms.PasswordInput())
    password_repeat.label = _('Повторите пароль')

    first_name = forms.CharField(max_length=User._meta.get_field('first_name').max_length)
    first_name.label = _('Имя')

    last_name = forms.CharField(max_length=User._meta.get_field('last_name').max_length)
    last_name.label = _('Фамилия')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise forms.ValidationError(
            _('Пользователь с таким Email:%(value)s уже зарегистрирован.'),
            code='email_unique',
            params={'value': email}
        )

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        if cleaned_data['password'] != cleaned_data['password_repeat']:
            raise forms.ValidationError(
                _('Введенные пароли не совпадают'),
                code='do_not_match'
            )

        return cleaned_data

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['email'],
            email=self.cleaned_data['email']
        )
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        user.set_password(self.cleaned_data['password'])
        user.save()

        user_profile = UserProfile(
            user=user
        )

        user_profile.save()
        return user_profile

    def get_user(self):
        return self.save().user


