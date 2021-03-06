from django import forms
from django.forms.models import ModelForm

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from userprofile.models import UserProfile


class EditProfileForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = [
            'about'
        ]

    email = forms.EmailField()
    email.label = _('Email')

    first_name = forms.CharField(max_length=User._meta.get_field('first_name').max_length)
    first_name.label = _('Имя')

    last_name = forms.CharField(max_length=User._meta.get_field('last_name').max_length)
    last_name.label = _('Фамилия')

    avatar = forms.ImageField()
    avatar.label = _('Загрузить фото')

    def update_initial(self):
        self.fields['email'].initial = self.instance.user.email
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name

    def clean_email(self):
        email = self.cleaned_data['email']

        try:
            user = User.objects.get(email=email)
            if user == self.instance.user:
                return email

        except User.DoesNotExist:
            return email

        raise forms.ValidationError(
            _('Пользователь с таким Email:%(value)s уже зарегистрирован.'),
            code='email_unique',
            params={'value': email}
        )

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']
        print('avatar', avatar)
        return avatar

    def save(self, commit=True):
        self.instance.user.email = self.cleaned_data['email']
        self.instance.user.username = self.instance.user.email
        self.instance.user.first_name = self.cleaned_data['first_name']
        self.instance.user.last_name = self.cleaned_data['last_name']
        self.instance.user.save()
        self.instance.about = self.cleaned_data['about']
        self.instance.avatar = self.cleaned_data['avatar']
        self.instance.save()
        return self.instance


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

    about = forms.CharField(widget=forms.Textarea())
    about.label = _('Расскажите о себе')
    about.required = False

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
        try:
            if cleaned_data['password'] == cleaned_data['password_repeat']:
                return cleaned_data
        except Exception:
            pass

        raise forms.ValidationError(
            _('Введенные пароли не совпадают'),
            code='do_not_match'
        )

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
        user_profile.about = self.cleaned_data['about']
        user_profile.save()
        return user_profile

    def get_user(self):
        return self.save().user